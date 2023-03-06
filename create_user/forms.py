from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

ADMIN = 1
VIP = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIP, "VIP"),
    (CLIENT, "CLIENT"),
)

MALE = 1
FEMALE = 2
SOMETHING_WRONG = 3

GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (SOMETHING_WRONG, "DIDN'T CHOOSE"),
)

STRAIGHT = 1
WRONG_MAN = 2
WRONG_WOMAN = 3

ORIENTATION = (
    (STRAIGHT, 'STRAIGHT'),
    (WRONG_MAN, 'GAY'),
    (WRONG_WOMAN, 'LESBIAN'),
)

YES = 1
OF_COURCE_YES = 2
ABSOLUTELY_CORRECT = 3
YES_OF_COURCE_IT_IS_ABSOLUTELY_CORRECT = 4

DUMP_TYPE = (
    (YES, 'YES!'),
    (OF_COURCE_YES, 'OF COURCE YES!'),
    (ABSOLUTELY_CORRECT, 'ABSOLUTELY CORRECT!'),
    (YES_OF_COURCE_IT_IS_ABSOLUTELY_CORRECT, 'YES OF COURCE IT IS ABSOLUTELY CORRECT!'),
)

MARRIED = 1
FREE = 2

MARRY_TYPE = (
    (MARRIED, 'MARRIED'),
    (FREE, 'SINGLE'),
)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    birthday = forms.CharField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    orientation = forms.ChoiceField(choices=ORIENTATION, required=True)
    dump = forms.ChoiceField(choices=DUMP_TYPE, required=True)
    favorite_anime = forms.CharField(required=True)
    marry = forms.ChoiceField(choices=MARRY_TYPE, required=True)
    city = forms.CharField(required=True)
    password_for_admins = forms.CharField(required=False)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
            "birthday",
            "user_type",
            "gender",
            "orientation",
            "dump",
            "favorite_anime",
            "marry",
            "city",
            "password_for_admins",
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
