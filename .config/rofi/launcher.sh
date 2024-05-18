#!/bin/bash

## style-1     style-2     style-3     style-4     style-5
## style-6     style-7     style-8     style-9     style-10

dir="$HOME/.config/rofi"
theme='config'

## Run
rofi \
    -show drun \
    -theme ${dir}/${theme}.rasi
