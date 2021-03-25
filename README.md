# Django-News-App

- ##  Django-News-App is a news app that presents the latest news in crisp format from trusted national and international publishers. Read the latest India News, Breaking ...

## To setup all the libraries use :-

- cd to the directory where requirements.txt is located.
- activate your virtualenv.
- run: pip install -r requirements.txt in your shell.

- ### Requirements.txt
![alt text](https://github.com/MohitKumarMandhre/Django-News-App/blob/main/PICS/c1.PNG)

## API USED

- #### News API is great as a data source for news tickers and other applications where you want to show your users live headlines.
We track headlines in 7 categories across over 50 countries, and at over a hundred top publications and blogs, in near real time.


- ### API CALL ( Get the current top headlines for a country or category )

- #### https://newsapi.org/v2/top-headlines?country=in&apiKey=API_KEY

- ### API IN JSON FORMAT EXAMPLE ( RAW FORM )

- #### one object of article :-
- {
"source": {
"id": null,
"name": "CNBCTV18"
},
"author": null,
"title": "Stock Market Live: Sensex down 350 points, Nifty below 14,500; Banks, auto stocks drag - CNBCTV18",
"description": "Stock Market Live: Indian indices were trading lower on Thursday as selling continued mainly dragged by banks, auto and IT stocks. Broader markets were also trading lower with the midcap and smallcap indices down over a percent each. Meanwhile, Asian equities…",
"url": "https://www.cnbctv18.com/market/stock-market-live-indian-indices-to-open-in-the-red-following-mixed-cues-in-asian-peers-8716431.htm",
"urlToImage": "https://images.cnbctv18.com/wp-content/uploads/2019/08/bse-768x559.jpg",
"publishedAt": "2021-03-25T04:15:29Z",
"content": null
}

- # GALLERY 

- ![alt text](https://github.com/MohitKumarMandhre/Django-News-App/blob/main/PICS/GIF-news.gif)

- ## Replace Api-key with yours in views.py in index method here

- ### url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=API-KEY')
