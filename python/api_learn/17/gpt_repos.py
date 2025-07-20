import requests

from plotly.graph_objs import Bar
from plotly import offline



url = 'https://api.github.com/search/repositories?q=chatgpt+in:name,description&sort=stars&order=desc&per_page=10'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get (url, headers = headers)
response_dict = r.json()
repo_dicts = response_dict['items']
name_urls, stars = [], []
for repo_dict in repo_dicts:
    url = repo_dict['html_url']
    name = repo_dict['name']
    name_url = f"<a href='{url}'>{name}</a>"
    stars.append(repo_dict['stargazers_count'])
    name_urls.append(name_url)

data = [{
    'type': 'bar',
    'x': name_urls,
    'y': stars,
}]

my_layout = {
    'title': {'text': 'Most starred gpt projects on GitHub.', 'font':{'size': 26}},
    'xaxis': {
        'title':{'text': 'Repository', 'font':{'size': 26}},
        'tickfont':{'size': 14}},
    'yaxis': {
        'title': {'text': 'Stars', 'font':{'size': 26}},
        'tickfont':{'size':14}},

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'gpt_r.html')


