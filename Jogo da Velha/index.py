jogo = [[1,0,1],
        [0,0,0],
        [0,0,0],]




def tabuleiro(mapa_jogo,jogador=0, linha=0, coluna=0, visualizar= False):
    print("   a  b  c")
    if not visualizar:
        mapa_jogo[linha][coluna] = jogador
    for count, linha in enumerate(mapa_jogo):
        print(count, linha)
    return(mapa_jogo)    
    
def win(jogo):
    for row in jogo:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("winner")


 The quick brown fox jumped over the lazy dog