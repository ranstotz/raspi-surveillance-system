#!/bin/bash

# Driver script.

echo -e "\n==========Starting ${0##*/} - Raspberry Pi streaming. ==========\n"
python src/stream_video.py
echo -e "========== End of ${0##*/} script ==========\n"
