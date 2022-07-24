#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "lauching main hub: PWD= $(pwd),  script dir = ${SCRIPT_DIR}" >> /home/patch/tmp/main-hub.log
one-loop.sh
