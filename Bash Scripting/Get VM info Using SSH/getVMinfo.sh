#!/bin/bash
SERVERS="192.168.0.241"
SSH_USER="fatih"
for VM in $SERVERS; do
        echo"---Info for $VM---"
        CMD="uptime && free -h"
        ssh $SSH_USER@$VM "$CMD"

        echo "------------------"
done

