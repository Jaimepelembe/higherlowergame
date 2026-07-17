# 📊 Jogo Higher Lower (Higher Lower Game)

Um jogo de "Higher ou Lower" desenvolvido em Python, onde o jogador compara duas contas/personalidades pelo número de seguidores no Instagram e tenta adivinhar qual tem mais seguidores.

## 📋 Descrição

Este é um jogo clássico de comparação onde são apresentadas duas contas ao jogador (uma "A" e uma "B"), com nome, descrição e país, e o jogador deve adivinhar qual das duas tem mais seguidores no Instagram. A cada acerto, uma nova conta entra em jogo e o objetivo é manter a sequência de acertos o maior tempo possível. O projeto foi desenvolvido como parte dos meus estudos de Python (utilizando o curso 100 Days of Code - App Brewery).

## ✨ Funcionalidades

- Escolha aleatória de contas a partir de uma base de dados com centenas de personalidades e marcas;
- Comparação entre duas contas por número de seguidores;
- Contagem da pontuação (streak) do jogador;
- Limpeza do ecrã entre rondas para melhor visualização;
- Mensagens de vitória (acerto) e derrota (fim de jogo).

## 🛠️ Tecnologias utilizadas

- Python 3.13.12
- Git version 2.53.0.windows.1
- Github

## 📁 Estrutura do projeto

```
higherlowergame/
├── main.py             # Arquivo principal 
├── gameData.py         # Base de dados com as contas (nome, seguidores, descrição, país)
├── art.py               # Arte ASCII/logotipo exibido no jogo
├── fileOperations.py  #Funções de leitura e escrita em arquivos
├── higerLower.py       # Arquivo com a lógica do jogo
├── highScore.txt       # Arquivo que armazena a pontuação máxima obtida no jogo
├── higherlower flowchart.drawio
├── higherlower flowchart.png
├── LICENSE

```

## 🚀 Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Jaimepelembe/higherlowergame.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd higherlowergame
   ```
3. Execute o jogo:
   ```bash
   python main.py
   ```

## 🎮 Como jogar

1. Ao iniciar, são apresentadas duas contas: A (já revelada) e B (a comparar).
2. Deves adivinhar se a conta B tem **mais** ou **menos** seguidores do que a conta A, digitando `A` ou `B`.
3. Se acertares, a conta B passa a ser a nova conta A e uma nova conta B entra em jogo, aumentando a tua pontuação.
4. O jogo termina quando erras a comparação, sendo apresentada a tua pontuação final.

## 👤 Autor

Desenvolvido por **Jaime Fernando**
- GitHub: [@jaimepelembe](https://github.com/jaimepelembe)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.