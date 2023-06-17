from django.shortcuts import render
def index(reqest):
    context = {
        'name': "Никита",
    }
    a=reqest.GET.get('fisrt',None)
    context['a']=a
    return render(reqest, 'index.html', context)
# Create your views here.
