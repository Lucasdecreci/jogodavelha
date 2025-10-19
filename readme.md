# Jogo da Velha em Python  

Este projeto implementa o clássico jogo da velha (tic-tac-toe) para dois jogadores no terminal, utilizando a linguagem **Python**.  

---

## 📌 Pré-requisitos  
- Python **3.8** ou superior instalado.  
- Terminal (Prompt de Comando, PowerShell, ou Terminal do Linux/Mac).  

---

## 🚀 Instalação  

1. **Verificar se o Python está instalado**  
   ```bash
   python --version
   ```  
   ou  
   ```bash
   python3 --version
   ```  

2. **Clonar ou salvar o código**  
   - Copie o conteúdo do código para um arquivo chamado:  
     ```
     jogo_da_velha.py
     ```  

3. **Abrir o terminal e acessar a pasta** onde o arquivo foi salvo:  
   ```bash
   cd caminho/da/pasta
   ```

---

## ▶️ Execução  

No terminal, execute o comando:  

```bash
python jogo_da_velha.py
```  
ou, em alguns sistemas:  

```bash
python3 jogo_da_velha.py
```

---

## 🕹️ Como jogar  

- O tabuleiro 3x3 será exibido no terminal.  
- O programa informa de quem é a vez (**Jogador X** ou **Jogador O**).  
- Cada jogador deve escolher uma **linha (0, 1 ou 2)** e uma **coluna (0, 1 ou 2)** para marcar sua jogada.  
- O jogo termina quando:  
  - Um jogador completa três símbolos iguais em linha, coluna ou diagonal (**vitória**);  
  - Todas as casas são preenchidas sem vencedor (**empate**).  

---

⚠️ Entradas inválidas (número fora do intervalo ou posição já ocupada) serão rejeitadas, e o programa solicitará uma nova jogada. 