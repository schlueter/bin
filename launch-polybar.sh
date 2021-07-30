#!/usr/bin/env bash

set -e
exec > >(tee -a "$XDG_CONFIG_HOME/polybar.log") 2>&1

echo "Terminating any current polybar instances..." >&2
for fifo in .xmonad-workspace-log .xmonad-title-log
do
    if [ -f "/tmp/$fifo" ]
    then
        rm "/tmp/$fifo"
    fi
    if ! [ -p "/tmp/$fifo" ]
    then
        mkfifo "/tmp/$fifo"
    fi
done
# Terminate already running bar instances
if ! killall -q -s SIGUSR1 polybar
then
    polybar main >>"$XDG_CONFIG_HOME/polybar.log"
    echo "Polybar successfully started." >&2
else
    echo "Polybar reloaded."
fi
