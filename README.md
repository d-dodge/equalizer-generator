# equalizer-generator
Converts acoustic measurements to graphic equalizer curves for closed-loop sound system calibration

This program is designed as an interface to connect Room EQ Wizard (REW) and EqualizerAPO.

# Quick Start Guide

1. Take a measurement in REW. Apply smoothing. I've had best results with 1/12 smoothing (Graph > 1/12 Smoothing). Note the average db level on the graph that you would like all the peaks and dips to be corrected towards. This will be the Target Level. This value is subjective and will vary from setup to setup. The goal is to bring the peaks and dips up or down to whatever the average level of the reading is, thus minimizing overcorrection. Experiment and see what works best for you.

2. Export the REW measurement by going to File > Export Measurement as Text. The default options should be ok. Save the text file to a convient location.

3. Run equalizer-generator.py, giving it the arguments of the Target Level, the path to the REW text file, and the path to where you would like the output saved.

4. Open the output text file. Inside will be a GraphicEQ config line that can be copied directly into EqualizerAPO's configuration file or the Configurator GUI. Happy EQing! 