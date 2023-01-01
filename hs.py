import scrapy
from ..items import homeItem
# import pandas as pd

class Hs(scrapy.Spider):
    name = 'hs'
    allowed_domains = ['https://iranfile.ir/FileDetail']


    def parse(self, response):
        item = homeItem()
        if 2>1:
            # print('-------------------------------------------------------------------------------------------------------------------------------------1')
            try:
                item['code'] = response.xpath("//span[@class='file-data']//text()").extract()[1]
            except:
                return()

            # item['ejare']= response.xpath("//span[@class='label-data']//text()").extract()[6]
            if response.xpath("//span[@class='label-data']//text()").extract()[6] == "مبلغ ودیعه:":
                return()



            item['tarick'] = response.xpath("//span[@class='file-data']//text()").extract()[0]
            item['noemelk'] = response.xpath("//span[@class='file-data']//text()").extract()[2]
            item['address'] = response.xpath("//span[@class='file-data']//text()").extract()[3].strip()
            item['ghymatkol'] = int(response.xpath("//span[@class='file-data']//text()").extract()[4].replace(" تومان", "" ).replace(",", "" ))
            item['gheymatvahed'] = int(response.xpath("//span[@class='file-data']//text()").extract()[5].replace(" تومان", "" ).replace(",", "" ))
            # print('333333333333333333333333333333333333333', item['ghymatkol'] ,'33333333333333333333')

            item['tabaghat'] = response.xpath("//div[@class='file-data']//text()").get().strip()
            item['vahed'] = response.xpath("//div[@class='file-data']//text()").get().strip()
        if 3>1:
            moshpart =  response.xpath("//div[@class='col-xs-8 col-md-4 info-melk-file-details']//text()").extract()
            moshakhasat={}
            # print('333333333333333333333333333333333333333', moshpart, '444444')

            for i in range(1,1+int(len(moshpart)),5):
                moshakhasat[moshpart[i]] = moshpart[i+2].strip()
                # item[f'{moshpart[i]}']= moshpart[i+2].strip()

            try:
                item['vaziat'] = moshakhasat['وضعیت ملک']
                item['sanad'] = moshakhasat['وضعیت سند']
                item['malek'] = moshakhasat['سکونت مالک']
            except:
                pass

            try:
                # print(1111,moshakhasat['سن بنا'])
                sen= moshakhasat['سن بنا']
                if 'نوساز' in sen:
                    sen=0
                    # print(444,sen)
            except:
                pass

            try:
                item['sen'] = 1401 - int(sen)
                # print(555, item['sen'])
            except:
                pass


            try:
                item['masahat'] =  moshakhasat['مساحت زمین']
            except:
                pass

            try:
                item['bar'] = (moshakhasat['طول بر'])
            except:
                pass

            try:
                item['nama'] = moshakhasat['نما']

            except:
                pass
        if 4>1:
            item['tabaghe'] = response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[1]//td[2]//text()").get().strip()
            item['zirbana'] =  response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[2]//td[2]//text()").get().strip()
            item['khab'] =  response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[3]//td[2]//text()").get().strip()
            item['tel'] =  response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[4]//td[2]//text()").get().strip()
            item['ashpazkhane'] =  response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[5]//td[2]//text()").get().strip()
            item['service'] =  response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[6]//td[2]//text()").get().strip()
            item['kafpoosh'] =  response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[7]//td[2]//text()").get().strip()
            item['openk'] = 'yes' if 'checked' in  response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[8]//td[2]").get() else ''
            item['parking'] = 'yes' if 'checked' in response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[9]//td[2]").get() else ''
            item['anbari'] = 'yes' if 'checked' in response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[10]//td[2]").get() else ''
            item['balkon'] = 'yes' if 'checked' in response.xpath("//div[@class='col-xxs-12 col-xs-12 col-sm-12 col-md-12']//tr[11]//td[2]").get() else ''

            item['shomali'] = 'yes' if 'checked' in response.xpath("//div[@class='col-xxs-12 col-xs-8 col-sm-4 centered-text positions']//div[1]//div[1]").get() else ''

            temp= response.xpath('//html / body/script[1] / text()').get()
            position1 = temp.find('LatPosition=')
            position2 = temp.find('LngPosition=')
            position3 = temp.find('PolygonData =')
            item['lat']=temp[(position1+13):(temp.find("'", position1+15))]
            item['long'] = temp[(position2 + 13):(temp.find("'", position2+15))]
            item['poly'] = temp[(position3 + 13):(temp.find(';', position3))]


            '''polygun
            print(5555,position3 , 66 , position4,7777)
            print(1111111, item['lat'],item['long'],33333333, item['poly'],444444,temp , 222222222222222, item['tabaghe'])
            
            
            '''



        if 5>1:
            table =  response.xpath("//div[@class='col-xxs-12 col-xs-12 col-md-12']//div[@class='check-box-info']//text()").extract()
            tajhiz = []
            for i in range(1,1+int(len(table)/4)):
                cc =  response.xpath(f"//div[@class='col-xxs-12 col-xs-12 col-md-12']//div[@class='check-box-info'][{i}]//text()").extract()[2]
                tajhiz.append(cc)
            # print('vvvvvvvvvvvvvvvvvv',tajhiz)

            item['tajhiz'] = tajhiz

        yield item


    def start_requests(self):
        for i in range((3979000),0, -1):
            url = (f'https://iranfile.ir/FileDetail/{i}/')



            yield scrapy.Request( url,callback=self.parse )

