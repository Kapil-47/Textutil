from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    removespace=request.POST.get('removespace','off')
    removenewline=request.POST.get('removenewline','off')
    count=request.POST.get('count','off')
    removedigits=request.POST.get('removedigits','off')
    capatilizes=request.POST.get('capatilizes','off')

    if removepunc=='on':
        punc='''`~!@#$%^&*(){}[]|\;':"<>?,./'''
        result=""
        for i in djtext:
            if i not in punc:
                result+=i
        param={'choice':'Remove punctuation','result':result}
        return render(request,'analyze.html',param)
    
    elif removespace=='on':
        result=''
        for i in djtext:
            if i!=" ":
                result+=i
        param={'choice':'Remove punctuation','result':result}
        return render(request,'analyze.html',param)
    
    elif removenewline=='on':
        result=''
        for i in djtext:
            if i =='\n' or i=='\r':
               pass
            else:
                result+=i
        
        param={'choice':'Remove punctuation','result':result}
        return render(request,'analyze.html',param)
   
    elif capatilizes=='on':
        result=djtext.upper()
        param={'choice':'Remove punctuation','result':result}
        return render(request,'analyze.html',param)
    
    elif count=='on':
        result=0
        for i in djtext:
            result+=1
        param={'choice':'Remove punctuation','result':result}
        return render(request,'analyze.html',param)

    elif removedigits=='on':
        punc='1234567890'
        result=""
        for i in djtext:
            if i not in punc:
                result+=i
        param={'choice':'Remove punctuation','result':result}
        return render(request,'analyze.html',param)
    else:
        param={'choice':'Not Selected','result':'ERROR !'}
        return render(request,'analyze.html',param)
    