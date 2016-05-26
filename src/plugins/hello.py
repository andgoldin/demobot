"""!hello says hello"""

def hello(name):
    return "Hello, " + name + "!"

def on_message(msg, server):
    text = msg["text"]
    if text == "!hello":
        username = server.slack.server.users[msg["user"]].name
        return hello(username)