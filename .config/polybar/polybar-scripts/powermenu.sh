#!/usr/bin/env bash


chosen=$(printf " Power Off\n Reboot\n Lock" | rofi -dmenu -i -theme-str '@import "~/.config/rofi/power.rasi"')

case "$chosen" in
	" Power Off") poweroff ;;
	" Reboot") reboot ;;
	" Lock") ~/.config/i3lock/i3lock.sh ;;
	*) exit 1 ;;
esac

