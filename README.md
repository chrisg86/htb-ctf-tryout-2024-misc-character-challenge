# HTB CTF - Try Out - 2024 - Misc: Character challenge

> Security through Induced Boredom is a personal favourite approach of mine. Not as exciting as something like The Fray, but I love making it as tedious as possible to see my secrets, so you can only get one character at a time!

## Overview
Upon spinning up the docker container, you retrieve a `nc` (netcat) command to the ip and port. Firing that command in the terminal presents the following message:

> Which character (index) of the flag do you want? Enter an index: 

Enter an index like 0, 1, 2 and you quickly realize that parts of the flag are returned one by one:

> Character at Index 0: H

> Character at Index 1: T

> Character at Index 2: B

Let's script this in order to retrieve the entire flag. We can do so by using the `socket` python module.

## How to run
Run via `HOST=1.1.1.1 PORT=11111 uv run python main.py` and provide `HOST` and `PORT`:

```
HOST=1.1.1.1 PORT=11111 uv run python main.py
```

You can probably skip `uv` alltogether if you want and run with `python` directly.

## Dependencies

None 🎉
