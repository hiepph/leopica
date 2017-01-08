import datetime 
import time   
import gy_521
import plotly.plotly as py  
import plotly.tools as tls
import plotly.graph_objs as go

# Get stream id list 
stream_ids = tls.get_credentials_file()['stream_ids']
stream_accel_x_id = stream_ids[0]
stream_accel_y_id = stream_ids[1]

# Make instance of stream id object 
stream_accel_x = go.Stream(token=stream_accel_x_id)
stream_accel_y = go.Stream(token=stream_accel_y_id)

# Initialize trace of streaming plot by embedding the unique stream_id
trace_accel_x = go.Scatter(
    x=[],
    y=[],
    mode='lines',
    name='accel_x',
    stream=stream_accel_x
)
trace_accel_y = go.Scatter(
    x=[],
    y=[],
    mode='lines',
    name='accel_y',
    stream=stream_accel_y
)
data = [trace_accel_x, trace_accel_y]

# Add title to layout object
layout = go.Layout(
    title='Accelerometer'
)

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot
py.plot(fig, filename='gy-521', auto_open=False)

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s_accel_x = py.Stream(stream_accel_x_id)
s_accel_y = py.Stream(stream_accel_y_id)

# We then open a connection
s_accel_x.open()
s_accel_y.open()
print("INFO: Start streaming!")
 
while True:
    # Current time on x-axis 
    x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    # Accel's x, y on y-axis
    y_x = gy_521.accel_rotation_data()[0]
    y_y = gy_521.accel_rotation_data()[1]

    # Send data to plot
    s_accel_x.write(dict(x=x, y=y_x))
    s_accel_y.write(dict(x=x, y=y_y))
    
    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot
           
    # 0.1s update frequency
    time.sleep(0.1) 

# Close the stream when done plotting
s.close() 
