import pytest
from wtforms_formly import Form, StringField


@pytest.mark.parametrize("exc", [IndexError, ZeroDivisionError, ValueError])
def test_raise_exceptions(exc):
    def validate(form, field):
        raise exc

    class F(Form):
        field = StringField(validators=[validate])

    f = F()

    with pytest.raises(exc):
        f.validate()
