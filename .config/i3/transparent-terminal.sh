##!/bin/bash

## Start the compositing manager
#xcompmgr &

## Get the window ID of the active GNOME Terminal window
##window_id=$(xprop -root _NET_ACTIVE_WINDOW | awk '{print $5}')
#term_window_id=$(wmctrl -l | grep "Gnome-terminal" | awk '{print $1}')


## Set the opacity of the window
## xprop -id "$window_id" -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY 0x80000000
#wmctrl -r "$term_window_id" -b add,opacity=0x80000000

## Repeat the opacity setting every 2 seconds for new terminal windows
#while true; do
#    window_id=$(xprop -root _NET_ACTIVE_WINDOW | awk '{print $5}')
#    xprop -id "$window_id" -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY 0x80000000
#    sleep 2
#done

#!/bin/bash

# Start the compositing manager (picom)
picom --config ~/.config/picom/picom.conf &

# Get the window ID of the active GNOME Terminal window
term_window_id=$(wmctrl -l | grep "Gnome-terminal" | awk '{print $1}')

# Set the opacity of the window
wmctrl -r "$term_window_id" -b add,opacity=0x80000000

# Repeat the opacity setting every 2 seconds for new terminal windows
while true; do
    term_window_id=$(wmctrl -l | grep "Gnome-terminal" | awk '{print $1}')
    wmctrl -r "$term_window_id" -b add,opacity=0x80000000
    sleep 2
done
