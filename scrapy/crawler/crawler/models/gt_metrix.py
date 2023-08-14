from crawler.apis import APIEndpoints
from crawler.models.abstract_model import AbstractModel
from crawler.debugger import Debugger
from crawler import configs


class AbstractGTMatrix:

    def get_auth(self):
        auth = (configs.GTMETRIX_API_KEY, '')
        return auth
        
class GTMetrixModel(AbstractGTMatrix, AbstractModel):

    url=APIEndpoints.gtmatrix


    def get_headers(self):
        headers = {"Content-Type": "application/vnd.api+json"}
        return headers

    def post(self, json):
        response = super().post(json)
        data = response.json()
        if response.status_code == 202:
            return data

        Debugger.error("error ", data, response.url)

        return None
    


class GTMetrixTestModel(AbstractGTMatrix, AbstractModel):


    def get(self):
        response = super().get()
        data = response.json()
        if response.status_code == 200:
            return data

        Debugger.error("error ", data, response.url)

        return None








# gtmatrix_model = GTMatrixModel()
# gtmatrix_model


