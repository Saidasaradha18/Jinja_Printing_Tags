from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='This Data Is Also Our Assumption'
    d={'key':data}
    return render(request,'data_render2.html',context=d)