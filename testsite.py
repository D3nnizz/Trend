import plotly.graph_objects as go
import numpy as np
import plotly.io as pio

# Data
t = np.linspace(0, 10, 1000)
x, y = t, np.cos(t)

# Scatter plot
data = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker={
        'color': y,
        'colorscale': [[0, 'red'], [0.5, 'yellow'], [1, 'green']],
        'size': 10,
        'colorbar': dict(
            title="Y value",
            x=-0.06,
            tickvals=[],
            showticklabels=False
        )
    }
)

# Layout
layout = dict(
    plot_bgcolor='white',
    margin=dict(t=0, b=0, r=0, l=0, pad=0),
    xaxis=dict(showgrid=False, zeroline=False, mirror=True, linecolor='gray'),
    yaxis=dict(
        showgrid=False, zeroline=False, mirror=True, linecolor='gray',
        side='right'
    )
)

# Create figure
fig = go.Figure(data=data, layout=layout)

# Export to HTML file
pio.write_html(fig, file='scatter_plot.html', auto_open=True)
