import requests
from wordcloud import WordCloud,STOPWORDS
import sys

if len(sys.argv) <= 2:
    print('Too few arguments.  You need to specify thread_id and filename.')
    print('example: python3 ./' + sys.argv[0]+' 8ish3t file.png')
    exit()
else:
    base_url = 'https://api.pushshift.io/reddit/search/comment/?fields=body&limit=25000&link_id='

    thread_id = sys.argv[1]

    final_url = f"{base_url}{thread_id}"
    print(final_url)

    response = requests.get(final_url)
    data_arr = response.json()['data']

    comment_str = " ".join(comment['body'] for comment in data_arr)
    stop = set(STOPWORDS)
    stop.add('https')
    stop.add('gif')

    wc = WordCloud(height=500, width=1000, stopwords=stop).generate(comment_str)

    image = wc.to_file(sys.argv[2])
    exit()