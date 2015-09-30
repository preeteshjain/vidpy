# vidpy
A Python based customizable script for getting/scraping links to videos hosted on any website. Based on Scrapy and BeautifulSoup.

#### Why?
I created this script for my friend who hasn't watched all the videos in the Maths section from [gre.magoosh.com](http://gre.magoosh.com) and was worried about his subscription, that was going to end soon. There were way too many links to click and download each video. So I built this script with just 2 hours of effort to scrape all the links to the videos (where they were directly hosted, in this case, Cloudfront), so that he can download all the videos in one shot.

#### Requirements:
- A valid subscription is neccessary for downloading videos off the site.
- Scrapy and BeautifulSoup should be installed for the program to work. Links:
    - [Install Scrapy](http://doc.scrapy.org/en/1.0/intro/install.html)
    - [Install BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

#### Executing the script:
See [Scrapy's documentation](http://doc.scrapy.org/en/latest/intro/tutorial.html) to learn how to execute spiders and crawlers.

#### Features:
- You can customize this Python code to different categories in the site. In the current code, only the videos in Mathematics section will be scraped from [gre.magoosh.com](http://gre.magoosh.com).
- The algorithm and logic behind this script can be applied to any site to extract any form of data with precision.
- Only the stuff you need will be extracted and rest all will be ignored. This saves time and overall bandwidth used to successfully run the script.

**Note to contributors:** Please update the documentation whenever neccessary.
