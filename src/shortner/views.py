from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, render

from .models import ShortURL
from .forms import SubmitURLForm
# Create your views here.


class HomeView(View):
    def get(self, req, *args, **kwargs):
        form = SubmitURLForm()
        context = {
            "title": "Home Page",
            "form" : form
        }
        return render(req, "shortner/home.html", context)

    def post(self, req, *args, **kwargs):
        form = SubmitURLForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
        context = {
            "form": form,
            "title": ""
        }
        return HttpResponse("This is from POST req<br> {i}".format(i=req.POST.get('url')))

def shrink_redirect_view(request, short_code=None, *args, **kwargs):
    # obj = ShortURL.objects.get(short_code=short_code)

    obj = get_object_or_404(ShortURL, short_code= short_code)
    # return HttpResponse("Function-Based-View<br/>URL for that short code: {sc}".format(sc=obj.url))
    return HttpResponseRedirect(obj.url)


class ShrinkRedirectView(View):
    def get(self, request, short_code=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, short_code=short_code)
        # return HttpResponse("Class-Based-View<br/>URL for that short code: {sc}".format(sc=obj.url))
        return HttpResponseRedirect(obj.url)
