The Files found in this folder currently are specific to the F411CWDecoder project.
If your interested in the MCUFriends code collection/project, the install steps would/will be essentially the same.
And the Black Pill to Display connections/wiring are also the same as used in the decoder.

The Files found in this folder currently are specific to the F411CWDecoder project.
If your interested in the MCUFriends code collection/project, the install steps would/will be essentially the same.
And the Black Pill to Display connections/wiring are also the same as used in the decoder.

The following operational notes are related to the Black Pill CW decoder only:

There is a “setup” mode that can be invoked with a “long press” of the blue “Clear” button.

In the setup mode, the user can adjust, & save, the following parameters:

1. Bias (+/-) ; value to subtract from ADC sample to remove the microphone's DC offset
2. MSQL(+/-); Squelch value to use when tone detector is operating in MAN SQLCH mode 
3. TSF(+/-);  “Tone Scale Factor”; Not Functional in the current version.  
4. NSF(+/-); “Noise Scale Factor”; speaker dependent; Adjust for best tone detection.
5. LED(+/-); Sets LED’s maximum brightness.
6. Freq(+/-); Tone detect Frequency; Manually change the tone detect center frequency; Use only when in the "FREQ LOCKED" Tone mode.
7. Squelch Mode (NOISE SQLCH / MAN SQLCH); no explanation needed
8. Factory Vals; return decoder to sketch’s default values.
9. Debug Mode (OFF / Plot / Decode); When not OFF, use the Arduino IDE plot /serial monitor tools, via USB serial connection.
10. Tone mode (AUTO Tune / FREQ LOCKED)
The setup screen has two additional buttons:
1. Exit (leave the Setup mode; return to Decode mode)
2. Save (Store the current setting to Flash memory)
Aug 31 2021:
On the bottom row of buttons, there is a new orange button (I'm calling it the program button, or "mode" button, and its default state is "CW". It cycles through 3 other values (FFT, Scope, & LED). This represents the three other programs that can/will run when the Yellow "Exit" button is pressed. They perform no useful task, but demos with just software changes, how differently the same collection of hardware can behave. When tired of watching one of the alternate views, touch the display. It will revert back to the setup screen.

When the Decoder is running in decode mode, the lower left segment of the display is touch sensitive
and will display one of three attributes:
1. current Words per Minute / Dot to Dash ratio
2. current Average Dot / Dash / Space interval (milliseconds)
3. current tone filter center frequency (hertz)
When the Decoder is running in decode mode, the Green button supports 4 modes
1. Norm; “Normal”; should work for 90% of the messages decoded
2. Bug1; Use with senders that exaggerate the spacing between dashes in the same letter
3. Bug2; Same as “Bug1” but using a different strategy to recover/decode the letter
4. Bug3; Similar to “Bug2” but uses different timing percentages to recover/decode a character.
And finally the lower right segment of the display has a “Slow”/”Fast”touch Button.
In the “Slow” mode, tone samples are processed at 8ms intervals, and in the “Fast” mode processing is done every 4ms. Normally, for well sent code at <30wpm, the slow mode will yield better results. While for faster WPM rates, or irregular symbol timing, the “fast” mode can/will yield a more accurate parsing.

Other Touch Screen Displays:
Realistically this project is designed for a “480 x 320” pixel display. However; within this group, vendors can use different touch pin pairs than whats been assigned in the default code.
If your Display uses something other than PB7/PA6 & PA&/PB6, see/modify lines 43 &44 in the BtnSuprt.h file. They currently read:
const int XP=PB7, XM=PA6, YP=PA7, YM=PB6;
const int TS_LEFT=634,TS_RT=399,TS_TOP=492,TS_BOT=522;
To determine what pin pairs are in play on your touch screen, you can run the “STM32_TouchScreen_Calibr_native.cpp” found in the MCUFreindsDisplay project (also located in this GitHub repository). The basic use of this diagnostic tool is fairly self explanatory. But what may not be obvious, is this program/tool is capable of generating a more detailed report via the BlackPill’s USB serial connection. One way to see this report is to use the Adruino IDE’s serial tool.  The Status of the STM32CUBEIDE doesn’t matter (it can be open or closed). But you may need to disconnect the ST link (at least at the computer end). With the ARDUINO IDE running, connect your C style USB cable between your computer and the Black Pill. Use the (ARDUINO) IDE’s Tools/Port menu to select the correct port number your computer sees the Black Pill on. Once you have it selected, reset (restart) the black pill, and as soon as you hear the windows USB connected chime/melody, launch the ARDUINO’s Tools/Serial Monitor. The scan portion of the report should appear in the serial monitor within a few seconds. But if the Display shows “Broken Screen” (or “Press to Continue”) and the serial monitor is blank. Close the serial monitor. Reset the black pill, and try again.
Note, this same method of linking your black pill decoder to your computer can also be used when the decoder is running in one of its two Debug Modes.

Finally, if you prefer to construct this decoder using a PCB mother board, rather than the jumper method shown in the video, contact W8DU (via QRZ.com) for board & pricing.


