import requests
from django.shortcuts import render

def fetch_images_from_github(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        return response.json()
    return []

def wallpapers_view(request):
    repo_url = "https://api.github.com/repos/gabrielmslima/wallpapers/contents/images"
    images = fetch_images_from_github(repo_url)
    context = {'images': images}
    return render(request, 'wallpapers_gallery/gallery.html', context)