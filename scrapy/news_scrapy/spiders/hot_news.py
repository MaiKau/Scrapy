import scrapy


class HotNewsSpider(scrapy.Spider):
    name = 'hot_news'
    allowed_domains = ['www.inside.com.tw']
    start_urls = ['http://www.inside.com.tw/']

    def parse(self, response):
        post_urls=response.xpath("//a[@class='hero_menu_link']/@href").getall()
        for post_url in post_urls:
        	yield scrapy.Request(post_url,self.parse_content) #前參為第二層的url，後參為parse_content為下述自訂方法的名稱

    def parse_content(self,response):
    	hot_news_title=response.xpath("//h1[@class='post_header_title js-auto_break_title']/text()").get()
    	hot_news_intro = response.xpath("//div[@class='post_introduction']/text()").get()
    	print(f"這邊是第一層網頁：{hot_news_title}", f"\n這是第二層網頁：{hot_news_intro}")

    	HotNewsItem={
    		"hot_news_title":hot_news_title,
    		"hot_news_intro":hot_news_intro
    	}
    	return HotNewsItem
