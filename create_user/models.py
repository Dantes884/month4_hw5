from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIP = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIP, 'VIP'),
    (CLIENT, 'CLIENT'),
)

MALE = 1
FEMALE = 2
SOMETHING_WRONG = 3

GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
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


class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя')
    phone_number = models.CharField('номер телефона', max_length=25)
    birthday = models.CharField('дата рождения', max_length=30)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Пол')
    orientation = models.IntegerField(choices=ORIENTATION, verbose_name='Ориентация')
    dump = models.IntegerField(choices=DUMP_TYPE, verbose_name='Вы глупы?')
    favorite_anime = models.CharField('Любимое аниме', max_length=45)
    marry = models.IntegerField(verbose_name='Семейное положение', choices=MARRY_TYPE)
    city = models.CharField('Город', max_length=40)
    password_for_admins = models.CharField(
        'Введите ещё раз пароль, что бы мы знали что вы его ещё помните',
        max_length=50
    )
