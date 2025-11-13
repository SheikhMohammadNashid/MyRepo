#!/bin/bash
servers="google.com youtube.com facebook.com amazon.com wikipedia.org instagram.com x.com linkedin.com reddit.com netflix.com"

for s in $servers; do
    echo "--- Pinging $s ---"
    if ping -c 1 $s > /dev/null 2>&1; then
        echo "OK"
    else
        echo "FAIL"
    fi
    echo ""
done

