import requests

from plotly.graph_objs import Bar
from plotly import offline

#Создание вызова API и сохранение ответа.
url= 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
status_code = r.status_code


# Сохранение ответа API в переменной.
response_data = r.json()
# Анализ информации о репозиториях.
repo_dicts = response_data['items']

repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    #for key in sorted(repo_dict.keys()):
    #    print(key)
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Построение визуализации.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': { 'text': 'Most-Starred Python Projects on GitHub', 'font':{'size': 28}},
    'xaxis': {
        'title': {'text': 'Repository', 'font': {'size': 24}},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': {'text': 'Stars', 'font': {'size': 24}},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html')