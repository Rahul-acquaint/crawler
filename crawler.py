from bs4 import BeautifulSoup
from securityheaders.core import analyze_url
import requests
from wp_version_checker import check_domains
import re
# http://lifeactionrevival.org/

# def get_seo_data(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     title = soup.find("title").get_text()
#     meta_description = soup.find("meta")#, attrs={"name": "description"}
#     # Extract other SEO-related information
#     return {"title": title, "meta_description": meta_description}

# # Call this function within your loop for each website
# seo_data = get_seo_data("https://www.youtube.com/")
# print(seo_data)


# Google
# AIzaSyCjC-KGCkvcta_1fMXHJcUbXY8C2hkq9yE

# GTMatrix
# 091f83815ffede0c83e45bf1762436aa

class Crawler:

    GTMETRIX_API_KEY="091f83815ffede0c83e45bf1762436aa"
    GOOGLE_API_KEY="AIzaSyCjC-KGCkvcta_1fMXHJcUbXY8C2hkq9yE"

    def __init__(self, url):
        self.url=url
        self._response= requests.get(url)
    

    def get_gtmetrix_data(self, url):
        endpoint = "https://gtmetrix.com/api/2.0/tests"
        headers = {
            "Content-Type": "application/vnd.api+json"
        }
        auth = (self.GTMETRIX_API_KEY, '') 
        
        data = {
            "data": {
                "type": "test",
                "attributes": {
                    "url":url,
                    "adblock":  1
                }
            }
        }
        
        response = requests.post(endpoint, headers=headers, auth=auth, json=data)
        data = response.json()
        return data
    
    def get_seo_data(self,url):
        # Extract other SEO-related information

        response = self._response
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title").get_text()
        meta_description_tag = soup.find("meta", attrs={"name": "description"})
        meta_description = meta_description_tag['content'] if meta_description_tag else None
        return {"title": title, "meta_description": meta_description}
    
    def get_security_headers(self, url):
        security_results = analyze_url(url)
        return security_results

    def mobile_compatibility(self, url):
        endpoint = "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?alt=json&key=AIzaSyCjC-KGCkvcta_1fMXHJcUbXY8C2hkq9yE"
        params = {
            "url": self.url,
             "requestScreenshot": False
        }
        response = requests.post(endpoint, params=params)
        data = response.json()
        if response.status_code == 200:
            return data
        
        return  {
            "status":"FAILED",
            "content": data
        }
    
    def get_wordpress_version(self, url):
        url = self.url
        if  url[-1] == '/': url+="feed/"
        else: url+="/feed/"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "xml")
        generator = soup.find("generator")
        wp_url =   generator.get_text().split("=") if generator else []
        wp_version=None
        if len(wp_url)> 1:
            wp_version=wp_url[1] 
        return wp_version


    def find_plugins_with_versions(self, url):
        response = requests.get(url)
        html_content = response.text

        # Use regular expressions to find references to plugin files
        plugin_pattern = re.compile(r'/wp-content/plugins/([^/]+)/')
        plugins = set(plugin_pattern.findall(html_content))

        plugin_versions = {}

        for plugin in plugins:
            # Look for version information in the plugin's JavaScript or CSS files
            js_url = f"{url}/wp-content/plugins/{plugin}/script.js"
            css_url = f"{url}/wp-content/plugins/{plugin}/style.css"

            js_response = requests.get(js_url)
            css_response = requests.get(css_url)

            js_version = re.search(r'@version\s*:\s*(\S+)', js_response.text)
            css_version = re.search(r'Version:\s*(\S+)', css_response.text, re.IGNORECASE)

            plugin_versions[plugin] = js_version.group(1) if js_version else css_version.group(1) if css_version else "Version not found"

        return plugin_versions

obj=Crawler("https://saracino.com.mt/")
print("======>>>>>>>>", obj.get_wordpress_version("https://saracino.com.mt/"))


# import requests

# GTMETRIX_API_KEY = '091f83815ffede0c83e45bf1762436aa'

# def get_status():
#     endpoint = "https://gtmetrix.com/api/2.0/status"
#     auth = (GTMETRIX_API_KEY, '')  # Use your GTmetrix API key as the username and leave the password empty
#     response = requests.get(endpoint, auth=auth)
#     data = response.json()
#     return data

# def main():
#     status_data = get_status()
#     print(status_data)
    
# if __name__ == "__main__":
#     main()