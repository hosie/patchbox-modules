#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

pkill sooperlooper
sleep 3
echo "starting sooperlooper" >> /home/patch/tmp/loopstation.log
sooperlooper -m ${SCRIPT_DIR}/one-loop.slb -L ${SCRIPT_DIR}/one-loop.slsess >> /home/patch/tmp/sooperlooper.log 2>&1 &
sleep 3
${SCRIPT_DIR}/connect-audio-ports.sh
${SCRIPT_DIR}/connect-audio-ports.sh
