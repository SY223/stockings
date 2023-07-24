# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User


# #generate and save token for a user
# def create_auth_token(sender, instance, created=False, **kwargs):
#     if created:
#         token=Token.objects.create(user=instance)
#         token.save()

# post_save.connect(create_auth_token, sender=User)