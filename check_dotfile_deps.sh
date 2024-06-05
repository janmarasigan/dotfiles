#!/bin/bash

# Check list of fonts used
echo -e "\nInstall or replace the fonts specified in the files below:"
grep -nH "^font" .config/i3/config .config/polybar/config.ini .config/kitty/kitty.conf
