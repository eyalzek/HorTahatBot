#!/bin/bash

function pull {
    cd /home/truser/repos/HorTahatBot
    git fetch
    LOCAL=$(git rev-parse @)
    REMOTE=$(git rev-parse @{u})

    if [ $LOCAL = $REMOTE ]; then
        echo "Up-to-date"
        return 1
    else
        echo "Need to pull"
        git pull
        return 0
    fi
}

function restart_bot {
    # kill running bot
    tmux send -t telebot "kill $(pidof python telebot.py)" ENTER
    sleep 2
    # start it again
    tmux send -t telebot "python /home/truser/repos/HorTahatBot/telebot.py &" ENTER
}

if pull; then
    restart_bot
else
    echo "no changes have been made"
fi
