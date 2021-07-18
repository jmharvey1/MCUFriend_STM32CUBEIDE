The Files found in this folder currently are specific to the F411CWDecoder project.
If your interested the MCUFriends collection/project the install steps would/will be essentially the same.
And the Black Pill to Display connections/wiring is also the same.

Operational Notes related to the Black Pill CW decoder only:

There is a “setup” mode that can be invoked with a “long press” of the blue “Clear” button.

In the setup mode, the user can adjust & save the following parameters:

1. Bias (+/-) ; value to subtract from ADC sample to remove the microphone's DC offset
2. MSQL(+/-); Squelch value to use when tone detector is operating in MAN SQLCH mode 
3. TSF(+/-);  “Tone Scale Factor”; Not Functional in the current version.  
4. NSF(+/-); “Noise Scale Factor”; speaker dependent; Adjust for best tone detection.
5. LED(+/-); Set maximum LED brightness.
6. SMPL(+/-); Sample Frequency; experimental; Manually change the sample value used to calculate the Goertzel tone detection coefficients.
7. Squelch Mode (NOISE SQLCH / MAN SQLCH); no explanation needed
8. Factory Vals; return decoder to sketch default value
9. Debug Mode (OFF / Plot / Decode); When not OFF, use Arduino IDE plot /serial monitor tools
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
4. Bug3; Similar to “Bug2” but uses different timing percentages to recover/decode the letter