# Rock, Paper and Scissors

## How the Game Works

There are three different options in this game, as the name suggests: Rock, Paper and Scizor. You and your opponent choose one of them, and then we compare your choices to determine who wins.

Here are the winning conditions:

- **Rock > Scissors**: Rock is harder than scissors, and scissors CAN'T cut rocks.
- **Scissors > Paper**: Scissors can easily cut paper, and paper CAN'T do anything against scissors.
- **Paper > Rock**: Paper wraps around rock, and rock CAN'T damage paper. Unless you throw it... BUT I DIDN'T CREATE THE GAME RULES SOOOOO YEAH.

That's basically how the game works! If you're planning to play with a friend (no, it's not online, but you can still play on the same local machine :D), it's better to take turns. In PvP mode, one player should make their choice without the other looking at the screen, then let the other player take their turn.

## About the Code

I made some decisions along the way while developing this project. Initially, I implemented the winning logic using an `if` statement with Player 1 as the reference, like this:

```python
if (player1 == "rock" and player2 == "scissors") or ...
```

But the condition was getting too long, and I didn't really like how it looked. So I decided to use a dictionary instead, making the code cleaner and easier to read.

I'm still using Player 1 as the reference, but now I look up the winning condition in a dictionary using the player's choice as a key, like this:

![Winning logic using a dictionary](https://github.com/user-attachments/assets/bf374ddb-a51e-4f6d-aa2f-a2e487dd600c)

This approach makes the logic clearer and much easier to maintain.

Another thing I did in this project, as well as in my TicTacToe game, was create a class to handle the console interface. I think separating the interface into its own object makes the code more organized and easier to understand.

If I want to change something about the interface, I can simply go to the class and modify it there. I also think this is a good way to prepare myself for creating real graphical interfaces in the future.

Finally, the game features two player modes:

- **PvP (Player vs. Player)**
- **PvE (Player vs. Environment)**

And two game modes:

- **OneShot**: Just one round.
- **3 Rounds**: A best-of-three format.

In PvE mode, the computer randomly chooses one of the available options. There is no AI or advanced logic behind its decisions yet; it simply uses `randint`. This makes its choices a little unpredictable, though! :D
