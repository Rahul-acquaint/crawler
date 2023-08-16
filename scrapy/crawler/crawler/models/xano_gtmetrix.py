from crawler.apis import APIEndpoints

from crawler.models.abstract_model import AbstractModel
from crawler.debugger import Debugger

class XanoGTMetrixModel(AbstractModel):

    url = APIEndpoints.x_gtmatrix

    def add(self, data):

        response = self.post(data)
        data = response.json()
        if response.status_code == 200:...
        else:
            Debugger.error("error ", data)

class XanoGTMetrixUpdateModel(AbstractModel):

    url = APIEndpoints.x_gtmatrix

    def update(self, data, pk):
        self.pk=pk
        response = self.post(data)
        data = response.json()
        if response.status_code == 200:...
        else:
            Debugger.error("error ", data)

    def get_post(self):
        url = f"{self.url}/{self.pk}"
        return url



