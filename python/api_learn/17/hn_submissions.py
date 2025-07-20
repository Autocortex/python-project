from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Создание отдельного вызова API для каждой статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    # Построение словаря для каждой статьи.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse = True)
titles, hn_links, comments = [],[],[]
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    url = submission_dict['hn_link']
    hn_link = f"<a href='{url}>Open link</a>"
    hn_links.append(hn_link)
    comments.append(submission_dict['comments'])

print(titles)
print(hn_links)
print(comments)

data = [{
    'type': 'bar',
    'x': titles,
    'y': comments,
    'hovertemplate': hn_links,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line':{'width': 1.5,'color': 'rgb(25,25,25)'},
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': {
        'text': 'Article statistics by comments.', 'font': {'size': 28}
    },
    'xaxis':{
        'title':{'text': 'Articles', 'font':{'size': 26}},
        'tickfont':{'size': 14}

    },
    'yaxis':{
        'title':{'text': 'Comments', 'font':{'size': 26}},
        'tickfont':{'size': 14}
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'hn_subs.html')


