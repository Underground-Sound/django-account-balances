from django.apps import apps

from accounts import names

Account = apps.get_model('accounts', 'Account')


def redemptions_account():
    return Account.objects.get(name=names.REDEMPTIONS)


def lapsed_account():
    return Account.objects.get(name=names.LAPSED)
