# Leopica

**WIP**

## Requirement

### Hardware

+ Raspberry Pi 3 (recommended), 2 is also available

+ Raspberry Pi's camera module. I recommend version 2, because it is equipped with Sony IMX219 8-megapixel sensor (compared to the 5-megapixel OmniVision OV5647 sensor of the first version)

### Software

* Python3 (>= `3.4` recommended)

* And some python libraries: `pydrive`, `pydrive`

All can be installed via `pip install <package>`

## Set things up and running

### Hardware config

+ Enable the camera:

```
sudo raspi-config
```

In the menu select **Enable Camera**.

### Launch

```
./launch.sh
```

A browser will pop-up and ask for authentication of Google Drive, just filling up and you're good to go.
