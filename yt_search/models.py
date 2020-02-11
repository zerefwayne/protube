from django.db import models


class YoutubeVideo(models.Model):

    videoId = models.CharField(max_length=128, primary_key=True)
    publishedAt = models.DateTimeField()
    videoTitle = models.CharField(max_length=500)
    thumbnailUrl = models.CharField(max_length=500)
    channelTitle = models.CharField(max_length=500)
    addedOn = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return "%s titled %s published on %s added on %s by %s" % (self.videoId, self.videoTitle, str(self.publishedAt), str(self.addedOn), self.channelTitle)

