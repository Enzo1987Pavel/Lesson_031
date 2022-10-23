import json

import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_add_ads(api_client, user):
    data = {
        "name": "test_Ads",
        "author": user.id,
        "price": 100
    }

    url = reverse("create_ad")
    res = api_client.post(
        url,
        data=json.dumps(data),
        content_type="application/json",
    )


