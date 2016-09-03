from django.shortcuts import render, get_object_or_404, redirect
from .form import PostForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post

# Create your views here.
def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "form.html", context)



def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	#messages.success(request, "Successfully deleted")
	return redirect("list")

def post_list(request):
    queryset_list = Post.objects.all()  # .order_by("-timestamp")

    context = {
        "object_list":queryset_list,

    }
    return render(request,'list.html',context)


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

