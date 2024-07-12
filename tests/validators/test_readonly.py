from wtforms_formly import Form, StringField
from wtforms_formly.validators import readonly

from tests.common import DummyPostData


def test_readonly():
    class F(Form):
        ro = StringField(validators=[readonly()])

    form = F(ro="foobar")
    assert "readonly" in form.ro.flags
    assert form.ro() == '<input id="ro" name="ro" readonly type="text" value="foobar">'
    assert form.validate()

    form = F(DummyPostData(ro=["foobar"]), data={"ro": "foobar"})
    assert form.validate()

    form = F(DummyPostData(ro=["foobar"]), data={"ro": "foobarbaz"})
    assert not form.validate()

    form = F(DummyPostData(ro=["foobar"]))
    assert not form.validate()


def test_readonly_with_default():
    class F(Form):
        ro = StringField(validators=[readonly()], default="foobar")

    form = F(DummyPostData(ro=["foobar"]))
    assert form.validate()

    form = F(DummyPostData(ro=["foobar"]), data={"ro": "foobarbaz"})
    assert not form.validate()

    form = F(DummyPostData(ro=["foobarbaz"]), data={"ro": "foobarbaz"})
    assert form.validate()
