#!/bin/bash
# Save this as ~/scripts/polybar-ip.sh

# Function to get local IP
get_local_ip() {
    # Try to get IP from common interface names
    for interface in eth0 wlan0 enp0s3 wlp2s0; do
        ip=$(ip addr show $interface 2>/dev/null | grep "inet\b" | awk '{print $2}' | cut -d/ -f1 | head -n1)
        if [ ! -z "$ip" ]; then
            echo "$ip"
            return
        fi
    done
    echo " 127.0.0.1"
}

# Function to get public IP
get_public_ip() {
    public_ip=$(curl -s --max-time 2 ifconfig.me)
    if [ $? -eq 0 ] && [ ! -z "$public_ip" ]; then
        echo "$public_ip"
    else
        echo "No Public IP"
    fi
}

# Function to get VPN IP (if connected)
get_vpn_ip() {
    vpn_ip=$(ip addr show tun0 2>/dev/null | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
    if [ ! -z "$vpn_ip" ]; then
        echo "$vpn_ip"
    else
        echo "No VPN"
    fi
}

# Main script with argument handling
case "$1" in
    "local")
        get_local_ip
        ;;
    "public")
        get_public_ip
        ;;
    "vpn")
        get_vpn_ip
        ;;
    "all")
        echo "L:$(get_local_ip) P:$(get_public_ip) V:$(get_vpn_ip)"
        ;;
    *)
        get_local_ip  # default to local IP if no argument provided
        ;;
esac
