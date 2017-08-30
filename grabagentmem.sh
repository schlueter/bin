#!/bin/bash

# First argument is the output directory.  Use /tmp if this is not specified.
outputdir="/tmp"

# Grab pids for each ssh-agent
sshagentpids=$(ps --no-headers -fC ssh-agent | awk '{print $2}')

# Iterate through the pids and create a memory dump of the stack for each
for pid in $sshagentpids; do
    stackmem="$(grep stack "/proc/$pid/maps" | sed -n 's/^\([0-9a-f]*\)-\([0-9a-f]*\) .*$/\1 \2/p')"
    startstack=$(echo "$stackmem" | awk '{print $1}')
    stopstack=$(echo "$stackmem" | awk '{print $2}')

    gdb --batch -pid "$pid" -ex "dump memory $outputdir/sshagent-$pid.stack 0x$startstack 0x$stopstack" 2&>1 >/dev/null

    # GDB doesn't error out properly if this fails.
    # This will provide feedback if the file is actually created
    if [ -f "$outputdir/sshagent-$pid.stack" ]; then
        echo "Created $outputdir/sshagent-$pid.stack"
    else
        echo "Error dumping memory from $pid"
    fi
done
