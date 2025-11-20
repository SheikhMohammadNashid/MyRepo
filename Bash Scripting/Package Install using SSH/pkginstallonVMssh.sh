#!/bin/bash
SERVERS="servers.txt"
SSH_USER="fatih"
pkg="htop"

while read -r VM; do
    echo "----Installing $pkg on $VM----"

    ssh -tt "$SSH_USER@$VM" \
        "sudo apt update && sudo apt -y install $pkg"

done < "$SERVERS"

