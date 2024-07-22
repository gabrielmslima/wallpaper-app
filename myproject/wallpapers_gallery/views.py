import requests
from django.shortcuts import render

def fetch_images_from_github(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        images_data = response.json()
        images_info = [{'name': img['name'], 'download_url': img['download_url']} for img in images_data]
        return images_info
    return []

def wallpapers_view(request):
    repo_url = "https://api.github.com/repos/gabrielmslima/wallpapers/contents/images"
    images_info = fetch_images_from_github(repo_url)
    context = {'images_info': images_info}
    return render(request, 'wallpapers_gallery/gallery.html', context)