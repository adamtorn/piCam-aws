#!/bin/bash

filename=$1
username=$2

fswebcam -r 640x480 -S 20 --flip h --jpeg 95 --shadow --title "Spot Security" --subtitle "Home of $username" --save $filename.jpg -q --fps 20 -F 600 -l 1