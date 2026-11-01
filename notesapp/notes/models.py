from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # flaw A02 Cryptographic Failures: the note text is stored in plaintext in the database,
    # problem: anyone who can read db.sqlite3 can read every user's notes.
    # how to fix the flaw: use an encrypted field by adding on the top of this file:
    #   from encrypted_model_fields.fields import EncryptedCharField
    # and then change the text field to:
    #   text = EncryptedCharField(max_length=200)
    # and put FIELD_ENCRYPTION_KEY in settings.py.
    text = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text