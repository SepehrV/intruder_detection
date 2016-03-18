#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 640x360 --no-banner current.jpg
