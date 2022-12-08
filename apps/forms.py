from django.forms import CharField, Form


class PositionForm(Form):
    position = CharField(max_length=255)
