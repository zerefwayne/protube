from django.db import models


class Video(models.Model):
    video_id = models.CharField(max_length=300)
    published_at = models.DateTimeField()
    video_title = models.CharField(max_length=500)
    thumbnail_url = models.CharField(max_length=500)
    channel_title = models.CharField(max_length=500)
    added_on = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return "%s titled %s published on %s added on %s by %s" % (self.video_id, self.video_title, str(self.published_at), str(self.added_on), self.channel_title)

