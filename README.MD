# Leopica

The name of the satellite joined in Vietnam CANSAT 2016 (Satellite in a can).

This is the source code of it.

## Requirement

### Hardware

+ Raspberry Pi 3 (recommended), 2 is also available

+ Raspberry Pi's camera module. I recommend version 2, because it is equipped with Sony IMX219 8-megapixel sensor (compared to the 5-megapixel OmniVision OV5647 sensor of the first version)

### Software

* Python3 (>= `3.4` recommended)

* `Redis` worker

* Some python libraries: `pydrive`, `plotly`, `rq`, `rq-dashboard`

All can be installed via `pip install <package>`


## Set things up and running

### Hardware config

+ Enable the camera:

```
sudo raspi-config
```

In the menu select **Enable Camera**.

+ Connect to 3G:

A nice tutorial by using Sakis's 3G connect script has been introduced here: https://shkspr.mobi/blog/2012/07/3g-internet-on-raspberry-pi-success/

### Redis worker for uploading image

* Activate worker:

```
rq worker
```

It will queue upload image command and continually executing it.

+ A nice dashboard admin:

```
rq-dashboard
```

Open browser and check process following link: `http://localhost:9181`

### Sensor Plotting

For setup, use Python interactive shell for quickly generating a `~/.plotly/.credentials` file:

```
>>> import plotly
>>> plotly.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
```

Go to https://plot.ly/settings/api to achieve your api key and stream id, and fill up to credentials file, a complete file will look like this:

    {
        "api_key": "abcdef123456",
        "username": "einstein",
        "stream_ids": [
            "e=mc2"
        ],
        "proxy_username": "",
        "proxy_password": ""
    }

More info you can check here: https://plot.ly/python/getting-started/
