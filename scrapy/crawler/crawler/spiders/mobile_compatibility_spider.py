import scrapy

class MobileCompatibilitySpider(scrapy.Spider):
    name = 'mobile_compatibility'
    start_urls = ['https://youtube.com']  # Replace with the URLs you want to check

    def parse(self, response):
        # Check for presence of mobile-friendly HTML elements
        mobile_elements_present = (
            response.css('meta[name="viewport"]') or
            response.css('meta[name="apple-mobile-web-app-capable"]') or
            response.css('link[rel="apple-touch-icon"]')
        )

        if mobile_elements_present:
            print(f"{response.url} is mobile compatible.")
        else:
            print(f"{response.url} is not mobile compatible.")