# Leopica
We're all made of stardust!

## Setup
### Satellite
+ Uncomment your IMU sensor board in `Multiwii/config.h`.
For example  with GY-521, I uncomment this line:
```
// #define GY_521
```
to
```
#define GY_521
```

+ Upload `Multiwii/Multiwii.ino` to your satellite arduino controller

### Ground station
+ Connect and upload `TelemetryTransmitter/TelemetryTransmitter.ino` to your Arduino controller.

+ Open `MultiwiiConf/application.windows<32|64>`, choose Arduino connected COM and press `START`.
