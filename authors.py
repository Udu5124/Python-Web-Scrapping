import requests
import bs4

# Create a set of authors so that no names are repeated
authors = set()

# Base URL for the web page
base_url = 'http://quotes.toscrape.com/page/{}/'
n = 1

# Iterate till the last page
while True:
    scrape_url = base_url.format(n)
    n += 1
    res = requests.get(scrape_url)

    # Given that last page contains 'No quotes found!'
    if "No quotes found!" in res.text:
        break

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Add names to authors to set
    for items in soup.select('.author'):
        authors.add(items.getText())

print('List of authors : \n')
for items in authors:
    print(items)