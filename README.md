# Python-SparkFun-RV8803-RTC
Python bindings for the RV8803 I2C interface originally written by SparkFun for Arduino.

I took the code from the [SparkFun_RV-8803 Arduino Library](https://github.com/sparkfun/SparkFun_RV-8803_Arduino_Library) and repurposed it for use with a raspberry pi via python bindings (just extending most of the existing API via ctypes). I used paulvha's [Two Wire](https://github.com/paulvha/twowire.git) which is very similar to Arduino's TwoWire, making it relatively easy to glue the Arduino API to Raspi's BCM2835 I2C interface.

The code isn't great at the moment so I'd appreciate merge requests to help clean it up. Some issues are:
 * Some hardcoded values (e.g. 0x32 bus ID and hardware SDA/SCL)
 * occasional segfaults due to untested edge cases
 * build chain / conversion to CircuitPython API
 * merge with the Arduino interface to minimize code repetition.

If it doesn't work, I recommend tweaking some settings in `SparkFun_RV8803.cpp` and rebuilding with the command

```gcc -shared -Wl,-soname,SparkFun_RV8803 -o SparkFun_RV8803.o -fPIC SparkFun_RV8803.cpp  -lstdc++  -ltwowire -lm -lm -lc -lgcc -lc -lbcm2835 -fpermissive && python3 SparkFun_RV8803.py```

You may also need to build the dependencies lbcm2835 and ltwowire, which are included in the repo. 
