from wtforms_formly.fields import SubmitField
from wtforms_formly.form import Form


class F(Form):
    a = SubmitField("Label")


def test_submit_field():
    assert F().a() == """<input id="a" name="a" type="submit" value="Label">"""
