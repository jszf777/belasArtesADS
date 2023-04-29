import pygame
from pygame.locals import *
from sys import exit 
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.2)
#music credits: https://freemusicarchive.org/music/Lo-Bat/Game_Boy/8bp042-01-lo-bat-white_russian/
background_music = pygame.mixer.music.load('Lo-Bat - White Russian.mp3')
collide_sound = pygame.mixer.Sound('mixkit-fairy-arcade-sparkle-866.wav')
pygame.mixer.music.play(-1)

collide_sound = pygame.mixer.Sound('mixkit-fairy-arcade-sparkle-866.wav')

largura = 640
altura = 480 

x_snake = int(largura/2)
y_snake = int(altura/2)

velocidade = 10 
x_controle = velocidade
y_controle = 0

x_bapple = randint(40, 600)
y_bapple = randint(50, 430)

pontos = 0 
font = pygame.font.SysFont('arialblack', 30, False, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('23105418')
relogio = pygame.time.Clock()

lista_snake = []
comprimento_inicial = 5
died = False

def grow_snake(lista_snake):
        for XeY in lista_snake:
            pygame.draw.rect(tela, (234, 22, 142), (XeY[0], XeY[1], 20, 20))

def reiniciar_game():
    global pontos, comprimento_inicial, x_snake, y_snake, lista_snake, lista_head, x_bapple, y_bapple, died
    pontos = 0
    comprimento_inicial = 5
    x_snake = int(largura/2)
    y_snake = int(altura/2)
    lista_snake = []
    lista_head = []
    x_bapple = randint(40, 600)
    y_bapple = randint(50, 430)
    died = False

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = font.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
            if event.type == KEYDOWN:
                if event.key == K_a:
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade
                        y_controle = 0
                if event.key == K_d:
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade
                        y_controle = 0
                if event.key == K_w:
                    if y_controle == velocidade:
                        pass
                    else:
                        y_controle = -velocidade
                        x_controle = 0
                if event.key == K_s:
                    if y_controle == -velocidade:
                        pass
                    else:
                        y_controle = velocidade
                        x_controle = 0

    x_snake = x_snake + x_controle
    y_snake = y_snake + y_controle
    #change colors
    snake = pygame.draw.rect(tela, (234, 22, 142), (x_snake, y_snake, 20, 20))
    bapple = pygame.draw.rect(tela, (30, 175, 237), (x_bapple, y_bapple, 20, 20))

    if snake.colliderect(bapple):
        x_bapple = randint(40, 600)
        y_bapple = randint(50, 430)
        pontos += 1
        collide_sound.play()
        comprimento_inicial = comprimento_inicial + 1

    lista_head = []
    lista_head.append(x_snake)
    lista_head.append(y_snake)

    lista_snake.append(lista_head)

    if lista_snake.count(lista_head) > 1:
        #change font + message 
        font2 = pygame.font.SysFont('arialblack', 20, False, False)
        mensagem = 'Game over! Pressione R para jogar novamente'
        texto_formatado = font2.render(mensagem, True, (255, 0, 0))
        ret_texto = texto_formatado.get_rect()

        died = True 
        while died:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_game()
            
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
    
    if x_snake > largura:
        x_snake = 0
    if x_snake < 0:
        x_snake = largura
    if y_snake < 0:
        y_snake = altura
    if y_snake > altura:
        y_snake = 0

    if len(lista_snake) > comprimento_inicial:
        del lista_snake[0]

    grow_snake(lista_snake)

    tela.blit(texto_formatado, (450,40))

    
    pygame.display.update()