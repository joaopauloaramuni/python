"""
Search Exceptions
"""


class InvalidBotException(Exception):
    """Raises when asked to run a bot that doesn't exist."""


class GeneralSearchException(Exception):
    """Raises when we could not determine the specific exception."""


class SearchTimeoutException(Exception):
    """Raises when the search reaches it's timeout threshold."""


class HttpResponseException(Exception):
    """Raises when a networking request fails."""


class APIRateLimitException(Exception):
    """Raises when a request fails due to API limitation."""


class ForbiddenException(Exception):
    """Raises when we could not determine the specific exception."""
