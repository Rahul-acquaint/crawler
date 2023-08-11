import scrapy
import requests
from crawler import configs

class XanoMainDBSpider(scrapy.Spider):

    name="x_main_db"
    url = "https://x8ki-letl-twmt.n7.xano.io/api:LbJeqyay/maindb_pagination?page={}"
    GTMETRIX_API_KEY=configs.GTMETRIX_API_KEY
    
    def start_requests(self):
        url = self.url.format(1)
        yield scrapy.Request(url=url)

    def xeno_store(self, link, id):

        url = "https://x8ki-letl-twmt.n7.xano.io/api:LbJeqyay/gtmetrix_test"
        data ={
            "maindb_id":id,
            "link":link
        }
        response = requests.post(url, json=data)
        if response.status_code == 200: 
            print("XENO data save successfully ============================>>>>>")
            

    def start_test(self, url, id):
        headers = {"Content-Type": "application/vnd.api+json"}
        auth = (self.GTMETRIX_API_KEY, '')
        data = { "data": {
                "type": "test",
                "attributes": {"url":url,
                    "adblock":  1
                }}}

        response = requests.post("https://gtmetrix.com/api/2.0/tests", headers=headers, auth=auth, json=data)
        print("GTMetri ======================>>>>>>", url,  response.status_code, response.json())
        if response.status_code == 202:
            response_data = response.json()
            test_link = response_data.get("links", {}).get("self", None)
            if test_link:
                print("test started ------------------->>>>>>", test_link)
                self.xeno_store(test_link, id)

    def parse(self, respose):
        response_data = respose.json()
        total_page = response_data.get("pageTotal")
        # cur_page = response_data.get("curPage")                       

        for i in range(2, total_page+1):
            url = self.url.format(i)
            yield scrapy.Request(url=url)
            
        items = response_data.get("items", [])
        site_webs = [{"url":item.get("site_web"), "id":item.get("id")} for item in items]


        for site in site_webs:
            # print("====================>>>>>>", site)
            self.start_test(**site)


