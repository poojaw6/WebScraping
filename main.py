# HTML Web Scraping using Beautiful Soup bs4
import requests
from bs4 import BeautifulSoup
url = "https://theoffice.fandom.com/wiki/Michael_Scott"

# Step1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step3: Traverse the HTML tree

# Types of objects that can be traversed
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# 4. Comment

# Get title of page
title = soup.title
# print(title)

# Get all paragraphs from page
paras = soup.find_all('p')
# print(paras)

# Get all anchor tags from page
anchors = soup.find_all('a')
# print(anchors)
all_links = set()
# Get all links on the page
for link in anchors:
    # print(link.get('href'))
    if(link.get('href')!='#'):
        linkText = link.get('href')
        all_links.add(link)
        # print(linkText)

# print(soup.find('p')) # gives first element
# print(soup.find('h2')['class']) # gives class of the element

# Find all elements with class lead
print(soup.find_all("h2", class_="pi-item"))

# Get text from tags/soup
print(soup.find('p').get_text())
# print(soup.get_text()) # to get full page text

# Comment Type Element
comm = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(comm)
print(soup2.p.string)
print(type(soup2.p.string))

navBarContent = soup.find(id='globalNavigation')
# print(navBarContent.contents) #returns list
for elem in navBarContent.contents:
    print(elem)

for elem in navBarContent.children:
    print(elem)

# .contents vs .children
# .contents = returns a tag's contents as a list
# .children = returns a tag's contents as a generator/iterator

for item in navBarContent.stripped_strings:
    print(item)

# Finding out parent
print(navBarContent.parent)

for item in navBarContent.parents:
    print(item.name)


# print(navBarContent.next_sibling.next_sibling)
# print(navBarContent.previous_sibling.previous_sibling)

# Get element via css selectors
element = soup.select(".WikiaPage")
print(element)