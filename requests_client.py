import requests 


class ResposneType:
    json="json"
    text="text"
    
    @classmethod
    def to_convert(cls, repsonse_type, response):
        
        #JSON
        if repsonse_type == cls.json: return response.json()

        return  response.text


class RequestsClient:

    def __init__(self, response_type:str=ResposneType.text) -> None:
        self.response_type= response_type
        self.response=None
    

    def get_response(self):
        return self.response
    
    def set_response(self, response):
        self.response=response
        return response
    
    
    def is_valid_status_code(self, code):

        if code >= 200 and code <= 226: return True      
        return False

    def validate(self, response, response_data) -> dict:
        
        status = self.is_valid_status_code(response.status_code)

        return { 
                "status":status,
                "data":response_data
                }

    def get_response_type(self):return self.response_type

    def get_to_convert(self,  response_type, response):
        response_data =  ResposneType.to_convert(response_type, response)
        if response_type == ResposneType.json:
            return self.validate(response, response_data)
        return response_data
    

    def get(self, url, params={}, **kwargs):

        response =  requests.get( url, params=params, **kwargs)
        self.set_response(response)
        response_type =self.get_response_type()
        response_data = self.get_to_convert(response_type, response)
        return response_data
    
    def post(self, url, **kwargs):

        response =  requests.post( url, **kwargs)
        self.set_response(response)
        response_type =self.get_response_type()
        response_data = self.get_to_convert(response_type, response)
        return response_data
    
    def delete(self, url, **kwargs):
        
        response =  requests.delete( url, **kwargs)
        self.set_response(response)
        response_type =self.get_response_type()
        response_data = self.get_to_convert(response_type, response)
        return response_data
    
    def put(self, url, **kwargs):
        
        response =  requests.put( url, **kwargs)
        self.set_response(response)
        response_type =self.get_response_type()
        response_data = self.get_to_convert(response_type, response)
        return response_data
        

