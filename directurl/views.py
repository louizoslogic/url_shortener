from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Url
import zlib


def index(request):

    # return render(request, 'directurl/index.html')
    url = Url.objects.all()
    # I think I'm supposed to put the model.Urls here shown below
    context = {
        'urls': url
    }
    return render(request, 'directurl/index.html', context)


def hash_url(direct_url):

    byte_str = bytes(direct_url, 'utf8')  # hash
    hash_code = zlib.adler32(byte_str)  # hash
    return hash_code


def save(request):
    # Pulling input from INDEX
    data = request.POST

    print(data)

    direct_url = data["actual"]

    url = Url(direct=direct_url, hashed=hash_url(direct_url))

    url.save()

    return HttpResponseRedirect(reverse('directurl:index'))


def send_to(request, hashed):
    obj = get_object_or_404(Url, hashed=hashed)
    return HttpResponseRedirect(obj.direct)
# is that http redirect right?
