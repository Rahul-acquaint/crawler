import requests


class AbstractModel:

    url ,auth ,headers ,params = None, None, {}, {}

    def get_params(self): return self.params
    def get_headers(self): return self.headers
    def get_auth(self): return self.auth
    def get_url(self): return self.url
    def get_post(self): return self.url
    def get_put(self): return self.url
    def get_delete(self): return self.url

    def get(self):
        url =self.get_url()
        headers = self.get_headers()
        params = self.get_params()
        auth = self.get_auth()
        return requests.get(url, headers=headers, params=params, auth=auth)
    
    def post(self, json):
        url = self.get_post()
        headers = self.get_headers()
        params = self.get_params()
        auth = self.get_auth()
        return requests.post(url, headers=headers, params=params, auth=auth, json=json)
    
    def put(self, json):
        url = self.get_put()
        headers = self.get_headers()
        params = self.get_params()
        auth = self.get_auth()
        return requests.put(url, headers=headers, params=params, auth=auth, json=json)
    
    def delete(self, pk):
        url =  self.get_delete()
        headers = self.get_headers()
        params = self.get_params()
        auth = self.get_auth()
        return requests.delete(url, headers=headers, params=params, auth=auth)
