import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

try:
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()  # Ensures HTTP request was successful

    data = response.json()  # Parses the response JSON
    question_data = data.get("results", [])  # Use .get() to avoid KeyError

    if not question_data:
        print("No questions received from API!")
    else:
        print("Questions fetched successfully!")
        print(question_data)  # Print to verify data

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
