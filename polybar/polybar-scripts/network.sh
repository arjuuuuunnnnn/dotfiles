#!/bin/bash

# Get the list of available connections
connections=$(nmcli -t -f NAME connection show)

# Check if internet is connected
if nmcli -t -f STATE general show | grep -q "connected"; then
    connected=$(nmcli -t -f NAME connection show --active)
    notify-send "Connected to: $connected"
    options="Disconnect\n$connections"
else
    options="Connect\n$connections"
fi

# Show Rofi menu with options
selected=$(echo -e "$options" | rofi -dmenu -p "Network" -i)

# Handle user selection
if [[ $selected == "Connect" ]]; then
    # Connect to a network
    nmcli device wifi rescan
    selected_connection=$(echo -e "$connections" | rofi -dmenu -p "Connect to" -i)
    nmcli device wifi connect "$selected_connection"
    notify-send "Connecting to: $selected_connection"
elif [[ $selected == "Disconnect" ]]; then
    # Disconnect from the current network
    current=$(nmcli -t -f NAME connection show --active)
    nmcli connection down "$current"
    notify-send "Disconnected from: $current"
elif [[ ! -z $selected ]]; then
    # Connect to the selected network
    nmcli device wifi rescan
    nmcli device wifi connect "$selected"
    notify-send "Connecting to: $selected"
fi

