#!/usr/bin/env bash


cat /root/.ssh/id_rsa.pub >> /cache/ssh/authorized_keys
awk '!a[$0]++' /cache/ssh/authorized_keys

python ./disk-usage.py $SSH_USERNAME

tail -f /dev/null
