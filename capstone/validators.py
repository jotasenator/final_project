from django.core.exceptions import ValidationError


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not any(char.isupper() for char in password):
            raise ValidationError(
                ("The password must contain at least 1 uppercase letter."),
                code="password_no_upper",
            )

        if not any(char in "!@#$%^&*()_+-/\\?" for char in password):
            raise ValidationError(
                ("The password must contain at least 1 symbol."),
                code="password_no_symbol",
            )
