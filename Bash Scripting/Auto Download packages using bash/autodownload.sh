#!/bin/bash
auto="autoinstallpackages.txt"
while read -r U; do
echo "installing $U"
sudo $U
done < "$auto"
