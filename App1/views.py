from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='This Data Is Our Assumption'
    d={'Assumption':data}
    return render(request,'data_render1.html',context=d)