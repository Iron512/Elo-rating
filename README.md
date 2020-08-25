# Elo rating

I wanted to develop a basic Elo rating system, for any two player games, where the game's output can either win, draw or lose.
I have no real use for this system right now, but you never know.

## Setup

The system uses by now python3 and JSON file format to store users data and configuration. 
Everything runs on a virtual environment, called `virtual`. No need sticking to this name, in case remember to configure *.gitignore* accordingly.

`
$	pyhton3 - m venv virtual
`

Then activate the environment and install all the required packages. They are stored inside the *environment.txt* file.

`
$ 	. virtual/bin/activate
`

`
$	pip install -r environment
`

If, while working you installed new packages, no changes will be saved on the repo, since the folder *virtual* is excluded by the *.gitignore*. The correct way to save a file is updating the *environment.txt* file, simply issuing

`
$	pip freeze > environment.txt
`

## Config and Usage

TBD