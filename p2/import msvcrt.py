import msvcrt
import sys
while True:
    pressedKey = msvcrt.getch()
    if pressedKey == b'q':    
       print("Q was pressed")
    elif pressedKey == 'x':    
       sys.exit()
    else:
       print( "Key Pressed:" + str(pressedKey))