import pygame
import random
# Aqui está um jogo criado com base total em aprendizado, divirtam-se
# Configurações iniciais
pygame.init()
amarelo, preto, verde, vermelho = (255, 255, 102), (0, 0, 0), (0, 255, 0), (213, 50, 80)
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game - Teste de Proteção')
relogio = pygame.time.Clock()

def jogo():
    sair = False
    x, y = largura / 2, altura / 2
    dx, dy = 0, 0
    corpo, tam = [], 1
    comida_x = round(random.randrange(0, largura - 10) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - 10) / 10.0) * 10.0

    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: dx, dy = -10, 0
                elif event.key == pygame.K_RIGHT: dx, dy = 10, 0
                elif event.key == pygame.K_UP: dx, dy = 0, -10
                elif event.key == pygame.K_DOWN: dx, dy = 0, 10

        x += dx
        y += dy
        tela.fill(preto)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, 10, 10])
        
        corpo.append([x, y])
        if len(corpo) > tam: del corpo[0]
        for parte in corpo[:-1]:
            if parte == [x, y]: sair = True
        
        for parte in corpo:
            pygame.draw.rect(tela, amarelo, [parte[0], parte[1], 10, 10])
        
        pygame.display.update()
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - 10) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - 10) / 10.0) * 10.0
            tam += 1
        relogio.tick(15)
    pygame.quit()

if __name__ == "__main__":
    jogo()