#!/usr/bin/env bash

ip=$(python ipaddress.py)

ssh -o StrictHostKeyChecking=no dmonk@$ip "pydf"
