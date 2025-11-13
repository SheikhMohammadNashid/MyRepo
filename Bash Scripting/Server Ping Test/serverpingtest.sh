#!/bin/bash
servers="google.com youtube.com facebook.com amazon.com wikipedia.org instagram.com x.com linkedin.com reddit.com netflix.com"

for s in $servers; do
    echo "--- Pinging $s ---"
    ping -c 3 $s
done
