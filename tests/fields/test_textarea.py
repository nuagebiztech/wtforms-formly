from wtforms_formly.fields import TextAreaField
from wtforms_formly.form import Form


class F(Form):
    a = TextAreaField(default="LE DEFAULT")


def test_textarea_field():
    form = F()
    assert form.a() == """<textarea id="a" name="a">\r\nLE DEFAULT</textarea>"""
