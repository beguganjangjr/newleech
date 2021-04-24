#!/bin/bash

wget -q https://github.com/xinxin8816/heroku-aria2c-21vianet/raw/master/rclone.zip
unzip -qj rclone.zip -d /usr/bin
rm -rf rclone.zip
chmod 777 /usr/bin/rclone

# Install aria2c static binary
wget -q https://github.com/P3TERX/aria2-builder/releases/download/1.35.0_2020.09.04/aria2-1.35.0-static-linux-amd64.tar.gz
tar xf aria2-1.35.0-static-linux-amd64.tar.gz -C /usr/local/bin
rm -rf aria2-1.35.0-static-linux-amd64.tar.gz

# Create download folder
#mkdir -p downloads

# DHT
wget -q https://github.com/P3TERX/aria2.conf/raw/master/dht.dat
wget -q https://github.com/P3TERX/aria2.conf/raw/master/dht6.dat

wget -q https://kmk.kmk.workers.dev/accounts.zip
unzip -q accounts.zip
rm -rf accounts.zip
