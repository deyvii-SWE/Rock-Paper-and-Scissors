# Rock, Paper and Scissors

## Como o Jogo Funciona

Existem três opções diferentes neste jogo, como o próprio nome sugere: Pedra, Papel e Scizor. Você e seu oponente escolhem uma delas, e então comparamos suas escolhas para determinar quem vence.

Aqui estão as condições de vitória:

- **Pedra > Tesoura**: A pedra é mais resistente que a tesoura, e a tesoura NÃO CONSEGUE cortar pedras.
- **Tesoura > Papel**: A tesoura pode cortar papel facilmente, e o papel NÃO CONSEGUE fazer nada contra a tesoura.
- **Papel > Pedra**: O papel envolve a pedra, e a pedra NÃO CONSEGUE causar nenhum dano ao papel. A menos que você jogue ela... MAS EU NÃO CRIEI AS REGRAS DO JOGO ENTÃOOOOO É ISSO.

Basicamente, é assim que o jogo funciona! Se você está pensando em jogar com um amigo (não, não é online, mas vocês ainda podem jogar na mesma máquina local :D), é melhor jogar por turnos. No modo PvP, um jogador deve fazer sua escolha sem que o outro olhe para a tela, e depois deixar o outro jogador fazer sua jogada.

## Sobre o Código

Fiz algumas escolhas durante o desenvolvimento deste projeto. Inicialmente, implementei a lógica de vitória utilizando um `if`, tomando o Player 1 como referência, assim:

```python
if (player1 == "rock" and player2 == "scissors") or ...
```

Mas a condição estava ficando muito extensa, e eu realmente não gostei de como ela estava. Então decidi utilizar um dicionário, tornando o código mais limpo e fácil de ler.

Ainda estou utilizando o Player 1 como referência, mas agora procuro a condição de vitória em um dicionário utilizando a escolha do jogador como chave, assim:

![Lógica de vitória utilizando um dicionário](https://github.com/user-attachments/assets/bf374ddb-a51e-4f6d-aa2f-a2e487dd600c)

Essa abordagem deixa a lógica mais clara e muito mais fácil de manter.

Outra coisa que fiz neste projeto, assim como no meu jogo de TicTacToe, foi criar uma classe para lidar com a interface do console. Acho que separar a interface em seu próprio objeto deixa o código mais organizado e fácil de entender.

Se eu quiser mudar alguma coisa na interface, posso simplesmente ir até a classe e modificá-la por lá. Também acredito que essa seja uma boa maneira de me preparar para criar interfaces gráficas de verdade no futuro.

Por fim, o jogo possui dois modos de jogadores:

- **PvP (Player vs. Player)**
- **PvE (Player vs. Environment)**

E dois modos de jogo:

- **OneShot**: Apenas uma rodada.
- **3 Rounds**: Um formato de melhor de três.

No modo PvE, o computador escolhe aleatoriamente uma das opções disponíveis. Ainda não existe nenhuma IA ou lógica avançada por trás de suas decisões; ele simplesmente utiliza `randint`. Isso torna suas escolhas um pouco imprevisíveis, porém! :D
