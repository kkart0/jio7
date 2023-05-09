from django.shortcuts import render,HttpResponse
from .models import Musiclist
from math import *

# Create your views here.
def index(request):
    song=Musiclist.objects.all()
    print(song)
    n=len(song)
    nSlides=n//4+ceil((n/4)-(n//4))
    params={"no_of_slides":nSlides,'range':range(1,nSlides),'songs':song}
    
    # allProd=[]
    # timeprod=Musiclist.objects.values('song_date')
    # times={item['song_date'] for item in timeprod}
    # for t in times:
    #     prod=Musiclist.objects.filter(song_date=t)
    #     n=len(prod)
    #     nSlides=n//4+ceil((n/4)-(n//4))
    #     allProd.append([prod,range(1,nSlides),nSlides])
    # params={"allProd":allProd}

    return render(request,"index.html",params)
