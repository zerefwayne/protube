from rest_framework.pagination import (
    PageNumberPagination
)


class YoutubeVideoResultsPagination(PageNumberPagination):
    page_size = 5

