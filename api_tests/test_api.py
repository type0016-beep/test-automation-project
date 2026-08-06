import requests

def test_jsonplaceholder_status_code():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200

def test_response_contains_title():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    json_data = response.json()
    assert 'title' in json_data