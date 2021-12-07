# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from news_scrapy import settings
import pyodbc
from scrapy.exporters import CsvItemExporter

###########################CSV######################################################################
# class CsvPipeline:
# 	def __init__(self):
# 		self.file = open('posts.csv','wb')
# 		self.exporter =CsvItemExporter(self.file,encoding='big5')
# 		self.exporter.start_exporting()

# 	def process_item(self,item,spider):
# 		self.exporter.export_item(item)
# 		return item

# 	def close_spider(self,spider):
# 		self.exporter.finish_exporting()
# 		self.file.close()
###########################CSV######################################################################

###########################SQL######################################################################
# class NewsScrapyPipeline:
# 	def open_spider(self,spider):
# 		self.conn = pyodbc.connect('Driver={SQL Server};'
#                               'Server=LAPTOP-VFEIS9GU;'
#                               'Database=Scrapy;'
#                               'Trusted_Connection=yes;')
# 		self.cursor=self.conn.cursor()
# 		print("資料庫連線成功")

# 	def process_item(self, item, spider):
# 		self.cursor.execute("INSERT INTO [Scrapy].[dbo].[Test](post_title,post_date,post_author)VALUES(?,?,?)",(item['post_title'],item['post_date'],item['post_author']))
# 		return item

# 	def close_spider(self,spider):
# 		self.conn.commit()
# 		self.conn.close()
###########################SQL######################################################################