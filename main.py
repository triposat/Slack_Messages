# Import the following modules
import json
import sys
import requests
import os
import github

# extracting all the input from environments
url = os.environ['INPUT_URL']
message = os.environ['INPUT_MESSAGE']
title = os.environ['INPUT_TITLE']



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

def send_message(url,title,slack_data,):

    # Size of the slack data
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json",
               'Content-Length': byte_length}

    # Posting requests after dumping the slack data
    response = requests.post(url, data=json.dumps(slack_data),headers=headers)

    # Post request is valid or not!
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

def main():
	send_message(url,title,slack_data)


if __name__ == '__main__':
	main()
