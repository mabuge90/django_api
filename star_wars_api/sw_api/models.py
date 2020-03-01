from django.db import models

# Create your models here.
class Character(models.Model):
	name = models.CharField(max_length=255, blank=False, unique=True)

	def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)