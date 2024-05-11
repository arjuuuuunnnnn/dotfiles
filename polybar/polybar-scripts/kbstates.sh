#!/bin/bash

# Define the symbols or text to display for each lock state
caps_on="🄲"
caps_off=""
num_on="🅝"
num_off=""
scroll_on="🄻"
scroll_off=""

# Check the lock states
caps_state=$(xset q | grep 'Caps Lock' | awk '{print $4}')
num_state=$(xset q | grep 'Num Lock' | awk '{print $5}')
scroll_state=$(xset q | grep 'Scroll Lock' | awk '{print $5}')

# Build the output string
output=""

if [ "$caps_state" = "on" ]; then
    output+="$caps_on"
else
    output+="$caps_off"
fi

if [ "$num_state" = "on" ]; then
    output+=" $num_on"
else
    output+=" $num_off"
fi

if [ "$scroll_state" = "on" ]; then
    output+=" $scroll_on"
else
    output+=" $scroll_off"
fi

# Output the lock states
echo "$output"
