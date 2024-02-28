import os
from django.conf import settings
from django.shortcuts import render
from .forms import VideoDownloadForm
from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_extension = 'mp4'  # Default file extension
        if stream.mime_type == 'video/mp4':
            file_extension = 'mp4'
        elif stream.mime_type == 'video/x-matroska':
            file_extension = 'mkv'
        file_path = os.path.join(settings.MEDIA_ROOT, yt.title + '.' + file_extension)
        stream.download(output_path=settings.MEDIA_ROOT, filename=yt.title)
        return file_path
    except Exception as e:
        print("Error:", str(e))
        return None


def download_video_view(request):
    if request.method == 'POST':
        form = VideoDownloadForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            file_path = download_video(url)
            if file_path:
                return render(request, 'downloader/download_success.html', {'file_path': file_path})
            else:
                return render(request, 'downloader/download_failed.html')
    else:
        form = VideoDownloadForm()
    return render(request, 'downloader/download_form.html', {'form': form})
