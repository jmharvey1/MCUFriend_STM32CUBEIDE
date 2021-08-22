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
And while running in decode mode, the lower right segment of the display has a “Slow”/”Fast”touch Button.
In the “Slow” mode, tone samples are processed at 8ms intervals, and in the “Fast” mode processing is done every 4ms. Normally for well sent code at <30wpm, the slow mode will yield better results. While for faster WPM rates, or irregular symbol timing, the “fast” mode can/will yield a more accurate parsing of symbols.
Finally, if you prefer to construct this decoder using a PCB mother board, rather than the jumper method shown in the video, contact W8DU (via QRZ.com) for board & pricing.   

