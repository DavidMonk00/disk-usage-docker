#!/usr/bin/env bash


cat /root/.ssh/id_rsa.pub >> /cache/ssh/authorized_keys
awk '!a[$0]++' /cache/ssh/authorized_keys

ip=$(python ipaddress.py)

ssh -o StrictHostKeyChecking=no dmonk@$ip "df"

tail -f /dev/null
