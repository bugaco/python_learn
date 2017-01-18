import requests

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

for submisson_dict in submission_dicts:
    print("\nTitle:", submisson_dict['title'])
    print("Discussion link:", submisson_dict['link'])
    print("score:", submisson_dict['score'])
