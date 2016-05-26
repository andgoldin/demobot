""" Functions for Slack message formatting """

def codeblock(text):
    """ Places the given text in a code block """
    return "```" + text + "```"

def monospace(text):
    """ Formats the given text to have a monospaced font """
    return "`" + text + "`"

def bold(text):
    """ Formats the given text as bold """
    return "*" + text + "*"

def italics(text):
    """ Formats the given text as italicized """
    return "_" + text + "_"

def quote(text):
    """ Places the given text in a quote """
    return ">" + text

def blockquote(text):
    """ Places the given text in a block quote """
    return ">>>" + text

def at(user, text=None):
    """ Prefixes the given text with an @ mention of the given user """
    if text is not None:
        return "<@" + user + ">: " + text
    return "<@" + user + ">"

def truncate(text, limit=50):
    """ Truncates the given string to the length defined by the limit """
    if limit < 3:
        raise ValueError("Truncate limit cannot be less than 3")
    else:
        return text if len(text) <= limit else text[0:limit - 3] + '...'
