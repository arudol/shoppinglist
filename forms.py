from wtforms import Form, StringField, validators

class InputForm(Form):
    item = StringField('Was?', [validators.Length(min=2, max=25)])
    shop = StringField('Welcher Laden?', [validators.Length(min=0, max=25)])
    comment = StringField('Kommentar', [validators.Length(min=0, max=25)])


class RemoveForm(Form):
    item = StringField('Was?', [validators.Length(min=0, max=25)])
    shop = StringField('Welcher Laden?', [validators.Length(min=0, max=25)])
