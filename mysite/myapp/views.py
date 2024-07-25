from django.shortcuts import render
from django.http import HttpResponse
from .models import Chairs, Main_DirChairs, Main_OfficeChairs, Main_OrtChairs, Main_GameChairs
from collections import defaultdict
from django.contrib.auth.decorators import login_required

def CHAIRS(request):
    Items = Chairs.objects.all()
    context={
        "items":Items
    }
    return render(request, 'myapp/gulp/app/chairs.html',context)

#def officeChairs(request):
#    officeItems = OfficeChairs.objects.all()
#    officeId = OfficeChairs.objects.only('id')
#    l=len(officeId)
#    if l%2!=0:
#        lp=len(officeId[:l-2])
#        officeContext = {
#            'officeAppendItems':officeItems[l-1:],
#            'officeCardsCountPrepend':range(0,(lp//2+1)),
#            'officeItems':[],
#        }
#        print(officeContext)
#        lpw=lp
#        oI=officeItems[:l-1]
#        if lpw>2:
#            for i in range(0,lpw-1):
#                p=oI[i*2:(i+1)*2]
#                officeContext['officeItems'].insert(i,p)
#        if lpw<2:
#            for i in range(0,lpw):
#                p=oI[i*2:(i+1)*2]
#                officeContext['officeItems'].insert(i,p)
#
#    elif l%2==0:
#        lp=len(officeId[:l-3])
#        officeContext = {
#            'officeAppendItems':officeItems[l-2:],
#            'officeCardsCountPrepend':range(0,lp//2+1),
#            'officeItems':[],
#        }
#        lpw=lp
#        oI=officeItems[:l-2]
#        if lpw>2:
#            for i in range(0,lpw-1):
#                p=oI[i*2:(i+1)*2]
#                officeContext['officeItems'].insert(i,p)
#        if lpw<2:
#            for i in range(0,lpw):
#                p=oI[i*2:(i+1)*2]
#                officeContext['officeItems'].insert(i,p)
#        
#
#    return officeContext

#def gameChairs(request):
#
#    gameItems = GameChairs.objects.all()
#    gameId = GameChairs.objects.only('id')
#
#    lg=len(gameId)
#    if lg%2!=0:
#        lp=len(gameId[:lg-2])
#        gameContext = {
#            'gameAppendItems':gameItems[lg-1:],
#            'gameCardsCountPrepend':range(0,(lp//2+1)),
#            'gameItems':[],
#        }
#        lpw=lp
#        oI=gameItems[:lg-1]
#        if lpw>2:
#            for i in range(0,lpw-1):
#                p=oI[i*2:(i+1)*2]
#                gameContext['gameItems'].insert(i,p)
#        if lpw<2:
#            for i in range(0,lpw):
#                p=oI[i*2:(i+1)*2]
#                gameContext['gameItems'].insert(i,p)
#
#    elif lg%2==0:
#        lp=len(gameId[:lg-3])
#        gameContext = {
#            'gameAppendItems':gameItems[lg-2:],
#            'gameCardsCountPrepend':range(0,lp//2+1),
#            'gameItems':[],
#        }
#        lpw=lp
#        oI=gameItems[:lg-2]
#        if lpw>2:
#            for i in range(0,lpw-1):
#                p=oI[i*2:(i+1)*2]
#                gameContext['gameItems'].insert(i,p)
#        if lpw<2:
#            for i in range(0,lpw):
#                p=oI[i*2:(i+1)*2]
#                gameContext['gameItems'].insert(i,p)
#
#
#    return gameContext
#
#def ortChairs(request):
#
#    ortItems = OrtChairs.objects.all()
#    ortId = OrtChairs.objects.only('id')
#
#    l=len(ortId)
#    if l%2!=0:
#        lp=len(ortId[:l-2])
#        ortContext = {
#            'ortAppendItems':ortItems[l-1:],
#            'ortCardsCountPrepend':range(0,(lp//2+1)),
#            'ortItems':[],
#        }
#        lpw=lp
#        oI=ortItems[:l-1]
#        if lpw>2:
#            for i in range(0,lpw-1):
#                p=oI[i*2:(i+1)*2]
#                ortContext['ortItems'].insert(i,p)
#        if lpw<2:
#            for i in range(0,lpw):
#                p=oI[i*2:(i+1)*2]
#                ortContext['ortItems'].insert(i,p)
#
#    elif l%2==0:
#        lp=len(ortId[:l-3])
#        ortContext = {
#            'ortAppendItems':ortItems[l-2:],
#            'ortCardsCountPrepend':range(0,lp//2+1),
#            'ortItems':[],
#        }
#        lpw=lp
#        oI=ortItems[:l-2]
#        if lpw>2:
#            for i in range(0,lpw-1):
#                p=oI[i*2:(i+1)*2]
#                ortContext['ortItems'].insert(i,p)
#        if lpw<2:
#            for i in range(0,lpw):
#                p=oI[i*2:(i+1)*2]
#                ortContext['ortItems'].insert(i,p)
#
#
#    return ortContext
#
#def chairs(request):
#    a = officeChairs(request)
#    b = gameChairs(request)
#    c = ortChairs(request)
#    alll = {
#
#    }
#    alll.update(a)
#    alll.update(b)
#    alll.update(c)
#    return render(request, 'myapp/gulp/app/chairs.html', alll)
#
def Main_officeChairs(request):
    officeItems = Main_OfficeChairs.objects.all()
    officeContext = {
        'OfficeItems': officeItems
    }

    return officeContext

def Main_ortChairs(request):
    ortItems = Main_OrtChairs.objects.all()
    ortContext = {
        'OrtItems': ortItems
    }

    return ortContext

def Main_dirChairs(request):
    dirItems = Main_DirChairs.objects.all()
    dirContext = {
        'dirItems': dirItems
    }

    return dirContext

def Main_gameChairs(request):
    gameItems = Main_GameChairs.objects.all()
    gameContext = {
        'gameItems': gameItems
    }

    return gameContext

def index(request):
    a = Main_officeChairs(request)
    b = Main_gameChairs(request)
    c = Main_dirChairs(request)
    d = Main_ortChairs(request)
    main_all = {

    }
    main_all.update(a)
    main_all.update(b)
    main_all.update(c)
    main_all.update(d)

    return render(request, 'myapp/gulp/app/index.html', main_all)

#def OofficeChairs(request):
#    a = officeChairs(request)
#    b = gameChairs(request)
#    c = ortChairs(request)
#    alll = {
#
#    }
#    alll.update(a)
#    alll.update(b)
#    alll.update(c)
#    return render(request, 'myapp/gulp/app/office-chairs.html', alll)
#
#def GgameChairs(request):
#    a = officeChairs(request)
#    b = gameChairs(request)
#    c = ortChairs(request)
#    alll = {
#
#    }
#    alll.update(a)
#    alll.update(b)
#    alll.update(c)
#    return render(request, 'myapp/gulp/app/game-chairs.html', alll)
#
#def OortChairs(request):
#    a = officeChairs(request)
#    b = gameChairs(request)
#    c = ortChairs(request)
#    alll = {
#
#    }
#    alll.update(a)
#    alll.update(b)
#    alll.update(c)
#    return render(request, 'myapp/gulp/app/ort-chairs.html', alll)

@login_required
def profile(request):
    return render(request, 'myapp/gulp/app/profile.html')