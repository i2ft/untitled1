from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request,'list.html',{})
def post_detail(request):
    return render(request,'detail.html',{})
def post_create(request):
    return render(request,'form.html',{})

