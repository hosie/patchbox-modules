#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

pkill sooperlooper
sleep 3
echo "about to start sooperlooper five loops" >> /home/patch/tmp/loopstation.log
sooperlooper -m ${SCRIPT_DIR}/five-loops.slb -L ${SCRIPT_DIR}/five-loops.slsess >> /home/patch/tmp/sooperlooper.log 2>&1 &
sleep 3
${SCRIPT_DIR}/connect-audio-ports.sh
${SCRIPT_DIR}/connect-audio-ports.sh
