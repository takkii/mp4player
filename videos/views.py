from django.shortcuts import render, get_object_or_404
from .models import Video


def video_list(request):
    videos = Video.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'videos/video_list.html', {'videos': videos})


def video_detail(request, id):
    video = get_object_or_404(Video, id=id)
    video.view_count += 1
    video.save()
    return render(request, 'videos/video_detail.html', {'video': video})
