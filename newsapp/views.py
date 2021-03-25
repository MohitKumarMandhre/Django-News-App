from django.shortcuts import render
import requests
# from newsapi import NewsApiClient

# Create your views here.
# In views, we create a view named index which takes a request 
# and
#  renders an html as a response. Firstly we import newsapi from NewsApiClient.

# def index(request) : 
    # newsapi = NewsApiClient(api_key=key")
    # top = newsapi.get_top_headlines(sourses="techcrunch")

    # l = top['articles'] 
    # desc = []
    # news = []
    # img = []

    # for i in range(len(l)) :
    #     f = l[i] 
    #     news.append(f['title'])
    #     desc.append(f['description'])
    #     img.append(f['urlToImage'])

    # myList = zip(news, desc, img)
    # return render( request, 'index.html', context={"mylist" : myList} )

def index(request) :

    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=API KEY')
    response = requests.get(url)
    r = response.json() 
    l = r['articles']
    desc =[]
    news =[]
    img =[]
    url = []
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)
    
    return render(request, 'index.html', context={'mylist': mylist})
