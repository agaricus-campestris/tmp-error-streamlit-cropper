#!/bin/bash

dateNow=$(date +%Hh%M:%S)
scanimage --device-name 'v4l:/dev/video0' --brightness 50 --format=png --mode=Color > ./SCANNER/"$dateNow".png
