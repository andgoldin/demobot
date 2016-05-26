# demobot
Demonstraction Slack bot for AppNexus learn &amp; teach

## Setup
* Clone the repository: `git clone https://github.com/andgoldin/demobot.git`
* Install virtualenv: `pip install virtualenv`
* `cd` into repository and run `./bin/setup`. This will set up your virtual environment with all of the dependencies we need to get started.

## Working with git
First make sure you are up to date with master:
* `git checkout master`
* `git pull`

Check out a new branch:
* `git checkout -b MyBranch`

Commit and push your changes:
* `git status` to see what files have been added changed
* `git add filename.py`
* `git status` to make sure your file has been staged for commit
* `git commit -m "commit message"`
* `git push origin MyBranch`

Merge branch into master when changes are ready:
* `git checkout master`
* `git pull`
* `git merge origin/MyBranch`
* `git push origin master`

## Writing a plugin
* Add a Python file to the `/src/plugins` directory
* Include a help string on the first line: `"""!command [<argument>] description"""`
* Include an `on_message` function that returns a string. This string will be the bot's reply for the command:

    ```
    on_message(msg, server):
        # some code
        # parse command input, make api calls, call helper functions, etc
        # create a response string
        return response
    ```

## Testing locally
Simply run the bot in test mode on your command line:
* `./bin/test`

This will let you test your command before you need to commit or push any code.

## Useful stuff
You can get user and message information from the `msg` and `server` objects in your `on_message` function:
* Message text: `msg["text"]`
* User ID: `msg["user"]`
* User name (a bit more complicated): `server.slack.server.users[msg["user"]].name`
* Channel ID: `msg["channel"]`
* Channel name: `server.slack.server.channels[msg["channel"]].name`