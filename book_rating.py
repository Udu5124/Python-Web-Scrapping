import requests
import bs4
import time

# Records the start time for running the code
start_time = time.time()

# Base url
page_url = 'http://books.toscrape.com/catalogue/page-{}.html'

# List to save the books with 5 star rating
five_star_titles = []

# Loop from first page to 50th page
for n in range(1, 51):

    # Iterating through every page on the website
    scrape_url = page_url.format(n)

    # Get page in res
    res = requests.get(scrape_url)

    # Format the page using lxml package
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # class .product_pod contains data of each book
    books = soup.select('.product_pod')

    # Iterate through each book and append in list if book has 5 stars
    for item in books:
        if [] == item.select(".star-rating.Five"):
            continue
        else:
            five_star_titles.append(item.select("h3 a")[0]['title'])

print('Books on toscrape.com with 5 star rating are :\n ')
for book_title in five_star_titles:
    print(book_title)

# End time for running code
end_time = time.time()
print(f'\nThe time required to perform web scrapping was : {end_time-start_time}secs.')