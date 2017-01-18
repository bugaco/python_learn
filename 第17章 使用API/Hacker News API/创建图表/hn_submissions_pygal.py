import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# 处理有关每篇文章的信息
submissions_ids = r.json()
submission_dicts = []
for submission_id in submissions_ids[:10]:
    # 对于每篇文章，都执行一个API调用
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json'
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'score': response_dict.get('score', 0),
    }

    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('score'), reverse=True)

names = []
plot_dicts = []
for submisson_dict in submission_dicts:
    print("\nTitle:", submisson_dict['title'])
    names.append(submisson_dict['title'])
    print("Discussion link:", submisson_dict['link'])
    print("score:", submisson_dict['score'])
    plot_dict = {
        'value': submisson_dict['score'],
        'xlink': submisson_dict['link'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
# chart = pygal.Bar(x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')