from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from celery.task import PeriodicTask
from datetime import timedelta
import datetime
import requests
from .models import YoutubeVideo
from api_manager.models import APIKey

logger = get_task_logger(__name__)

search_topic = "cricket"

URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&order=date&q="+search_topic+"&regionCode=IN&type=video&key="


def generate_new_api_key():
    new_api_key = APIKey.objects.filter(exhausted=False)

    if new_api_key:
        return {'success': True, 'data': new_api_key[0]}
    else:
        return {'success': False}


@periodic_task(run_every=(timedelta(seconds=10)), name="fetch_youtube_data", ignore_result=True)
def fetch_youtube_data():

    api_key = generate_new_api_key()

    if api_key['success']:

        complete_url = URL + str(api_key['data'])

        r = requests.get(url=complete_url)
        data = r.json()

        if data['items']:

            number_of_videos_found = len(data['items'])

            for i in range(number_of_videos_found):

                video = data['items'][i]

                new_model = YoutubeVideo(videoId=video['id']['videoId'], publishedAt=video['snippet']['publishedAt'], videoTitle=video['snippet']['title'], description = video['snippet']['description'], thumbnailUrl=video['snippet']['thumbnails']['default']['url'], channelTitle=video['snippet']['channelTitle'], addedOn=datetime.datetime.utcnow().isoformat())

                new_model.save()

        elif data['error']:

            APIKey.objects.filter(api_key=api_key).update(exhausted=True)
            fetch_youtube_data()

    else:

        task = PeriodicTask.objects.get(name="fetch_youtube_data")
        task.delete()
        return dict({'error': "No API Key Found. Please supply a new one."})

