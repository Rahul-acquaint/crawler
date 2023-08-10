from requests_client import RequestsClient, ResposneType
from xanodb import GTMatrixModel

class GTMatrixClient:

    GTMETRIX_API_KEY="091f83815ffede0c83e45bf1762436aa"

    def __init__(self, url) -> None:
        self._url=url
        self._test_url=None


    def set_test_url(self, url):
        self._test_url=url

    def start_test(self) -> dict:
        endpoint =  self._url
        headers = {
            "Content-Type": "application/vnd.api+json"
        }
        auth = (self.GTMETRIX_API_KEY, '') 
        
        data = {
            "data": {
                "type": "test",
                "attributes": {
                    "url":self._url,
                    "adblock":  1
                }
            }
        }
        request_client = RequestsClient(response_type=ResposneType.json)
        response_data = request_client.post(endpoint, headers=headers, auth=auth, json=data)

        if response_data.get("status", False):
            self.set_test_url(response_data.get("links", {}).get("self", None))
            print("setting testing url ==========================>>>>>>")
                

        return response_data

    def get_test(self, site_id):
        assert self._test_url,"did't get test url"

        auth = (self.GTMETRIX_API_KEY, '') 
        request_client = RequestsClient(response_type=ResposneType.json)
        response_data = request_client.get(self._test_url, auth=auth)

        if  response_data.get("status",False):
            response_data= response_data.get("data",{})
            attributes = response_data.get("data",{}).get("attributes",{})

            if attributes.get("state") not in ["started", "error"]:
                attributes["maindb_id"] = site_id
                model = GTMatrixModel()


        return response_data
        



##### testing 
# client = GTMatrixClient("https://youtube.com/")
# client.set_test_url("https://gtmetrix.com/api/2.0/tests/LwSkckKN")
# print("=========================>>>>", client.get_test(1))