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
    token=stream_id  # link stream id to 'token' key
)

stream_1 = dict(token=stream_id)

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

# Send fig to Plotly, initialize streaming plot
py.plot(fig, filename='gy-521', auto_open=False)

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

# We then open a connection
s.open()
 
while True:
    # Current time on x-axis 
    x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    # Accel's y on y-axis
    y = gy_521.accel_rotation_data()[1]
        
    # Send data to plot
    s.write(dict(x=x, y=y))  
    
    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot
            
    time.sleep(0.1) 

# Close the stream when done plotting
s.close() 
