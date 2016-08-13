from django.shortcuts import render, get_object_or_404, redirect
from .form import PostForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post

# Create your views here.
def post_update(request):
    return render(request,'list.html',{})
def post_delete(request):
    return render(request,'list.html',{})

def post_list(request):
    return render(request,'list.html',{})


def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	share_string = instance.content
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "detail.html", context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)

        instance.user = request.user
        instance.save()
        # message success
        #messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render(request,'form.html',context)

