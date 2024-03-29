import pygame
import random
import time
import sys

# Inicialize o Pygame
pygame.init()

# Carregue a imagem de fundo
background1 = pygame.image.load("ims.png")
background2 = pygame.image.load("ceu.png")

# Defina a largura e a altura da tela
width, height = 720, 720

# Crie a tela
window = pygame.display.set_mode((width, height))

# Defina o ícone da janela
pygame.display.set_icon(pygame.image.load("logoIMS.png"))

# Carregue as imagens dos objetos do jogo
bird = pygame.image.load("plan.png")
bird_dead = pygame.image.load("lose.png")

# Crie as fontes
font = pygame.font.SysFont('Arial', 72)
font2 = pygame.font.SysFont('Arial', 27)
font3 = pygame.font.SysFont('Arial', 25)

# Defina o relógio
clock = pygame.time.Clock()

# Defina as variáveis do jogo
game_state = 0 # 0: Jogo ainda não começou, 1: Jogo em andamento, 2: Jogo terminou
vel = 7.
ypos = 300
hscore = 0
pipe = [720, random.randint(0,380)]
tscore = 0
died = False

# Crie a legenda de início
caption = font2.render('', True, (104,34,139), None)

# Loop principal do jogo
while True:

    # Desenhe o fundo
    if game_state == 1:
        window.blit(background2, (0, 0))
    else:
        window.blit(background1, (0, 0))

    # Trate os eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_state == 0:
                ypos, game_state = 300, 1
            vel = 7.

    # Desenhe os objetos do jogo se o jogo estiver em andamento
    if game_state == 1:
        window.blit(bird,(50,ypos))
        ypos, vel, pipe[0] = ypos - vel, vel - 0.5, pipe[0] - 5
        pygame.draw.rect(window,(0,255,0),(pipe[0],0,50,pipe[1]))
        pygame.draw.rect(window,(0,255,0),(pipe[0],pipe[1]+130,50,720))
        window.blit(font2.render('Pontuação: ' + str(tscore), True, (255,255,255)), (0, 0))
        if pipe[0] < -50:
            pipe, tscore =[720, random.randint(0,380)], tscore + 1
            if tscore > hscore:
                hscore = tscore

    # Desenhe a tela de título se o jogo ainda não começou
    else:
        if died:
            window.blit(bird_dead,(0,0))
        window.blit(font.render('', True, (0,0,0), None),(160,0))
        window.blit(caption,(150,620))
        window.blit(font3.render('Pontuação mais alta - ' + str(hscore), True, (0,0,0), None),(5,10))

    # Verifique se o avião atingiu um obstáculo ou a borda da tela
    if ypos >= 710 or ((pipe[0] < 170 and pipe[0] > 14) and (ypos+70 > pipe[1]+170 or ypos < pipe[1])):
        ypos, start, tscore, pipe[0], died, caption = 528, False, 0, 720, True, font2.render('', True, (105,89,205), None)
        game_state = 0
    elif ypos < 0:
        ypos, vel = 0, -abs(vel)
    clock.tick(60)
    pygame.display.flip()

    #by: Max Muller