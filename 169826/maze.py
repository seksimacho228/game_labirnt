from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,image_sprite,x,y,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_sprite),(65,65))  
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def show_image(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class rotate(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] == True:
            self.rect.x -= self.speed
        if keys[K_d] == True:
            self.rect.x += self.speed
        if keys[K_w] == True:
            self.rect.y -= self.speed
        if keys[K_s] == True:
            self.rect.y += self.speed
        
class Enemy(GameSprite):
    right_left = 'left'
    def move(self):
        if self.rect.x <= 470:
            self.right_left = 'right'
        if self.rect.x >= win_widght  - 85:
            self.right_left = 'left'

        if self.right_left == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,wall_x,wall_y,wall_width,wall_high):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.wall_high = wall_high
        self.wall_width = wall_width

        self.image = Surface((self.wall_width,self.wall_high))
        self.image.fill((self.color1,self.color2,self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def show_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

win_widght = 700
win_high = 500

window = display.set_mode((win_widght,win_high))
display.set_caption('ПРОИГРАТОПГГВПАСАСИНСТАЛКЕРЕГОРКРИД')

bg = transform.scale(image.load('background.jpg'),(win_widght,win_high))

igrok = Player('hero.png',5,win_high-70,4)
lox = Enemy('cyborg.png',win_widght-80,280,2)
end = GameSprite('treasure.png',win_widght-120,win_high-80,0)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

clock = time.Clock()
run = True
finish = False

w1 = Wall(100,200,100, 100,40,200,30)
w2 = Wall(100,200,100, 300,10,200,30)
w3 = Wall(100,200,100, 100,440,200,30)
w4 = Wall(100,200,100, 100,10,200,30)

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('ТЫ ЛОХ ЕБАНЫЙ ', True, (180, 0, 0))

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    
    if finish != True:
        window.blit(bg,(0,0))
        igrok.show_image()
        lox.show_image()
        end.show_image()
        w1.show_wall()
        w2.show_wall()
        w3.show_wall()
        w4.show_wall()
    igrok.move()
    lox.move()

    if sprite.collide_rect(igrok,lox) or sprite.collide_rect(igrok,w1) or sprite.collide_rect(igrok,w2) or sprite.collide_rect(igrok,w3) or sprite.collide_rect(igrok,w4):
        finish = True 
        window.blit(lose,(200,200))

    if sprite.collide_rect(igrok,end):
        finish = True
        window.blit(lose,(200,200))

    display.update()
    clock.tick(60)