#!/bin/sh

# Terminate already running bar instances
killall -q i3bar
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar, using default config location ~./config/polybar/config
polybar main &

echo "Bars launched..."
