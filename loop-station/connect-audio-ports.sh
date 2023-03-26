#!/bin/bash
jack_connect system:capture_1 sooperlooper:common_in_1
jack_connect system:capture_2 sooperlooper:common_in_2
jack_connect sooperlooper:common_out_1 system:playback_1
jack_connect sooperlooper:common_out_2 system:playback_2
jack_connect system:capture_1 system:playback_1
jack_connect system:capture_2 system:playback_2
jack_lsp -c >> /home/patch/tmp/loopstation.log
