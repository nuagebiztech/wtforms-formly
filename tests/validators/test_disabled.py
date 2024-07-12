from wtforms_formly import Form, StringField
from wtforms_formly.validators import Disabled

from tests.common import DummyPostData


def test_disabled():
    class F(Form):
        disabled = StringField(validators=[Disabled()])

    form = F(disabled="foobar")
    assert "disabled" in form.disabled.flags
    assert (
        form.disabled()
        == '<input disabled id="disabled" name="disabled" type="text" value="foobar">'
    )
    assert form.validate()

    form = F(DummyPostData(disabled=["foobar"]))
    assert not form.validate()
