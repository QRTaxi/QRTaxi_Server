from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    # All drivers
    def create_user(self, username, password=None, **extra_fields):

        if username is None:
            raise TypeError('Drivers must have a username.')

        if password is None:
            raise TypeError('Drivers must have a password.')

        user = self.model(
        username = username,
        **extra_fields
        )

        user.set_password(password)
        user.save()

        return user

    # admin user
    def create_superuser(self, username, password, **extra_fields):

        user = self.create_user(username, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user