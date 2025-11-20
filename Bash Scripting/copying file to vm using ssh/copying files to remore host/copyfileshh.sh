#!/bin/bash

REMOTE_USER="fatih"
REMOTE_HOST="192.168.0.241"
LOCAL_FILE="/home/fatih/Documents/nashid.txt"
REMOTE_DEST="/home/fatih/Documents/"

scp "$LOCAL_FILE" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_DEST"

