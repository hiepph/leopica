import datetime 
import time   
import logging
import Adafruit_DHT as dht
import plotly.plotly as py  
import plotly.tools as tls
import plotly.graph_objs as go

logging.basicConfig(format='[%(asctime)s] %(levelname)s ($%(name)s) - %(message)s',
                    level=logging.DEBUG)

# Get stream id list 
# Only get 6th, 7th token for DHT
stream_ids = tls.get_credentials_file()['stream_ids'][5:]

# Specify individual name value to display
names = [
    'humidity',
    'temperature'
]

# Initialize trace of streaming plot and corresponding data
data = list(map(lambda stream_id: go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    name=names.pop(0),
    stream=go.Stream(token=stream_id)
), stream_ids))

# Add title to layout object
layout = go.Layout(
    title='DHT22: Humidity + Temperature'
)

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot
py.plot(fig, filename='dht-22', auto_open=False)

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
streams = list(map(lambda stream_id: py.Stream(stream_id), stream_ids))

# We then open a connection
for stream in streams:
    stream.open()
    
logging.info("Start %d streams!", len(streams))
 
while True:
    # Current time on x-axis 
    x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    
    # Humidity + Temperature on y-axes
    # y = [humidity, temperature]
    # DHT22's data pin on GPIO 4
    y = dht.read_retry(dht.DHT22, 4)

    # Send data to plot
    for (idx, stream) in enumerate(streams):
        stream.write(dict(x=x, y=y[idx]))
    
    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot
           
    # 0.1s update frequency
    time.sleep(0.1) 

# Close the stream when done plotting
for stream in streams:
    stream.close()
