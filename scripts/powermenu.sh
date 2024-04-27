#!/usr/bin/env bash


chosen=$(printf "Power Off\nRestart\nLock" | rofi -dmenu -i -theme-str '@import "power.rasi"')

case "$chosen" in
	"Power Off") poweroff ;;
	"Reboot") reboot ;;
	"Lock") i3lock ;;
	*) exit 1 ;;
esac

