from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.core.cache import cache
from unittest.mock import patch
from .views import fetch_images_from_github

class FetchImagesFromGitHubTests(TestCase):
    def setUp(self):
        # Clear the cache before each test
        cache.clear()

    @patch('requests.get')
    def test_cache_behavior(self, mock_get):
        # Mock the response from requests.get
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'name': 'image1.jpg', 'download_url': 'http://example.com/image1.jpg'},
            {'name': 'image2.jpg', 'download_url': 'http://example.com/image2.jpg'},
        ]

        repo_url = "https://api.github.com/repos/gabrielmslima/wallpapers/contents/images"
        cache_key = 'github_images_data'

        # Ensure cache is empty initially
        self.assertIsNone(cache.get(cache_key))

        # Call the function for the first time, should populate the cache
        first_call_result = fetch_images_from_github(repo_url)
        self.assertEqual(len(first_call_result), 2)
        self.assertIsNotNone(cache.get(cache_key))

        # Call the function again, should use the cache (mock_get is not called again)
        second_call_result = fetch_images_from_github(repo_url)
        self.assertEqual(len(second_call_result), 2)
        mock_get.assert_called_once()  # Ensure requests.get was only called once