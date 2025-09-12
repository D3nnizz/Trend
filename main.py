import plotly.graph_objects as go
import numpy as np

t = np.linspace(0, 10, 1000)
x, y = t, np.cos(t)

data = go.Scatter(
    x=x, 
    y=y, 
    mode='markers',
    marker={
        'color': y,  # vertical coloring
        'colorscale': [[0, 'red'], [0.5, 'yellow'], [1, 'green']],  # red-yellow-green
        'size': 10,
        'colorbar': dict(
            title="Y value",
            x=-0.06,         # move colorbar to left
            tickvals=[],     # hide ticks
            showticklabels=False
        )
    }
)

layout = dict(
    plot_bgcolor='white',
    margin=dict(t=0, b=0, r=0, l=0, pad=0),
    xaxis=dict(showgrid=False, zeroline=False, mirror=True, linecolor='gray'),
    yaxis=dict(
        showgrid=False, zeroline=False, mirror=True, linecolor='gray',
        side='right'      # move y-axis ticks to the right
    )
)

fig = go.Figure(data=data, layout=layout)
fig.show()
