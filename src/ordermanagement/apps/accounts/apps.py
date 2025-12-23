from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'apps.accounts'
    label = "accounts"

    def ready(self):
        pass
