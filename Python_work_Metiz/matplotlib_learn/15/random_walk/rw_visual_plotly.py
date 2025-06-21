from plotly.graph_objs import Scatter, Layout
from plotly import offline

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
steps = list(range(len(rw.x_values)))
x_axis_config = {'title': 'x rw', 'dtick': 1}
y_axis_config = {'title': 'y rw', 'dtick': 1}
data = [Scatter(x = rw.x_values, y= rw.y_values, mode = 'markers',marker=dict(size=3, color=steps, colorscale='Viridis', showscale=True))]
my_layout = Layout(title='Result of random walk.',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data,'layout': my_layout}, filename = 'rw.html')