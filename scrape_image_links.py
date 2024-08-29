import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep

base_url = "https://www.quantamagazine.org/archive/page/"

fd = open("image_links.txt", "a")

for page_number in range(1, 221):
    page_url = f"{base_url}{page_number}/"
    print(f"Scraping {page_url}")
    
    response = requests.get(page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all divs with the class "card clearfix mv05 pv1"
        cards = soup.find_all('div', class_="card clearfix mv05 pv1")
        
        for card in cards:
            # Find the anchor tag and extract the href
            link = card.find('a')
            if link:
                article_url = urljoin(base_url, link['href'])
                print(f"Found article URL: {article_url}")
                
                # Scrape the article page
                article_response = requests.get(article_url)
                if article_response.status_code == 200:
                    article_soup = BeautifulSoup(article_response.content, 'html.parser')
                    
                    # Find the figure with class "leading-0" and download the image
                    figure = article_soup.find('figure', class_="leading-0")
                    if figure:
                        image = figure.find('img')
                        if image and 'src' in image.attrs:
                            image_url = image['src']
                            fd.write(f"{image_url}\n")
                else:
                    print(f"Failed to scrape {article_url}")
        
    else:
        print(f"Failed to scrape {page_url}")
    
    # Be polite and avoid spamming the server
    sleep(2)

fd.close()
print("Scraping completed.")
