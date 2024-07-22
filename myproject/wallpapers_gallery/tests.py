from django.test import TestCase

from django.test import TestCase
from django.core.cache import cache
from unittest.mock import patch
from .views import fetch_images_from_github

class FetchImagesFromGitHubTests(TestCase):
    def setUp(self):
        cache.clear()

    @patch('requests.get')
    def test_cache_behavior(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'name': 'image1.jpg', 'download_url': 'http://example.com/image1.jpg'},
            {'name': 'image2.jpg', 'download_url': 'http://example.com/image2.jpg'},
        ]

        repo_url = "https://api.github.com/repos/gabrielmslima/wallpapers/contents/images"
        cache_key = 'github_images_data'

        self.assertIsNone(cache.get(cache_key))

        first_call_result = fetch_images_from_github(repo_url)
        self.assertEqual(len(first_call_result), 2)
        self.assertIsNotNone(cache.get(cache_key))

        second_call_result = fetch_images_from_github(repo_url)
        self.assertEqual(len(second_call_result), 2)
        mock_get.assert_called_once()  # Ensure requests.get was only called once