#Web scraping - parsing HTML with Beautiful Shop Module

import bs4
import requests
headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}

def get_headline(url, headers):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elements = soup.select('.body > h1:nth-child(1)')
    return elements[0].text

headline = get_headline('https://www.weather.gov',headers=headers)
print("Today's Weather Headline: " + headline)
