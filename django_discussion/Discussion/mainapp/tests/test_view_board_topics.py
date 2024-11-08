from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Category
from ..views import TopicListView


class BoardTopicsTests(TestCase):
    def setUp(self):
        Category.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('category_topics', kwargs={'pk': 1})
        print("url=",url)
        response = self.client.get(url)
        print("response=",response)
        self.assertEqual(response.status_code, 200)
"""
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('category_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/category/1/')
        self.assertEqual(view.func.view_class, TopicListView)

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('category_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
"""