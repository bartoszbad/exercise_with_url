from django.forms import ModelForm, forms

from shortening_urls.models import Url


class UrlForm(ModelForm):

    class Meta:
        model = Url
        fields = ["url"]

    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields["url"].label = "Wstaw URL, który chcesz skrócić"
        self.fields["url"].widget.attrs['placeholder'] = "http..."
