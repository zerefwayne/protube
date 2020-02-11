from django.db import models

# Create your models here.

# HTTP Response:
# {
#    "id": {
#     "videoId": "GI2Z53mGIJE"
#    },
#    "snippet": {
#     "publishedAt": "2020-02-11T13:35:08.000Z",
#     "title": "Beyond The Game: Interview with Graham Jones",
#     "description": "Beyond the Game, TRT World's flagship sports show coming to you from gorgeous Malaysia. Robin Adams is there for the annual Tour De Langkawi cycle race.",
#     "thumbnails": {
#      "default": {
#       "url": "https://i.ytimg.com/vi/GI2Z53mGIJE/default.jpg",
#      },
#     },
#     "channelTitle": "TRT World",
#    }
#  }


class Video(models.Model):
    video_id = models.CharField()
    published_at = models.DateTimeField()
    video_title = models.CharField()
    thumbnail_url = models.CharField()
    channel_title = models.CharField()
    added_on = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s titled %s publised on %s added on %s by %s" % (self.video_id, self.video_title, str(self.published_at), str(self.added_on), self.channel_title)

