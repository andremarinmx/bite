"""
Author: Óscar Miranda

Functions collection to handle whether login is required or not using Flask.
"""

from flask import session, redirect

class NoDefaultPageError(Exception):
	"""
	Raises when no default page fallback is set in app config.
	"""

class NoSessionNameError(Exception):
	"""
	Raises when the login session name is not set in app config.
	"""

class LoginHandler:
	"""
	Handles whether a route needs the user to be logged in or not.

	Usage:
	```python
	login = LoginHandler(app)
	```
	"""
	def __init__(self, app):
		self.login_required_fallback = app.config.get('LOGIN_REQUIRED_FALLBACK_PAGE')
		self.logout_required_fallback = app.config.get('LOGOUT_REQUIRED_FALLBACK_PAGE')
		self.login_session_name = app.config.get('LOGIN_SESSION_NAME')

		if not self.login_required_fallback:
			raise NoDefaultPageError('LOGIN_REQUIRED_FALLBACK_PAGE is not set in app config.')
		if not self.logout_required_fallback:
			raise NoDefaultPageError('LOGOUT_REQUIRED_FALLBACK_PAGE is not set in app config.')
		if not self.login_session_name:
			raise NoSessionNameError('LOGIN_SESSION_NAME is not set in app config.')

	def login_required(self, function):
		"""
		login_required decorator

		Access to the requested page if the user is logged in, else to the main page.

		Usage:
		```python
		@app.route('<your-route>')
		@login_required
		def function(*args, **kwargs):
			...
		```
		"""
		def wrapper(*args, **kwargs):
			user_id = session.get(self.login_session_name)
			if user_id:
				return function(*args, **kwargs)
			return redirect(self.login_required_fallback)
		# Renaming the function name to avoid duplicates in Flask routes.
		wrapper.__name__ = function.__name__
		return wrapper

	def logout_required(self, function):
		"""
		logout_required decorator

		Redirect to the home page if the user is already logged in.

		Usage:
		```python
		@app.route('<your-route>')
		@logout_required
		def function(*rgs, **kwargs):
			...
		```
		"""
		def wrapper(*args, **kwargs):
			user_id = session.get(self.login_session_name)
			if user_id:
				return redirect(self.logout_required_fallback)
			return function(*args, **kwargs)
		# Renaming the function name to avoid duplicates in Flask routes.
		wrapper.__name__ = function.__name__
		return wrapper
