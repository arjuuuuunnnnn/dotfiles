#!/bin/sh

INTERFACE="wlan0"

IP=$(hostname -I | awk '{print $1}')

echo "$IP"

