# MCUFriend_STM32CUBEIDE
MCUFriend_Kvb Library files compatible with the STM32CUBEIDE
THe files contained here are those that were reviewed/described in YouTube Video https://youtu.be/tUJbHZI50fw
The original upload consists of the MCUFriend_KBV and the TouchScreen files plus their support files
Also included are 4 "demo" programs that should work with the f411 Black Pill and a MCFriend Compatible 3.5 TFT touch screen display.
Any other combination of hardware, will likely require modification to one or more files contained here.
These files are believed to be "open source" files, and are not to be used beyond what the their oringinal authors intended.
20210426
Added blackpill CWdecoder project Zip file. 
Wiring is essentially the same as the Blue Pill Decoder, with the following exceptions: 
1. LCD_D3 is connected to PB0. Not PA3
2. The Key interrupt jumper is now on PB12 to PB13
3. Mic Bd output is connected to PB1
4. LED Tuning input pin is connected to PB15

The STMCUBEIDE can be downloaded at this site:
		https://www.st.com/en/development-tools/stm32cubeide.html