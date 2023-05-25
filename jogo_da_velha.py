import pygame
import sys
import random

pygame.init()

BRANCO = (255, 202, 152)
PRETO = (0, 0, 0)
VERMELHO = (246, 41, 19)

largura_janela = 300
altura_janela = 400
tamanho_quadrado = 100
largura_linha = 5

janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo da Velha")

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

pontos_x = 0
pontos_o = 0

fonte = pygame.font.Font(None, 36)
pontos_x_texto = fonte.render("Pontos X: {}".format(pontos_x), True, PRETO)
pontos_o_texto = fonte.render("Pontos O: {}".format(pontos_o), True, PRETO)

def desenhar_tabuleiro():
    janela.fill(BRANCO)

    for linha in range(1, 3):
        pygame.draw.line(janela, PRETO, (0, linha * tamanho_quadrado), (largura_janela, linha * tamanho_quadrado), largura_linha)
        pygame.draw.line(janela, PRETO, (linha * tamanho_quadrado, 0), (linha * tamanho_quadrado, altura_janela - tamanho_quadrado), largura_linha)

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == "X":
                pygame.draw.line(janela, VERMELHO, (coluna * tamanho_quadrado + 20, linha * tamanho_quadrado + 20), ((coluna + 1) * tamanho_quadrado - 20, (linha + 1) * tamanho_quadrado - 20), largura_linha)
                pygame.draw.line(janela, VERMELHO, ((coluna + 1) * tamanho_quadrado - 20, linha * tamanho_quadrado + 20), (coluna * tamanho_quadrado + 20, (linha + 1) * tamanho_quadrado - 20), largura_linha)
            elif tabuleiro[linha][coluna] == "O":
                pygame.draw.circle(janela, VERMELHO, (coluna * tamanho_quadrado + tamanho_quadrado // 2, linha * tamanho_quadrado + tamanho_quadrado // 2), tamanho_quadrado // 2 - 20, largura_linha)

    pontos_x_texto = fonte.render("Pontos X: {}".format(pontos_x), True, PRETO)
    pontos_o_texto = fonte.render("Pontos O: {}".format(pontos_o), True, PRETO)
    janela.blit(pontos_x_texto, (10, altura_janela - 60))
    janela.blit(pontos_o_texto, (10, altura_janela - 30))

def verificar_vencedor():
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] and tabuleiro[linha][0] != " ":
            return tabuleiro[linha][0]

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != " ":
            return tabuleiro[0][coluna]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
        return tabuleiro[0][0]
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
        return tabuleiro[0][2]

    if all(tabuleiro[linha][coluna] != " " for linha in range(3) for coluna in range(3)):
        return "Empate"

    return None

def reiniciar_jogo():
    global tabuleiro

    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

jogador_atual = "X"

jogando = True
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and jogador_atual == "X":

            linha = evento.pos[1] // tamanho_quadrado
            coluna = evento.pos[0] // tamanho_quadrado

            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador_atual

                resultado = verificar_vencedor()
                if resultado:
                    if resultado == "Empate":
                        pass
                    else:
                        if resultado == "X":
                            pontos_x += 1
                        else:
                            pontos_o += 1

                    reiniciar_jogo()
                else:
                    jogador_atual = "O"

    if jogador_atual == "O" and not verificar_vencedor():
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)

        while tabuleiro[linha][coluna] != " ":
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)

        tabuleiro[linha][coluna] = jogador_atual
        jogador_atual = "X"

    desenhar_tabuleiro()

    pygame.display.update()

pygame.quit()
