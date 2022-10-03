# Note: this is a 4-chili exercise, not because it introduces a concept (although it introduces a new library),
# but because this exercise is more like a project. Feel free to skip this and come back when you’re more ready!
#
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
# on the New York Times homepage.
#
# https://www.nytimes.com/


import requests
from bs4 import BeautifulSoup

def nt_titles():
    r = requests.get('https://www.nytimes.com/')
    r_html = r.text

    soup = BeautifulSoup(r_html,'html.parser')
    all_titles = []
    for title in soup.find_all('h3'):
        all_titles.append(title.text)

    return all_titles

if __name__ == "__main__":
    for i in nt_titles():
        print(i)