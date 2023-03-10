import pygame, random, time, sys
pygame.init()
pygame.display.set_icon(pygame.image.load("logoIMS.png"))
pygame.font.init()
pygame.display.set_caption('IMS Bird')
bird, bird_dead, window, font, font2, clock, start, vel, ypos, hscore, pipe, tscore, died = pygame.image.load("logo.png"), pygame.image.load("logolose.png"), pygame.display.set_mode((720,720)), pygame.font.SysFont('Arial', 72), pygame.font.SysFont('Arial', 36), pygame.time.Clock(), False, 7., 300, 0, [720,random.randint(0,380)], 0, False
caption = font2.render('Aperte ESPAÇO para começar', True, (0,0,0), None)
while True:
    window.fill((120,120,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if start == False:
                ypos, start = 300, True
            vel = 7.
    if start:
        window.blit(bird,(50,ypos))
        ypos, vel, pipe[0] = ypos - vel, vel - 0.5, pipe[0] - 5
        pygame.draw.rect(window,(0,255,0),(pipe[0],0,50,pipe[1]))
        pygame.draw.rect(window,(0,255,0),(pipe[0],pipe[1]+300,50,720))
        window.blit(font2.render('Pontuação: ' + str(tscore), True, (0,0,0), None),(10,10))
        if pipe[0] < -50:
            pipe, tscore = [720, random.randint(0,380)], tscore + 1
            if tscore > hscore:
                hscore = tscore
    else:
        if died:
            window.blit(bird_dead,(100,500))
        window.blit(font.render('IMS Bird', True, (0,0,0), None),(100,100))
        window.blit(caption,(100,300))
        window.blit(font2.render('Pontuação mais alta - ' + str(hscore), True, (0,0,0), None),(100,400))
    if ypos >= 528 or ((pipe[0] < 164 and pipe[0] > 14) and (ypos+192 > pipe[1]+300 or ypos < pipe[1])):
        ypos, start, tscore, pipe[0], died, caption = 528, False, 0, 720, True, font2.render('Você perdeu', True, (0,0,0), None)
    elif ypos < 0:
        ypos, vel = 0, -abs(vel)
    clock.tick(60)
    pygame.display.flip()

#By: Max Muller