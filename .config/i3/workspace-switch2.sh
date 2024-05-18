#!/bin/bash

# Get the current workspace
current_ws=$(i3-msg -t get_workspaces | jq -r '.[] | select(.focused) | .num')

# Determine the direction of the gesture
case "$1" in
    "3" )
        # 3-finger swipe left
        new_ws=$((current_ws - 1))
        ;;
    "4" )
        # 3-finger swipe right
        new_ws=$((current_ws + 1))
        ;;
    * )
        exit 1
        ;;
esac

# Switch to the new workspace
i3-msg workspace $new_ws
