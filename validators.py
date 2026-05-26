import re

class InputValidator:
    @staticmethod
    def is_valid_username(username):
        """ Validate username: 3-20 characters, alphanumeric, underscores """
        pattern = re.compile(r'^[a-zA-Z0-9_]{3,20}$')
        return bool(pattern.match(username))

    @staticmethod
    def is_valid_email(email):
        """ Validate email format """
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com$')
        return bool(pattern.match(email))

    @staticmethod
    def is_valid_password(password):
        """ Validate password: 8-32 characters, at least one upper, one lower, one digit """
        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,32}$')
        return bool(pattern.match(password))

    @staticmethod
    def validate_all(username, email, password):
        return (
            InputValidator.is_valid_username(username) and
            InputValidator.is_valid_email(email) and
            InputValidator.is_valid_password(password)
        )