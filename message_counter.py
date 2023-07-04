import requests
import json
import datetime

url = "https://getcody.ai/api/v1/messages"
headers = {
    "Authorization": "Bearer xxxxxxxxxxxxxxxx",
    "Content-Type": "application/json"
}
body = {
    "bot_id": "xxxx"
}

# Initialize the counts to 0
questions = 0
answers = 0
total_questions = 0
total_answers = 0

# Set the reference date as July 1, 2023
reference_date = datetime.datetime(2023, 7, 1)
# Convert it to Unix Timestamp
reference_timestamp = reference_date.timestamp()

# First request to get the total number of pages
response = requests.get(url, headers=headers, json=body)
data = response.json()

total_pages = data['meta']['pagination']['total_pages']

# Iterate through all pages
for page in range(1, total_pages + 1):
    params = {'page': page}
    response = requests.get(url, headers=headers, params=params, json=body)
    data = response.json()

    # Iterate through the response data
    for item in data['data']:
        # Count all questions and answers
        if not item['machine']:
            total_questions += 1
        elif item['machine']:
            total_answers += 1

        # Only consider the message for the other count if the creation date is later than the reference date
        if item['created_at'] > reference_timestamp:
            if not item['machine']:
                questions += 1
            elif item['machine']:
                answers += 1

    # Print the current page and the total pages
    print(f"{page} out of {total_pages} pages calculated")

    # Print the current count of questions and answers
    print("Questions so far: ", questions)
    print("Answers so far: ", answers)
    print("Total questions so far: ", total_questions)
    print("Total answers so far: ", total_answers)
    print("------------------------")

# Print the total number of questions and answers
print("Total Questions: ", questions)
print("Total Answers: ", answers)
print("Total Questions (regardless of timestamp): ", total_questions)
print("Total Answers (regardless of timestamp): ", total_answers)
