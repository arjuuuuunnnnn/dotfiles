#!/bin/sh

INTERFACE="wlan0"

IP=$(hostname -I | awk '{print $1}')

# UPLOAD=$(vnstat -tr 1 | grep "$IP" | awk '{print $6 "KB/s";}')
# DOWNLOAD=$(vnstat -tr 1 | grep "$IP" | awk '{print $5 "KB/s";}')

# echo "$IP  %{F#6790EB}⬆%{F-} $UPLOAD %{F#E58501}⬇%{F-} $DOWNLOAD"

echo "$IP"
