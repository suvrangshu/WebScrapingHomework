#Author: Suvrangshu Ghosh
#Date Feb 24th 2019

from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
import sys
from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
import sys

#executable_path = {'executable_path': '/Users/sghosh/Documents/Suv/Personal/Berkeley/chromedriver.exe'}
executable_path = {"executable_path": "drivers/chromedriver"}
browser = Browser('chrome', **executable_path, headless=False)

#This code scrapes the following websites:
#----------------------------------------
#url = 'https://mars.nasa.gov/news/'
#pic_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#t_url = 'https://twitter.com/marswxreport?lang=en'
#fact_url = 'http://space-facts.com/mars/'
#hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

def scrape():
    
    # url = https://mars.nasa.gov/news/' 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(4)#Waiting to give time for loading
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    
    title = soup.find('div', class_='content_title') # gets 1st title
    news_title = title.text
    title_p = soup.find('div', class_='article_teaser_body') # gets paragraph text
    #get news details
    news_p = title_p.text
    
    ## Section to get image
    pic_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(pic_url)
    time.sleep(4) # giving time to load
    #navigating to main full image
    browser.click_link_by_partial_text('FULL IMAGE')

    #putting 1 sec sleep, to load page
    time.sleep(2)
    
    browser.click_link_by_partial_text('more info') #Click more info
    time.sleep(2)
    soup = BeautifulSoup(browser.html, "html.parser")
    #get image
    #title = soup.find_all('div', class_='content_title') # gets all title
    image = soup.find('img', class_='main_image') # gets 1st title
    #get the image path
    featured_image = image["src"]
    #creating full path for the image url:
    featured_image_url = 'https://www.jpl.nasa.gov' + featured_image
    
    #Twitter page:
    twit_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twit_url)
    time.sleep(2)
    soup = BeautifulSoup(browser.html, "html.parser")
    #twit = soup.find_all('div', class_='content_title') # gets all title
    twit = soup.find('p', class_='tweet-text') # gets 1st title
    mars_weather= twit.text
    #spliting to get rid of the - pic.twitter.com/WlR4gr8gpC
    x = mars_weather.split("\n")
    #picking only the part required
    mars_weather = x[0]
    
    #Fact Url Page :
    fact_url = 'http://space-facts.com/mars/'
    time.sleep(1)
    #pandas html to table
    tables = pd.read_html(fact_url)
    #put column head
    df = tables[0]
    df.columns = ['Mars_detail', 'Values']
    #pandas to HTML
    fact_table = df.to_html()

    #clean up new lines
    fact_table = fact_table.replace('\n', '')
    
    #Mars Hemispheres Page:

    hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #Mars Hemispheres

    browser.visit(hem_url)
    time.sleep(4)
    hemisphere_image_urls = []

    #soup = BeautifulSoup(browser.html, "html.parser")
    h_soup = BeautifulSoup(browser.html, 'lxml')
    
    hemis_check = h_soup.find_all(class_='description')
    #reading in loop
    for results in hemis_check:
        h1 = results.h3.text
        #href_image = h1['href']
        browser.click_link_by_partial_text(h1)
        time.sleep(1)
        hemis_temp_soup = BeautifulSoup(browser.html, 'lxml')
        image_link = hemis_temp_soup.find('a',target="_blank" )
        href_image = image_link["href"]
        hemisphere_image_urls.append({'title':h1, 'img_url':href_image})
        browser.visit(hem_url) # takes back to home
        #print(href_image)
    
    #close browsers
    browser.quit()
    
    #Final Output dictionary
    final_output = dict (
        top_news_head = news_title,
        news_detail = news_p,
        featured_image = featured_image_url,
        weather = mars_weather,
        facts_table = fact_table,
        hemisphere_images = hemisphere_image_urls
           )
    
    return final_output
