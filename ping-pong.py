from pygame import * 
from random import randint 
 
 
 
 
win_width = 500 
win_height = 500 
window = display.set_mode((win_width, win_height)) 
 
 
class GameSprite(sprite.Sprite): 
  
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (65, 65)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
  
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
 
 
 
 
class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 700 - 80: 
            self.rect.y += self.speed 
    def update2(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 700 - 80: 
            self.rect.y += self.speed 
fon = transform.scale(image.load("fon.jpg"),(500,500)) 
plat = Player('1.png.png', 5, win_width - 80,4) 
plat2 = Player('3.png.png', 435, win_width - 80,4) 
mach = transform.scale(image.load("4.png.png"),(80,80)) 
 
 
 
 
 
 
run = True 
clock = time.Clock() 
FPS = 60 
while run: 
     
    for i in event.get(): 
        if i.type == QUIT: 
            run = False 
 
 
 
    window.blit(fon,(0,0)) 
    window.blit(mach,(200,200)) 
    plat.update() 
    plat.reset() 
    plat2.update2() 
    plat2.reset()     
 
    display.update() 
    clock.tick(FPS)
