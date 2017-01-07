import datetime 
import time   
import gy_521
import plotly
import numpy as np 
import plotly.plotly as py  
import plotly.tools as tls   
import plotly.graph_objs as go

# Get stream id from stream id list 
stream_ids = tls.get_credentials_file()['stream_ids']
stream_id = stream_ids[0]

# Make instance of stream id object 
stream_1 = go.Stream(
    token=stream_id,  # link stream id to 'token' key
    maxpoints=80      # keep a max of 80 pts on screen
)

stream_1 = dict(token=stream_id, maxpoints=60)

# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1         # (!) embed stream id, 1 per trace
)
data = go.Data([trace1])

# Add title to layout object
layout = go.Layout(title='Rotation status')

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot, open new tab
py.plot(fig, filename='gy-521')

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

# We then open a connection
s.open()
 
i = 0    # a counter
k = 5    # some shape parameter

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5) 

while True:
    [x, y] = gy_521.rotation_data()
        
    # Send data to plot
    s.write(dict(x=x, y=y))  
    
    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot
            
    # Plot with 100Hz frequency
    time.sleep(1) 

# Close the stream when done plotting
s.close() # Embed never-ending time series streaming plot
tls.embed('gy-521','12')
