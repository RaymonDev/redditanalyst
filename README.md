# Reddit Analyst
A python script that gets the posts in r/depression by the top specified redditors of a desired subreddit


.
## Before using the script, you need to create your own Reddit App, and enter the Cliend ID and the secret token in the specified section of the code. Click [here](https://www.reddit.com/prefs/apps) to create it
.

## How it works
This script gets the top specified redditors (from hot) that posted on a desired subreddit and analizes their account to se if they ever posted on r/depression. Then, returns the number of  all the posts of r/depression by the top specified number of users (from hot) of a desired subreddit. The script can be slightly modified to show the posts of the users, simply uncomment line __ of the main.py file.

This repository also includes a graph.py script, that, after specifying the needed info, graphs your results. In a future update, I will combine both of them.

### Requisites:

This program requires PRAW

    pip install praw
    
Beepy

    pip install beepy
    
Matplotlib (for the graph script)

    pip install matplotlib

### Installing

- Download or clone the repository.
- Execute the Python file (with launcher.bat or witht any other prefered method)
- A command prompt window should appear.

### How to use:
- Create the reddit bot
- Execute the script (a command prompt window should appear)
- Introduce the desired subbredit to analyse.
- Press enter
- Wait until the programm makes a sound.
- Press enter. A txt file will be created with the exact same information as the terminal.
- (optional) Graph the info with the graph.py file 

### Works for sure on:

- Windows 10 with Python 3.9
