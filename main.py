# Import the following modules
import json
import sys
import requests

if __name__ == '__main__':
	# Webhooks URL
	url = "https://hooks.slack.com/services/xxxyyyzzz"
	
	# Message you wanna send
	message = (
		"Hi there!, GeeksforGeeks is the Best Learning Platform\
		for Computer Science Students")
	
	# Title
	title = (f"GeeksforGeeks Bot :satellite:")
	
	# All slack data
	slack_data = {

		"username": "Testing",
		"attachments": [
			{
				"color": "#FF0000",
				"fields": [
					{
						"title": title,
						"value": message,
						"short": "false",

					}
				]
			}
		]
	}
	
	# Size of the slack data
	byte_length = str(sys.getsizeof(slack_data))
	headers = {'Content-Type': "application/json",
			'Content-Length': byte_length}
	
	# Posting requests after dumping the slack data
	response = requests.post(url, data=json.dumps(slack_data), headers=headers)
	
	# Post request is valid or not!
	if response.status_code != 200:
		raise Exception(response.status_code, response.text)
