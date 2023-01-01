import scrapy
import json
  
class Exit(scrapy.Spider):
    name='home11'
    
    start_urls=['https://shabesh.com/search/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4/%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%A2%DB%8C%D8%AA-%D8%A7%D9%84%D9%84%D9%87-%DA%A9%D8%A7%D8%B4%D8%A7%D9%86%DB%8C-%D8%AA%D9%87%D8%B1%D8%A7%D9%86']
    def parse(self, response):
        Question_Page=response.xpath("//div[@class='list_announceListMode__69v30 mt-2  col-12']")
        for item in Question_Page:
            link='https://shabesh.com'+item.xpath(".//a/@href").extract_first()
            print('1111111111111111111111111111111111111111111111111111111111111111')
            print(link)
            # features=Shabesh(link=link)
            if link:
                request=scrapy.Request(link,callback=self.parse_page_detail)
                yield request

        next_page=response.xpath('//link[@rel="next"]/@href').get()
        print('============================================')
        print('next',next_page)
        print('==================----------------------==========================')
        if next_page:
            print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
            yield scrapy.Request(next_page, callback=self. parse)
        print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
        
    def parse_page_detail(self, response):
        t=response.xpath('//head/script[contains(text(), "geo")]/text()').get()
        dic=json.loads(t[:])
        d=dic[1]
        s=d['geo']
        
        print('0000000000000000000000000000000000000000000000000000000000')
        table1={
                'نوع ملک':response.css('div.announce-specs span::text')[5].get(),
                'متراژ':response.css('div.announce-specs span::text')[7].get(),
                'قیمت':response.css('div.announce-specs span::text')[9].get(),
                'قیمت(متر مربع)':response.css('div.announce-specs span::text')[11].get(),
                'منطقه':response.css('div.announce-specs span::text')[13].get(),
                'سال ساخت':response.css('div.announce-specs span::text')[15].get(),
                'تعداد خواب':response.css('div.announce-specs span::text')[17].get(),
                'جهت ساختمان':response.css('div.announce-specs span::text')[19].get(),
                'نوع سند':response.css('div.announce-specs span::text')[21].get(),
                'طبقه':response.css('div.announce-specs span::text')[23].get(),
                'تعداد طبقات':response.css('div.announce-specs span::text')[25].get(),
                'سرویس بهداشتی':response.css('div.announce-specs span::text')[27].get(),
                'تعداد واحد طبقه':response.css('div.announce-specs span::text')[29].get(),
                'نوع کف':response.css('div.announce-specs span::text')[31].get(),
                'نما':response.css('div.announce-specs span::text')[33].get(),
                'سرمایش':response.css('div.announce-specs span::text')[35].get(),
                'گرمایش':response.css('div.announce-specs span::text')[37].get(),
                'آب گرم':response.css('div.announce-specs span::text')[39].get(),
                'تاریخ انتشار':response.css('div.announce-specs span::text')[41].get(),

                'پارکینگ':response.css("div.announce_announceProp__eh2FN span::text")[0].get(),
                'آسانسور':response.css("div.announce_announceProp__eh2FN span::text")[1].get(),
                # 'لابی':response.css("div.announce_announceProp__eh2FN span::text")[2].get(),
                'انباری':response.css("div.announce_announceProp__eh2FN span::text")[3].get(),
                'latitude':s['latitude'],
                'longitude':s['longitude']
                # 'سونا و جکوزی':response.css("div.announce_announceProp__eh2FN span::text")[4].get(),
                # 'سالن اجتماعات':response.css("div.announce_announceProp__eh2FN span::text")[5].get(),
                # 'تهویه هوا':response.css("div.announce_announceProp__eh2FN span::text")[6].get(),
                # 'روف گاردن':response.css("div.announce_announceProp__eh2FN span::text")[7].get(),
                # 'پنجره دو جداره':response.css("div.announce_announceProp__eh2FN span::text")[8].get(),
                # 'درب ضد سرقت':response.css("div.announce_announceProp__eh2FN span::text")[9].get(),
                # 'سیستم اعلام حریق':response.css("div.announce_announceProp__eh2FN span::text")[10].get(),
                # 'باربیکیو':response.css("div.announce_announceProp__eh2FN span::text")[11].get(),
                # 'بالکن':response.css("div.announce_announceProp__eh2FN span::text")[12].get(),
                # 'سرایدار':response.css("div.announce_announceProp__eh2FN span::text")[13].get(),
                # 'استخر':response.css("div.announce_announceProp__eh2FN span::text")[14].get(),
                # 'حیاط':response.css("div.announce_announceProp__eh2FN span::text")[15].get(),
                # 'سالن ورزشی':response.css("div.announce_announceProp__eh2FN span::text")[16].get(),
                # 'گرمایش مرکزی':response.css("div.announce_announceProp__eh2FN span::text")[17].get(),
                # 'فرنیش':response.css("div.announce_announceProp__eh2FN span::text")[18].get(),
                # 'آیفون تصویری':response.css("div.announce_announceProp__eh2FN span::text")[19].get(),
                # 'دزدگیر':response.css("div.announce_announceProp__eh2FN span::text")[20].get(),
                # 'درب ریموت':response.css("div.announce_announceProp__eh2FN span::text")[21].get(),
               

                
         }
            
        yield table1