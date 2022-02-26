from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Ensure this value contains only letters.')


@deconstructible
class MaxSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.file.size > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB'

# Seems invalid
# def validate_max_file_size(max_size):
#     def validate(value):
#         if value.file.size > max_size * 1024 * 1024:
#             raise ValidationError(f"Max file size is 5.00 MB")