import requests

# Define the base URL of your API
BASE_URL = 'http://localhost:8000/'  # Update with your API's URL

# Helper function to send requests and print responses
def send_request(method, endpoint, data=None):
    url = BASE_URL + endpoint
    response = None
    
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=data)
    elif method == 'PUT':
        response = requests.put(url, json=data)
    elif method == 'PATCH':
        response = requests.patch(url, json=data)
    elif method == 'DELETE':
        response = requests.delete(url)
    
    if response:
        print(f'{method} {url} - Response Status Code: {response.status_code}')
        if response.status_code != 204:  
            print('Response Body:')
            print(response.json())
    else:
        print(f'Failed to send {method} request to {url}')

# Test Create (POST) operation
create_data = {
    "name": "Salim",
    "age": 30
}
send_request('POST', 'persons/', data=create_data)

# Test Read (GET) operation
send_request('GET', 'persons/3')

# Test Update (PUT) operation
update_data = {
    "name": "Updated Salim",
    "age": 35
}
send_request('PUT', 'persons/3', data=update_data)

# Test Partial Update (PATCH) operation
partial_update_data = {
    "age": 40
}
send_request('PATCH', 'persons/3', data=partial_update_data)

# Test Delete (DELETE) operation
send_request('DELETE', 'persons/3')

print(f'Completed testing for Person ID')
