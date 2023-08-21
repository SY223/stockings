from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.contrib.auth import get_user_model


User = get_user_model()


@receiver(email_confirmed)
def set_user_active(sender, email_address, **kwargs):
    try:
        user = User.objects.get(email=email_address.email)
        user.email_address_verified = True
        user.save()
    except User.DoesNotExist:
        print('User not found')