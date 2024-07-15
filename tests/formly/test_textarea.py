"""

@Filename : test_textarea
@created :  Jul 12 15:02 2024
@project: wtforms_formly
@author : pritam
"""

import validators
from wtforms_formly.fields import TextAreaField
from wtforms_formly.form import Form


class F(Form):
    a = TextAreaField(
        name="TextArea",
        default="LE DEFAULT",
        label="Text Area",
        description="Description",
        validators=[validators.data_required()],
        _json=True,
        render_kw={
            "placeholder": "Placeholder",
        },
    )


def test_textarea_field():
    form = F()
    """
    Sample TextArea from formly.dev
    {
      key: 'Textarea',
      type: 'textarea',
      props: {
        label: 'Textarea',
        placeholder: 'Placeholder',
        description: 'Description',
        required: true,
      },
    }
    {
  key: 'comments',
  type: 'textarea',
  props: {
    label: 'Comments',
    placeholder: 'Enter your comments',
    required: true,
    rows: 4,
    cols: 50,
  },
}
    """
    assert form.a() == {
        "key": "TextArea",
        "type": "textarea",
        "props": {
            "label": "Text Area",
            "placeholder": "Placeholder",
            "description": "Description",
            "required": True,
            "defaultValue": "LE DEFAULT",
        },
    }
