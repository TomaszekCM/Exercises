# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on
# this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
#
# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen
# so that you can read the full article without having to click any buttons.
#
# (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries
# through the solution of the exercise posted here.)
#
# This will just print the full text of the article to the screen.
# It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.


import requests
from bs4 import BeautifulSoup

def get_plain_text():
    web = requests.get('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
    web_html = web.text

    soup = BeautifulSoup(web_html, 'html.parser')
    text = ""
    for i in soup.find_all("div", {"class": "article__body"}):
        text += i.text

    return text

if __name__=="__main__":
    print(get_plain_text())