import short_url
from django.shortcuts import render, redirect
from django.views import View
from recruitment_task.forms import UrlForm
from recruitment_task.models import Url


class LandingPageView(View):
    def get(self, request):
        form = UrlForm()
        return render(request, "landing_page.html", context={"form": form})

    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            new_url = Url.objects.create(url=url)
            new_url.shorten_url = short_url.encode_url(new_url.id)
            new_url.save()
            return redirect(f'shorter_url/{new_url.shorten_url}')
        return render(request, "landing_page.html", context={"form": form})


class ShorterUrlView(View):
    def get(self, request, link):
        return render(request, "shorter_url.html", context={"shorter_link": link})


class YourShorterUrlView(View):
    def get(self, request, link):
        your_url = Url.objects.get(shorten_url=link)
        return redirect(your_url.url)



