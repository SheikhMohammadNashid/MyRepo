#!/bin/bash

REMOTE_USER="fatih"
REMOTE_HOST="192.168.0.241"
REMOTE_FILE="/home/fatih/Documents/nashid.txt"
LOCAL_DEST="/home/fatih/Downloads"

scp "$REMOTE_USER@$REMOTE_HOST:$REMOTE_FILE" "$LOCAL_DEST"

