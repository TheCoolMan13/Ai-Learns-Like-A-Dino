import pygame
from sys import exit
import random


GAME_WIDTH = 360
GAME_HEIGHT = 780

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH , GAME_HEIGHT))
pygame.display.set_caption("Will i ever get a job? - No")
clock = pygame.time.Clock()

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)


backgroundColor = (209, 234, 209)
window.fill(backgroundColor)
pygame.display.flip()

#534 e linia

def Draw_Start_Line():
    Start_Line_width = 360
    Start_Line_height = 534
    Start_Line_color = ( 0 , 0  , 0)
    pygame.draw.line(window , Start_Line_color, (0 , Start_Line_height) , (Start_Line_width , Start_Line_height) , 5)
    


Character_Width = 180
Character_Height = 500

def Daw_Character(character_x):
    Character_Color = (255 , 0 , 0)
    pygame.draw.rect(window , Character_Color , (character_x, Character_Height , 36 , 70) ) 


Tube_Width = 0
Tube_Height = 0
Tube_Speed = 5 #px/s

def Draw_Tube(tube_y ):
    Tube_Color = (0 , 0 , 0)
    pygame.draw.rect(window , Tube_Color , (Tube_Width, tube_y , 36 , 50) )



Score = 0

while True:
    window.fill(backgroundColor)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if(Character_Width > 0):
                    Character_Width -= 36
            if event.key == pygame.K_d:
                if(Character_Width < GAME_WIDTH - 36):
                    Character_Width += 36
    
    Tube_Height += Tube_Speed
    
    # Checking for colision

    if Tube_Height <= 534:
        Draw_Tube(Tube_Height)
    else:
       # pygame.quit()
       # exit()
        if(Tube_Width == Character_Width):
           Score +=1
           Tube_Height = -50
           Tube_Width = random.choice([0, 36, 72, 108 , 144 , 180 , 216 , 252 , 288, 324])
           print("COLISION")
        else:
           pygame.quit()
           exit()
          
    
    
    Score_text = f"Score : {Score}"
    Score_Surface = my_font.render(Score_text, True, (0,0,0))
    window.blit(Score_Surface, (200 , 10))
    
    Draw_Start_Line()
    Daw_Character(Character_Width)
    pygame.display.update()
    clock.tick(30) #30 fps