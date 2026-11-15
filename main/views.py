from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect


def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site',default='')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.get_text(strip=True)
            if link_address and link_text:Link.objects.create(address=link_address,name=link_text)

        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    return render(request, 'main/result.html', {'data': data})


def clear(request):
    Link.objects.all().delete()
    return render(request, 'main/result.html')