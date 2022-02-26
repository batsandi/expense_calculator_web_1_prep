from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Ensure this value contains only letters.')


def validate_max_file_size(max_size):
    def validate(value):
        if value.file.size > max_size * 1024 * 1024:
            raise ValidationError(f"Max file size is 5.00 MB")