Updated: 20211108

The Files found in this repository are for the F411CWDecoder, KeyBoard Encoder, & BlackPill SDR projects.

The the PDF file "CubeIDE_Programming_StepR2A.pdf" was created specifically for the CW decoder project;
However, if your interested in the MCUFriends code collection/project, or the KeyBoard Encoder project, these install steps would/will be essentially the same.

The Black Pill to TFT Display connections/wiring are the same for all projects.
However, there is a separate connection wiring diagram (MAX3421_BlackPillConnDiag.pdf) for the BlackPill to MAX3421 Mini Breakout board.
This 2nd Diagram overides any overlapping connections shown in the 1st (or base) Diagram. Additionally, see "BlackPillWirelessCWKeyBrdSchematic.pdf"  for a schematic view of the Keyboard encoder project. It can be used to further clarify how this project can be wired up.

***********************************************************************************

And finally the lower right segment of the display has a “Slow”/”Fast”touch Button.
In the “Slow” mode, tone samples are processed at 8ms intervals, and in the “Fast” mode processing is done every 4ms. Normally, for well sent code at <30wpm, the slow mode will yield better results. While for faster WPM rates, or irregular symbol timing, the “fast” mode can/will yield a more accurate parsing.

Other Touch Screen Displays:
The Decoder & Keyboard projects are designed for a “480 x 320” pixel display. While the SDR project uses a 240 x 320 display. All use the Arduino sheild form factor. However; within this group, vendors can use different touch pin pairs than whats been assigned in the default code.
The SDR & Decoder projects now have built-in screen cal code. This code should discover and set the parameters described below. And therefore should supercede the need for the following instructions. But are still here, as general information.
Note: The BT Keyboard project does NOT require the "touch" option. 
If your Display uses something other than PB7/PA6 & PA&/PB6, see/modify lines 43 &44 in the BtnSuprt.h file. They currently read:
const int XP=PB7, XM=PA6, YP=PA7, YM=PB6;
const int TS_LEFT=634,TS_RT=399,TS_TOP=492,TS_BOT=522;
To determine what pin pairs are in play on your touch screen, you can run the “STM32_TouchScreen_Calibr_native.cpp” found in the MCUFreindsDisplay project (also located in this GitHub repository). The basic use of this diagnostic tool is fairly self explanatory. But what may not be obvious, is this program/tool is capable of generating a more detailed report via the BlackPill’s USB serial connection. One way to see this report is to use the Adruino IDE’s serial tool.  The Status of the STM32CUBEIDE doesn’t matter (it can be open or closed). But you may need to disconnect the ST link (at least at the computer end). With the ARDUINO IDE running, connect your C style USB cable between your computer and the Black Pill. Use the (ARDUINO) IDE’s Tools/Port menu to select the correct port number your computer sees the Black Pill on. Once you have it selected, reset (restart) the black pill, and as soon as you hear the windows USB connected chime/melody, launch the ARDUINO’s Tools/Serial Monitor. The scan portion of the report should appear in the serial monitor within a few seconds. But if the Display shows “Broken Screen” (or “Press to Continue”) and the serial monitor is blank. Close the serial monitor. Reset the black pill, and try again.
Note, this same method of linking your black pill decoder to your computer can also be used when the decoder is running in one of its two Debug Modes.

Finally, if you prefer to construct this decoder using a PCB mother board, rather than the jumper method shown in the video, contact W8DU (via QRZ.com) for board & pricing.
Or you can order your own PCBs, from JLCPCB, using the ..._JLCPCBfiles_... .zip files, found in this respository.

