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
    

Should_Spawn_Tube = pygame.USEREVENT + 1
pygame.time.set_timer(Should_Spawn_Tube , 1500) # ms


Tube_Width = 0
Tube_Height = 0
Tube_Speed = 3 #px/s
Tubes = []


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
        if event.type == Should_Spawn_Tube:
            random_x = random.randint(0 , (GAME_WIDTH // 36) - 1) * 36
            new_tube =  pygame.Rect(random_x , -50 , 36 , 50)
            Tubes.append(new_tube)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if(Character_Width > 0):
                    Character_Width -= 36
            if event.key == pygame.K_d:
                if(Character_Width < GAME_WIDTH - 36):
                    Character_Width += 36
    
    
    for tube in Tubes[:]:
        tube.y += Tube_Speed
    
    # Checking for colision
    player_rect = pygame.Rect(Character_Width, Character_Height, 36, 70)
    for tube in Tubes[:]:
        # 1. Move the tube down
        tube.y += Tube_Speed
        
        # 2. Check for COLLISION (Collection)
        if player_rect.colliderect(tube):
            Score += 1
            Tubes.remove(tube)
            print("COLLECTED!")
            continue # Move to the next tube in the list

        # 3. Check for MISS (Game Over)
        # If the bottom of the tube passes the line
        if tube.y + tube.height > 534:
            print("MISSED! GAME OVER")
            pygame.quit()
            exit()

        # 4. Draw the tube
        pygame.draw.rect(window, (0, 0, 0), tube)
    
    
    Score_text = f"Score : {Score}"
    Score_Surface = my_font.render(Score_text, True, (0,0,0))
    window.blit(Score_Surface, (200 , 10))
    
    Draw_Start_Line()
    Daw_Character(Character_Width)
    pygame.display.update()
    clock.tick(30) #30 fps