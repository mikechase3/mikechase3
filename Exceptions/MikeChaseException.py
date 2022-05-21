"""
Exceptions for Mike Chase
"""


class MikeChaseException(Exception):
	"""
	Exception that gets thrown when Mike Chase doesn't
	know why he doesn't work.
	"""

	def __init__(self):
		pass

	def __repr__(self):
		return "Mike Chase Exception"


class UserIsStupidException(MikeChaseException):
	"""
	Exception for exceptionally stupid user errors.
	"""
	