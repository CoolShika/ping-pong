from pygame import *
import pygame
'''Необходимые классы'''
#comment 
#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.player_image = player_image
       self.wight = wight
       self.height = height
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
   
   def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y) 

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def change_img(self, img):
        self.image = transform.scale(image.load(img), (self.wight, self.height))

class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = Rect(x, y, width, height) #прямоугольник
      self.fill_color = color
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      draw.rect(window, self.fill_color, self.rect)
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)      
'''класс надпись'''
class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
BLACK = (0,0,0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
PAPAYA_WHIP = (255, 239, 213)

#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
#флаги, отвечающие за состояние игры
game = True
startGame = False
menuOn = False
clock = time.Clock()
FPS = 60
 
#создания мяча и ракетки   
user_racket_img = ''
r1 = Player('line.png',  30, 200, 4, 100, 150) 
r2 = Player('line.png', 520, 200, 4, 100, 150)
ball = GameSprite('ball.jpg', 200, 200, 4, 50, 50)
 
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
 
speed_x = 3
speed_y = 3

menu = []
play = Label(250, 250 , 80, 40, GREY)
play.set_text("PLAY", 30, RED)
store = Label(240, 250 + 40, 110, 40, GREY)
store.set_text("STORE", 30, RED)
button_back = Label(0, win_height - 40 , 90, 40, GREY)
button_back.set_text("BACK", 30, BLACK)
menu.append(play)
menu.append(store)

x = 30
store_racket = []
img_names = ["line.png"]
for i in range(1): 
    racket = GameSprite(img_names[i], x, 20, 4, 50, 130)
    store_racket.append(racket)
    x += 140

while game:
    window.fill((200, 255, 255))
    play.draw()
    store.draw()

    
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if play.collidepoint(x, y): #play
                startGame = True
                ball.rect.x = 200
                ball.rect.y = 200
            if store.collidepoint(x, y):
                menuOn = True
            if button_back.collidepoint(x, y):
                menuOn = False
            for racket in store_racket:
                if racket.collidepoint(x, y):
                    print(racket.player_image)
                    r1.change_img(racket.player_image) 
    if startGame:
       window.fill(back)
       r1.update_l()
       r2.update_r()
       ball.rect.x += speed_x
       ball.rect.y += speed_y
 
       if sprite.collide_rect(r1, ball) or sprite.collide_rect(r2, ball):
           speed_x *= -1
           speed_y *= 1
      
       #если мяч достигает границ экрана, меняем направление его движения
       if ball.rect.y > win_height-50 or ball.rect.y < 0:
           speed_y *= -1
 
       #если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
       if ball.rect.x < 0:
           startGame = False
           window.blit(lose1, (200, 200))
           #game_over = True
 
       #если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
       if ball.rect.x > win_width:
           startGame = False
           window.blit(lose2, (200, 200))
           #game_over = True
 
       r1.reset()
       r2.reset()
       ball.reset()
    
    if menuOn:
        window.fill(PAPAYA_WHIP)
        for racket in store_racket:
            racket.reset()
        button_back.draw()
       


    display.update()
    clock.tick(FPS)
