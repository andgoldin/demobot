# demobot
Demonstraction Slack bot for AppNexus learn &amp; teach

## Setup
* Clone the repository: `git clone https://github.com/andgoldin/demobot.git`
* Install virtualenv: `pip install virtualenv`
* `cd` into repository and run `./bin/setup`. This will set up your virtual environment with all of the dependencies we need to get started.

## Writing a plugin
* Add a Python file to the `/src/plugins` directory
* Include a help string on the first line: `"""!command [<argument>] description"""`
* Tnclude a function `on_message(msg, server):` that returns a string. This string will be the bot's reply for the command

## Testing locally
Simply run in test mode in your command line: `./bin/test`. This will let you test your command before you need to commit or push any code.

## Useful stuff
You can get user and message information from the `msg` and `server` objects in your `on_message` function:
* Message text: `msg["text"]`
* User ID: `msg["user"]`
* User name (a bit more complicated): `server.slack.server.users[msg["user"]].name`
* Channel ID: `msg["channel"]`
* Channel name: `server.slack.server.channels[msg["channel"]].name`