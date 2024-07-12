from wtforms_formly.fields import HiddenField
from wtforms_formly.form import Form


class F(Form):
    a = HiddenField(default="LE DEFAULT")


def test_hidden_field():
    form = F()
    assert form.a() == """<input id="a" name="a" type="hidden" value="LE DEFAULT">"""
    assert form.a.flags.hidden
