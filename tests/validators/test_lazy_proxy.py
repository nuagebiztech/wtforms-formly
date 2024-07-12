import pytest
from wtforms_formly.validators import (
    NumberRange,
    data_required,
    email,
    equal_to,
    ip_address,
    length,
    regexp,
    url,
)


def test_lazy_proxy_raises(really_lazy_proxy):
    """
    Tests that the validators support lazy translation strings for messages.
    """
    with pytest.raises(
        Exception,
        match=(
            "Translator function called during form declaration: "
            "it should be called at response time."
        ),
    ):
        str(really_lazy_proxy)


def test_lazy_proxy_fixture(really_lazy_proxy):
    """
    Tests that the validators support lazy translation strings for messages.
    """
    equal_to("fieldname", message=really_lazy_proxy)
    length(min=1, message=really_lazy_proxy)
    NumberRange(1, 5, message=really_lazy_proxy)
    data_required(message=really_lazy_proxy)
    regexp(".+", message=really_lazy_proxy)
    email(message=really_lazy_proxy)
    ip_address(message=really_lazy_proxy)
    url(message=really_lazy_proxy)
