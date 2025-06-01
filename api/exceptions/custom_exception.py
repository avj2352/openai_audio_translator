"""
    Consists of a list of
    Custom exceptions
"""

class YoutubeClientException(Exception):
    def __init__(self, message = "ERROR! youtube client exception occurred!"):
        self.message = message
        super().__init__(self.message)

class OpenAIClientException(Exception):
    def __init__(self, message = "ERROR! openai client exception occcurred!"):
        self.message = message
        super().__init__(self.message)
