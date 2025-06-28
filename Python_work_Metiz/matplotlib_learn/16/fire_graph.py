import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/fire_nrt_M-C61_627972.json'
with open(filename) as f:
    all_fire_data = json.load(f)

lons, lats, frps = [], [], []
for fire_dict in all_fire_data:
    frp = fire_dict['frp']
    if frp is None or frp <= 10:
        continue
    lons.append(fire_dict['longitude'])
    lats.append(fire_dict['latitude'])
    frps.append(frp)


data = [{
        'type': 'scattergeo',
        'lon': lons[:10000],
        'lat': lats[:10000],
        'marker': {
                'size': [min(25, max(2, frp / 10)) for frp in frps[:10000]],
                'color': frps[:10000],
                'colorscale': 'Reds',
                'cmin': 0,
                'cmax': 100,
                'colorbar': {'title': 'Fire Radiative Power'},
                },
    }]
my_layout = Layout(title = 'Global Fire Map')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'global_fire_map.html')