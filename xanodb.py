from requests_client import RequestsClient, ResposneType
from api_lists import APIEndpoint

class GTMatrixModel:

    endpoint=APIEndpoint.x_gtmatrix


    def post(self, inputs:dict) -> None:
        data={
            "gtmetrix_grade" : inputs.get("gtmetrix_grade"),
            "performance_score" : inputs.get("performance_score"),
            "structure_score" : inputs.get("structure_score"),
            "largest_contentful_paint" : inputs.get("largest_contentful_paint"),
            "total_blocking_time" : inputs.get("total_blocking_time"),
            "cumulative_layout_shift" : inputs.get("cumulative_layout_shift"),
            "maindb_id" : 1,
        }

        print("posting these data ==============================>>>", data)
        request_client = RequestsClient(response_type=ResposneType.json)
        response_data = request_client.post(self.endpoint, json=data)

################## TESTING
# data={
#     "gtmetrix_grade" : "B",
#     "performance_score" : 100,
#     "structure_score" : 100,
#     "largest_contentful_paint" : 100,
#     "total_blocking_time" : 100,
#     "cumulative_layout_shift" : 100,
#     "maindb_id" : 1,
# }

# model =  GTMatrixModel()
# print(model.post(data))