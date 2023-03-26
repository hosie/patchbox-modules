#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "lauching loop station: PWD= $(pwd),  script dir = ${SCRIPT_DIR}" >> /home/patch/tmp/loopstation.log
one-loop.sh
