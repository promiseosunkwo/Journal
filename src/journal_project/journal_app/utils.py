from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db.models.fields import DateTimeField
import six
from .models import my_user

My_user = my_user()
# timestamps = my_user.timestamp

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk)+six.text_type(my_user.timestamp)+six.text_type(my_user.is_email_verified))

    
generate_token = TokenGenerator()