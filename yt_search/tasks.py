from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from datetime import timedelta
import datetime
import requests
from .models import YoutubeVideo

logger = get_task_logger(__name__)

# {
#   id: {
#       videoId: "9Q9GP5I0q2U"
#   },
#   snippet: {
#       publishedAt: "2020-02-11T18:27:00.000Z",
#       title: "Darren Jackson: My Thoughts Are With Jackie - The Football Show - Tue 11th Feb 2020.",
#       description: "SUBSCRIBE HERE ➡️: https://bit.ly/2wbYWiG With Arnold Clark Visit us on: http://plzsoccer.com Follow us on Twitter: @plzsoccer Like us on Facebook: ...",
#       thumbnails: {
#           default: {
#               url: "https://i.ytimg.com/vi/9Q9GP5I0q2U/default.jpg",
#           },
#       },
#       channelTitle: "PLZ Soccer - The Football Show",
#   }
# },


# {'error': {'errors': [{'domain': 'usageLimits', 'reason': 'dailyLimitExceeded', 'message': 'Daily Limit Exceeded. The quota will be reset at midnight Pacific Time (PT). You may monitor your quota usage and adjust limits in the API Console: https://console.developers.google.com/apis/api/youtube.googleapis.com/quotas?project=229626395005', 'extendedHelp': 'https://console.developers.google.com/apis/api/youtube.googleapis.com/quotas?project=229626395005'}], 'code': 403, 'message': 'Daily Limit Exceeded. The quota will be reset at midnight Pacific Time (PT). You may monitor your quota usage and adjust limits in the API Console: https://console.developers.google.com/apis/api/youtube.googleapis.com/quotas?project=229626395005'}}

URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&order=date&q=football&regionCode=IN&type=video&key=AIzaSyC-CqA46hfh4_3vzFR772sy8JCelAnFy2w"


@periodic_task(run_every=(timedelta(minutes=1)), name="fetch_youtube_data", ignore_result=True)
def fetch_youtube_data():

    r = requests.get(url=URL)
    data = r.json()

    if data['items']:

        number_of_videos_found = len(data['items'])

        for i in range(number_of_videos_found):

            video = data['items'][i]

            new_model = YoutubeVideo(videoId=video['id']['videoId'], publishedAt=video['snippet']['publishedAt'], videoTitle=video['snippet']['title'], description = video['snippet']['description'], thumbnailUrl=video['snippet']['thumbnails']['default']['url'], channelTitle=video['snippet']['channelTitle'], addedOn=datetime.datetime.utcnow().isoformat())

            new_model.save()

    elif data['error']:
        return data['error']['errors'][0]['message']
