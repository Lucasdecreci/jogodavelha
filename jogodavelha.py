
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro: 
        print(" | ".join(linha))
        print("-" * 9) 
def verificar_vencedor(tabuleiro):
    
    for linha in tabuleiro: 
        if linha[0] == linha[1] == linha[2] != " ": 
            return linha[0] 
    
    for col in range(3): 
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] != " ": 
            return tabuleiro[0][col] 
  
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0] 
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ": 
        return tabuleiro[0][2] 
    return None
def verificar_empate(tabuleiro): 
    for linha in tabuleiro: 
        if " " in linha: 
            return False 
    return True
def jogar_jogo_da_velha(): 
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"] 
    turno = 0 

    while True: 
        exibir_tabuleiro(tabuleiro) 
        jogador_atual = jogadores[turno % 2] 
        print(f"Vez do jogador {jogador_atual}") 

        while True: 
            try:
                linha = int(input("Escolha a linha (0, 1, 2): ")) 
                coluna = int(input("Escolha a coluna (0, 1, 2): ")) 
                if tabuleiro[linha][coluna] == " ": 
                    tabuleiro[linha][coluna] = jogador_atual 
                    break 
                else:
                    print("Posição já ocupada. Tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida. Tente novamente.")

        vencedor = verificar_vencedor(tabuleiro) 
        if vencedor: 
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {vencedor} venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro) 
            print("Empate!") 
            break

        turno += 1 
if __name__ == "__main__": 
    jogar_jogo_da_velha() 
