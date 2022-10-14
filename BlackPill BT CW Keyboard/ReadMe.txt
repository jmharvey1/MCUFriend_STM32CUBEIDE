BlackPillWirelessCWKeyBrd_JLCPCB_2022-05-06.zip may be used to submit an order to JLCPCB for the motherboard, to host the Blackpill, display, and other components, used in this project

Use "BlackPill_BT_CWKeyboard_20220905.bin" and STM's STM32CubeProgrammer to flash the Keyboard to the BlackPill's MPU.
Alternatively you can compile the source code using files found in "BlackPill_BT_CWKeyboard_20220905.zip" and STM's STM32CubeIde (ver 1.9.0)

Bluetooh KeyBoard user notes

***********************************************************************************
KeyBoard Encoder Notes:
Special Keys & their functions:
Keys that send special Morse Characters
1. “=”   <BT>
2. “+”	<KN>
3. ”>”	<AR>
4. ”<”	<AS>
5. ”%”	<SK>
6. All other unassigned keys (i.e. “{“, “]”,…) send 6 dits, CW error code

Special Functions:
1. cntrl+T	Generates continuous key down state. Press “cntrl+T” again (or another key) to stop.
2. “Enter”	One button press to send your preloaded CallSign.
3. “delete” Back space, to delete unsent buffered code.
4. Right Arrow		Alternate action; Allows text to be typed, and not sent. Press again, and normal sending resumes. (In hold mode, lower left box is yellow)
5. Left Arrow		Store text (When active, lower left box is White). Up to 20 characters (no spaces) can be stored to be sent later. (Space bar, auto exit F1 store mode, or press F1 again to stop store) 
6. Lshift+Enter” Send "Left Arrow" stored text plus Your call sign.
7. Cntrl+Enter” Send "Left Arrow" stored text.
8. "Esc"   Abort outgoing text 	
10. cntrl+S User params/settings; i.e., Default WPM. Call Sign, F2 memory
11. F2 Send contents stored in "F2" memory (See "10.")  