![](http://ForTheBadge.com/images/badges/made-with-python.svg)
![](https://forthebadge.com/images/badges/built-by-developers.svg)</br>
[![Prettier](https://img.shields.io/badge/Code%20Style-Prettier-red.svg)](https://github.com/prettier/prettier)
![Size](https://img.shields.io/github/repo-size/Iamtripathisatyam/Slack_Messages?color=red&label=Repo%20Size%20)
![](https://img.shields.io/tokei/lines/github/Iamtripathisatyam/Slack_Messages?color=red&label=Lines%20of%20Code)</br>
![sds](https://profile-counter.glitch.me/{Slack_Messages}/count.svg)

We need to make use of webhooks. You can deliver automatic messages from one app to another using webhooks. When you create an Incoming Webhook, you’ll be given a unique URL to which you may send a JSON payload including the message text and some parameters.

### Setup: 
Create a Slack Workspace [**here**](https://slack.com/get-started#/create) and create your own app.
- Go to Browse Slack
- Select Apps
- A new window will appear. From there select App Directory
- Now select Build
- Again a new window will open up, select create an app
- Select from scratch
- Set app name and workspace
- Then create app
- Select Incoming Webhooks
- Turn activate incoming webhooks on and add new webhook to workspace
- Select a bot and give it allow access
- Copy the webhook URL as this will be used later

Now that we’ve created the app and obtained the webhook URL, it’s time to start coding.

### Sending Messages: 

We first have to import all the required modules. Now, get your webhook URL and save it to the variable. In a variable, save the message and title you want to send.

Now it’s time to make all the slack data we want to send. It consists of your username and in the  Attachment section we have:

- The color you want to choose.
- Fields consist of the following things:
  - Title of our message.
  - The message we want to send.
  - Short means, display message should be of sort type or long type.

Now with the use of the sys module, we will get the size of the slack data and store it in a variable. Now for headers, we will define the Content-Type and Content-Length. Use the post method of requests module to post all, the data after dumping it using the dumps function of json module. At last, check whether the response is valid or not with the use of a status code.

### Output: 
<p align="center"><img width="80%" src="https://user-images.githubusercontent.com/69134468/129148686-9884b0ac-19c5-4324-8f70-f4342bf1a808.png"></p>
