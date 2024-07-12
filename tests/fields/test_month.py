from datetime import date

from wtforms_formly.fields import MonthField
from wtforms_formly.form import Form

from tests.common import DummyPostData


class F(Form):
    a = MonthField()
    b = MonthField(format="%m/%Y")


def test_basic():
    d = date(2008, 5, 1)
    form = F(DummyPostData(a=["2008-05"], b=["05/2008"]))

    assert d == form.a.data
    assert "2008-05" == form.a._value()

    assert d == form.b.data


def test_failure():
    form = F(DummyPostData(a=["2008-bb"]))

    assert not form.validate()
    assert 1 == len(form.a.process_errors)
    assert 1 == len(form.a.errors)
    assert "Not a valid date value." == form.a.process_errors[0]
