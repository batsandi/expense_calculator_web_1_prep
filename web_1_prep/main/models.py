from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from web_1_prep.main.validators import validate_only_letters, MaxSizeValidator


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2
    MAX_PHOTO_SIZE = 5
    MIN_BUDGET = 0.0
    IMAGE_UPLOAD_TO = 'PROFILES/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters
        )
    )

    last_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    budget = models.FloatField(
        default=0,
        validators=(
            MinValueValidator(MIN_BUDGET),
        )
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO,
        null=True,
        blank=True,
        # default='staticfiles/images/user.png',
        validators=(
            MaxSizeValidator(MAX_PHOTO_SIZE),
        )
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )

    expense_image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()