from django.db import models


class Post(models.Model):
    title_post = models.CharField(max_length=120)
    text_post = models.TextField()
    date_post = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/')

    def get_summary_text(self):
        return self.text_post[:120]

    def __str__(self):
        return self.title_post
