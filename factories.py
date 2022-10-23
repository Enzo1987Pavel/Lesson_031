from datetime import date

import factory
import faker

from ads.models import Selection
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    first_name = "test_first_name",
    last_name = "test_last_name",
    username = "test_username",
    birth_date = factory.Faker("date_field"),
    email = "test@test.com",
    password = "1374SSS"

    class Meta:
        model = User


class AdsFactory(factory.django.DjangoModelFactory):
    name = "test_Ads"
    author = factory.SubFactory(UserFactory)
    price = 1


class SelectionFactory(factory.django.DjangoModelFactory):
    name = "test_name",
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Selection
