"""
Http Exceptions
"""


class HttpClientException(Exception):
    """Raises when an error occurs while doing a networking request."""


class GeneralHttpClientException(Exception):
    """Raises when an unexpected error occurs while doing a networking request."""
