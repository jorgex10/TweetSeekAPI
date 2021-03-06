from django.db import models
from django.contrib.auth.models import User

class DetailUser(models.Model):
	twitter_token = models.CharField(max_length = 50)
	location = models.CharField(max_length = 100, null = True, blank = True)
	description = models.TextField(default = '', null = True, blank = True)
	enabled = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now = True)
	user = models.OneToOneField(User, null = False, blank = False, on_delete = models.CASCADE)

	class Meta:
		verbose_name = "DetailUser"
		verbose_name_plural = "DetailUsers"

	def __str__(self):
		return '%s %s' % (self.user.first_name, self.user.last_name)