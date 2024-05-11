#!/usr/bin/env bash

# kill already running polybar on refresh
killall -q polybar

# Launch bar1 and bar2
#echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
polybar | tee -a /tmp/polybar.log & disown
#polybar bar2 2>&1 | tee -a /tmp/polybar2.log & disown
