#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

pkill sooperlooper
sleep 3
echo "about to start sooperlooper four loops" >> /home/patch/tmp/main-hub.log
sooperlooper -m ${SCRIPT_DIR}/four-loops.slb -L ${SCRIPT_DIR}/four-loops.slsess >> /home/patch/tmp/main-hub.log 2>&1 &
sleep 3
${SCRIPT_DIR}/connect-audio-ports.sh
${SCRIPT_DIR}/connect-audio-ports.sh
