from .models import Post

def setDep(instance):

    parentObject = Post.objects.get(name=instance.parent)
    instance.dep = parentObject.dep + 1;
    return 1