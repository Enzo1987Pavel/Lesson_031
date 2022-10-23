import pytest

from factories import SelectionFactory, UserFactory, AdsFactory
from users.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from pytest_factoryboy import register


register(UserFactory)
register(AdsFactory)
register(SelectionFactory)


@pytest.fixture
def api_client(db, user):
    # user = User.objects.create_user(
    #     first_name="test_first_name",
    #     last_name="test_last_name",
    #     username="test_username",
    #     # birth_date = models.DateField(verbose_name="Дата рождения", max_length=10, validators=[birth_date_validator])
    #     email="test@test.com",
    #     password="1374SSS"
    # )
    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")
    return client
