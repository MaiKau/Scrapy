# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

##########################宣告存放欄位#######################################
# class NewScraperItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     post_title = scrapy.Field()
#     post_date  = scrapy.Field()
#     post_author= scrapy.Field()
##########################宣告存放欄位#######################################


##########################宣告存放欄位#######################################
class HotNewsItem(scrapy,Item):
	hot_news_title=scrapy.Field()
	hot_news_intro=scrapy.Field()

##########################宣告存放欄位#######################################