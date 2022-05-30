import plotly.graph_objects as go
import numpy as np

from random_walk import RandomWalk

 # Make a random walk. 
rw = RandomWalk(50_000)
rw.fill_walk()

fig = go.Figure(data=go.Scatter(
    x=rw.x_values,
    y=rw.y_values,
    mode='markers',
    name='Random Walk',
    marker=dict(
        color=np.arange(50000),
        size=8,
        colorscale='Greens',
        showscale=True
    )
))

fig.show()