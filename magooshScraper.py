import scrapy
from bs4 import BeautifulSoup

class magooshSpider(scrapy.Spider):
	name = 'magoosh'
	start_urls = ['http://gre.magoosh.com/login']

	def parse(self, response):
		return scrapy.FormRequest.from_response(
			response,
			'''
			Replace the fake text below with your own registered
			email and password on http://gre.magoosh.com:
			'''
			formdata={'session[login]': 'abc@xyz.com', 'session[password]': 'somepassword'},
			callback=self.after_login
		)

	def after_login(self, response):
		if 'Dashboard' in response.body:
			self.logger.info('Logged in successfully!')

		return scrapy.Request('http://gre.magoosh.com/lessons',
			callback=self.lessonsPage_loaded)

	def lessonsPage_loaded(self, response):
		self.logger.info('Lessons page opened.')
		soup = BeautifulSoup(response.body)
		for categ in soup.find_all('h2'):
			# Set the Subject name to crawl
			# In this example, Maths section is scraped.
			if 'Math' in categ:
				self.logger.info('Math section found.')
				cgparent = categ.parent.parent
				for vu in cgparent.find_all('a'):
					link = str(vu.get('href'))
					if '/lessons/' in link:
						s = 'http://gre.magoosh.com' + str(link) + "\n"
						req = scrapy.Request(s, callback=self.videoPage_loaded)
						yield req
		return

	def videoPage_loaded(self, response):
		self.logger.info('Fetching video...')
		soup = BeautifulSoup(response.body)
		for div in soup.find_all('div'):
			if div.get('data-file'):
				vl = div.get('data-file')
				f = open('scrapedVideoLinks.txt', 'a')
				f.write(str(vl) + '\n')
				f.close()
