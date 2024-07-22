import requests
from django.shortcuts import render
from django.core.cache import cache
from django.core.paginator import Paginator

def fetch_images_from_github(repo_url):
    # Try to get cached data
    cache_key = 'github_images_data'
    images_info = cache.get(cache_key)

    if not images_info:
        response = requests.get(repo_url)
        if response.status_code == 200:
            images_data = response.json()
            images_info = [{'name': img['name'], 'download_url': img['download_url']} for img in images_data]
            cache.set(cache_key, images_info, 3600)
        else:
            images_info = []

    return images_info

def wallpapers_view(request):
    images_info = fetch_images_from_github("https://api.github.com/repos/gabrielmslima/wallpapers/contents/images")
    
    paginator = Paginator(images_info, 36)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'wallpapers_gallery/gallery.html', {'page_obj': page_obj})