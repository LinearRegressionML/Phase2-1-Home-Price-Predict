import scrapy
from ..items import CrawldivarItem


class DivarSpider(scrapy.Spider):
    name = 'divar'
    allowed_domains = ['divar.ir']
    start_urls = ['https://divar.ir/s/tehran/buy-residential']

    def parse(self, response):
        # Main_Page=response.xpath("//div[@class='post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46']")
        # for item in Main_Page:
        #     link="https://divar.ir"+item.xpath(".//a/@href").get()

        tokens=[]
        token_file=open('tokens_20000.txt','r')
        # print(token_file)
        tokens=token_file.read().split(',')
        
        for t in tokens:
            link="https://divar.ir/v/"+t
            home_info = CrawldivarItem(link=link)

            if link:
                request=scrapy.Request(link,callback=self.parse_page_detail)
                request.meta['item'] = home_info
                yield request
                
    def parse_page_detail(self,response):
        item = response.meta['item']

        item['title']=response.xpath("//*[@id='app']/div[1]/div/div[1]/div[1]/div[1]/div/div[1]/text()").get()
        item['neighbourhood']=response.xpath("//div[@class='kt-page-title__subtitle kt-page-title__subtitle--responsive-sized']/text()").get()

        first_three_data=response.xpath("//div[@class='kt-group-row-item kt-group-row-item--info-row']") 
        item['size_metre'] = first_three_data[0].xpath(".//span[2]/text()").get()
        item['construct_year'] = first_three_data[1].xpath(".//span[2]/text()").get()
        item['number_of_room'] = first_three_data[2].xpath(".//span[2]/text()").get()
        
        second_three_data=response.xpath("//div[@class='kt-base-row__end kt-unexpandable-row__value-box']")
        item['total_price'] = second_three_data[0].xpath(".//p/text()").get()
        item['price_perMetre'] = second_three_data[1].xpath(".//p/text()").get()
        if (len(second_three_data)==4):
            item['floor_number'] = second_three_data[3].xpath(".//p/text()").get()
        else:
            item['floor_number'] = second_three_data[2].xpath(".//p/text()").get()

        # elevator, parking, cage, balcon 
        # این آیتم ها در آگهی های مختف متغیر است
        # مجبوریم همه آیتم ها را با هم دریافت کنیم
        # و در مرحله تمیز کردن داده ها آن ها جدا کنیم
        item['facilities']=response.xpath("//span[@class='kt-group-row-item__value kt-body kt-body--stable']/text()").getall()
        
        item['description'] = response.xpath("//p[@class='kt-description-row__text kt-description-row__text--primary']/text()").get()
        
        yield item
