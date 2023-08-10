from bs4 import BeautifulSoup
from securityheaders.core import analyze_url
import requests
from wp_version_checker import check_domains
import re

from requests_client import RequestsClient, ResposneType
from api_lists import APIEndpoint
from gtmatrix import GTMatrixClient

class Crawler:

    GTMETRIX_API_KEY="091f83815ffede0c83e45bf1762436aa"
    GOOGLE_API_KEY="AIzaSyCjC-KGCkvcta_1fMXHJcUbXY8C2hkq9yE"

    def __init__(self, url):
        self.url=url
    

    def get_gtmetrix_data(self):
        #  when you exceed this limit, you will get a 429 HTTP status code.
        gtmatrix_client =  GTMatrixClient(self.url)
        gtmatrix_client.start_test()
    
    def get_seo_data(self):
        # Extract other SEO-related information
        request_client = RequestsClient()
        response_data = request_client.get(self.url)
        soup = BeautifulSoup(response_data, "html.parser")
        title = soup.find("title").get_text()
        meta_description_tag = soup.find("meta", attrs={"name": "description"})
        meta_description = meta_description_tag['content'] if meta_description_tag else None
        return {"title": title, "meta_description": meta_description}
    
    def get_security_headers(self):
        security_results = analyze_url(self.url)
        return security_results

    def mobile_compatibility(self):
        endpoint = APIEndpoint.mobile_compatibility.format(self.GOOGLE_API_KEY)
        params = {
            "url": self.url,
             "requestScreenshot": False
        }
        request_client = RequestsClient(response_type=ResposneType.json)
        data = request_client.post(endpoint, params=params)
        if data.get("status", False) == 200:
            return data
        
        return  {
            "data": data
        }
    
    def get_wordpress_version(self):
        url = self.url
        if  url[-1] == '/': url+="feed/"
        else: url+="/feed/"

        request_client = RequestsClient(response_type=ResposneType.text)
        response_text =request_client.get(url)
        soup = BeautifulSoup(response_text, "xml")
        generator = soup.find("generator")
        wp_url =   generator.get_text().split("=") if generator else []
        wp_version=None
        if len(wp_url)> 1:
            wp_version=wp_url[1] 
        return wp_version

obj=Crawler("https://youtube.com/")
print("Response : ", obj.get_gtmetrix_data())