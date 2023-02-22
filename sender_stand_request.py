import configuration
import data
import requests

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=data.kit_body,
                         headers=data.kit_headers)
response = post_new_client_kit(data.kit_body);
print(response.json())


