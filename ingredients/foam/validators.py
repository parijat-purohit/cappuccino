from django.core.exceptions import ValidationError
import re


class DigitValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'The password must contain at least one digit.')

    def get_help_text(self):
        return 'Your password must contain at least one digit.'


class UppercaseLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isupper() for char in password):
            raise ValidationError(
                'The password must contain at least one uppercase letter.')

    def get_help_text(self):
        return 'Your password must contain at least one uppercase letter.'


class LowercaseLetterValidator:
    def validate(self, password, user=None):
        if not any(char.islower() for char in password):
            raise ValidationError(
                'The password must contain at least one lowercase letter.')

    def get_help_text(self):
        return 'Your password must contain at least one lowercase letter.'


class SpecialCharacterValidator:
    def validate(self, password, user=None):
        if not re.search(r"[^\w\s]", password):
            raise ValidationError(
                'The password must contain at least one special symbol.')

    def get_help_text(self):
        return 'Your password must contain at least one special symbol (e.g., !, @, #, $).'
