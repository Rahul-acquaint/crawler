from datetime import datetime
from crawler.apis import APIEndpoints
from crawler.models.abstract_model import AbstractModel
from crawler.debugger import Debugger

class XanoMainDBUpdateModel(AbstractModel):

    url = APIEndpoints.x_maindb

    def update_timespamp(self, data, pk):
        datetime_now = datetime.now()
        format_string = "%Y-%m-%dT%H:%M:%S%z"
        parsed_datetime = datetime.strftime(datetime_now, format_string)
        data["updated_at"]=parsed_datetime
        return self.update(data, pk)

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
