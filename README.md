# web-crawler
web crawler template

python3 -m pip install scrapy

# start a project
scrapy startproject tutorial
scrapy crawl quotes

# create a basic spider
scrapy genspider example example.com

# Create one-off web crawler
scrapy runspider brickset.py

# Interactive Scrapy
scrapy shell "http://a.url.com/to/explore/"
