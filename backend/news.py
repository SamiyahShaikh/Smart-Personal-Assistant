import requests

def get_news():
    api_key = 'YOUR_NEWSAPI_KEY'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    articles = response.json()['articles'][:5]
    headlines = [article['title'] for article in articles]
    return 'Top headlines: ' + ', '.join(headlines)
