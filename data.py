import requests


parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
json_data = response.json()
question_data = json_data["results"]
