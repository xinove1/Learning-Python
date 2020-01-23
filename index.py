jogo = [[0,0,0],
        [0,0,0],
        [0,0,0],]

jogador1 = 1
jogador2 = 2

def tabuleiro(mapa_jogo,jogador=0, linha=0, coluna=0, visualizar= False):
    print("   a  b  c")
    if not visualizar:
        mapa_jogo[linha][coluna] = jogador
    for count, linha in enumerate(mapa_jogo):
        print(count, linha)
    return(mapa_jogo)    
    
jogo = tabuleiro(jogo, 1, 0, 2)    
#tabuleiro(visualizar=True)