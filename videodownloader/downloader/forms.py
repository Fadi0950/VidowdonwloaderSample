from django import forms

class VideoDownloadForm(forms.Form):
    url = forms.URLField(label='Enter YouTube video URL', max_length=200)
