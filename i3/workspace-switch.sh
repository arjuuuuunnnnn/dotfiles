#!/bin/bash

current_workspace=$(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true) | .num')

if [[ "$1" == "up" ]]; then
  new_workspace=$((current_workspace + 1))
elif [[ "$1" == "down" ]]; then
  new_workspace=$((current_workspace - 1))
elif [[ "$1" == "left" ]]; then
  new_workspace=$((current_workspace - 1))
elif [[ "$1" == "right" ]]; then
  new_workspace=$((current_workspace + 1))
else
  exit 1
fi

if [[ "$new_workspace" -lt 1 ]]; then
  new_workspace=$(($(i3-msg -t get_workspaces | jq -r '.[].num' | wc -l)))
elif [[ "$new_workspace" -gt $(i3-msg -t get_workspaces | jq -r '.[].num' | wc -l) ]]; then
  new_workspace=1
fi

i3-msg workspace "$new_workspace"
