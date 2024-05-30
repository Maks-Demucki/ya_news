from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from news.models import News


class TestContent(TestCase):
    HOME_URL = reverse('news:home')

    @classmethod
    def setUpTestData(cls):
        all_news = [
            News(title=f'Новость {index}', text='Просто текст.')
            for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1)
        ]
        News.objects.bulk_create(all_news)

    def test_news_count(self):
        responce = self.client.get(self.HOME_URL)
        object_list = responce.context['object_list']
        news_count = object_list.count()
        self.assertEqual(news_count, settings.NEWS_COUNT_ON_HOME_PAGE)
