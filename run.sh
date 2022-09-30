#!/bin/bash
cd /workspace/rubbishbot &&
nohup python bot.py &
cd /workspace/rubbishbot/gocqhttps &&
nohup ./go-cqhttp &
