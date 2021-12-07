import scrapy
import bs4
 
 
class InsideSpider(scrapy.Spider):
    name = 'inside'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['https://www.inside.com.tw/tag/ai']

# #BeautifulSoup方式定位元素
#     def parse(self, response):
#         soup = bs4.BeautifulSoup(response.text, 'lxml')
#         titles = soup.find_all('h3', {'class': 'post_title'})
#         for title in titles:
#             print(title.text.strip())
 
# #Scrapy CSS方法取得單一元素值
#     def parse(self, response):
#         title = response.css("a.js-auto_break_title::text").get()
#         print(title)

# #Scrapy CSS方法取得多個元素值
#     def parse(self,response):
#     	titles=response.css("a.js-auto_break_title::text").getall()
#     	print(titles)

# #Scrapy CSS方法取得子元素值
#     def parse(self,response):
#     	titles=response.css("h3.post_title a::text").getall()
#     	for title in titles:
#     		print(title)

# # Scrapy CSS方法取得元素屬性值
#     def parse(self,response):
#     	urls=response.css("a.js-auto_break_title::attr(href)").getall()
#     	for url in urls:
#     		print(url)

# #Scrapy XPath方法取得單一元素值
#     def parse(self,response):
#     	title = response.xpath("//a[@class='js-auto_break_title']/text()").get()
#     	print(title)

# # Scrapy XPath方法取得多個元素值
#     def parse(self,response):
#     	title = response.xpath("//a[@class='js-auto_break_title']/text()").getall()
#     	print(title)

#     def parse(self,response):
#     	list1=[]
#     	titles = response.xpath("//a[@class='js-auto_break_title']/text()").getall()
#     	for title in titles:
#     		list1.append(title)
#     	print(list1)

# #Scrapy XPath方法取得子元素值
#     def parse(self,response):
#     	titles = response.xpath("//div[@class='post_list_item_content']/h3[@class='post_title']/a/text()").getall()
#     	for title in titles:
#     		print(title)

# Scrapy XPath方法取得元素屬性值
    # def parse(self,response):
    # 	titles = response.xpath("//a[@class='js-auto_break_title']/@href").getall()
    # 	for title in titles:
    # 		print(title)

#測試自動翻頁之用
    # count = 1 #指定頁數
    def parse(self,response):
    	yield from self.scrape(response)
    	next_page_url = response.xpath("//a[@class='pagination_item pagination_item-next']/@href")
    	if next_page_url:
    		url = next_page_url.get()
    		# InsideSpider.count+=1 #指定頁數
    		# if InsideSpider.count<=7: #指定頁數
    			# yield scrapy.Request(url,callback=self.parse) #指定頁數
    		yield scrapy.Request(url,callback=self.parse)

    def scrape(self,response):
    	post_titles = response.xpath("//a[@class='js-auto_break_title ']/text()").getall()
    	post_dates  = response.xpath("//li[@class='post_date']/span/text()").getall()
    	post_authors= response.xpath("//span[@class='post_author']/a/text()").getall()
    	post_hrefs  = response.xpath("//a[@class='js-auto_break_title ']/@href").getall()
    	for data in zip(post_titles,post_dates,post_authors,post_hrefs):
    		NewScraperItem={
    			"post_title":data[0],
    			"post_date":data[1],
    			"post_author":data[2],
    			"post_href":data[3]
    		}
    		yield NewScraperItem



#save DB&csv之用
    # def parse(self,response):
    # 	post_titles = response.xpath("//a[@class='js-auto_break_title']/text()").getall()
    # 	post_dates  = response.xpath("//li[@class='post_date']/span/text()").getall()
    # 	post_authors= response.xpath("//span[@class='post_author']/a/text()").getall()
    # 	for data in zip(post_titles,post_dates,post_authors):
    # 		NewScraperItem={
    # 			"post_title":data[0],
    # 			"post_date":data[1],
    # 			"post_author":data[2]
    # 		}
    # 		yield NewScraperItem