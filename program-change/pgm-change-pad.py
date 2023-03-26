import time
import picokeypad as keypad
# micropython program for pimoroni RGB keypad on raspberry pi pico
# TODO - send USB messages. Micropython support for USB on pico is not great at the moment so this project is parked,
#        while I try another project based on circuitputhon

# Behaviour
# Press A to enter Bank Select mode
# Press B to enter Patch Select mode
# if A and B are pressed at the same time, A wins.  If A is released before B, then B wins
# Numbers for currenty selected Bank or Patch is illuminated
# Press C to cycle throuh hundreds, tens and units
# C is lit Red for hundreds, Green for tens and Blue for units
# Press 3 number keys to enter bank or patch
# each press moves to next order of magnitude
# Switch modes (A or B) to discard any entered numbers
# press D to commit entered number

keypad.init()
keypad.clear()
keypad.set_brightness(1.0)
last_button_states = 0
orderOfMagnitude=2
mode=0
bankSelect=[0,0,0]
patchSelect=[0,0,0]
NUM_PADS = keypad.get_num_pads()
while True:
    # Has anything changed since previous loop?
    button_states = keypad.get_button_states()
    if last_button_states != button_states:
        last_button_states = button_states
        # is anything actually being pressed now?
        if button_states > 0:
            #What mode are we in? Bank select or patch select?    
            if (button_states >> 0x0A) & 0x01:
                mode=0
                orderOfMagnitude=2
            elif (button_states >> 0x0B) & 0x01:
                mode=1
                orderOfMagnitude=2
            elif (button_states >> 0x0C) & 0x01:
                print('C {:d}'.format(orderOfMagnitude))
                orderOfMagnitude = orderOfMagnitude -1
                if orderOfMagnitude == -1:
                    orderOfMagnitude=2
                print('C {:d}'.format(orderOfMagnitude))
            elif (button_states >> 0x0D) & 0x01:
                print('enter {:d}{:d}{:d} - {:d}{:d}{:d}'.format(bankSelect[2],bankSelect[1],bankSelect[0],patchSelect[2],patchSelect[1],patchSelect[0]))
            else:
                for i in range(0,9):
                    if (button_states >> i) & 0x01:
                        if mode ==0:
                            bankSelect[orderOfMagnitude]=i
                        else:
                            patchSelect[orderOfMagnitude]=i
                orderOfMagnitude = orderOfMagnitude -1
                if orderOfMagnitude == -1:
                    orderOfMagnitude=2
                    
    #light up current state
    keypad.clear()
    if mode == 0:
        keypad.illuminate(0xA,0,0x20,0)
        keypad.illuminate(0xB,0,0,0)
        keypad.illuminate(bankSelect[orderOfMagnitude],0,0,0x20)
        #print('mode 0 oom {:d} value {:d}'.format(orderOfMagnitude,bankSelect[orderOfMagnitude]))
    else:
        keypad.illuminate(0xA,0,0,0)
        keypad.illuminate(0xB,0,0x20,0)
        keypad.illuminate(patchSelect[orderOfMagnitude],0,0,0x20)
        #print('mode 1 oom {:d} value {:d}'.format(orderOfMagnitude,patchSelect[orderOfMagnitude]))
    if orderOfMagnitude==2:
        keypad.illuminate(0xC,0x20,0,0)
    elif orderOfMagnitude==1:
        keypad.illuminate(0xC,0,0x20,0)
    elif orderOfMagnitude==0:
        keypad.illuminate(0xC,0,0,0x20)
    else:
        keypad.illuminate(0xD,0x20,0,0)
    
        
    keypad.update()
                                          
    time.sleep(0.1)