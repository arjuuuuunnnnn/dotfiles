#!/bin/bash


xcompmgr &

term_window_id=$(wmctrl -l | grep "Gnome-terminal" | awk '{print $1}')


wmctrl -r "$term_window_id" -b add,opacity=0x80000000


while true; do
    window_id=$(xprop -root _NET_ACTIVE_WINDOW | awk '{print $5}')
    xprop -id "$window_id" -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY 0x80000000
    sleep 2
done

