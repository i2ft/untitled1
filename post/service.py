from .models import Post

def setDep(instance):

    parentObject = Post.objects.get(title=instance.parent)
    instance.dep = parentObject.dep + 1;
    return 1

def reset_dep(instance):
    if( instance.parent=="NULL"):
        instance.dep=0;

    if(instance.parent!="NULL"):
        instance.dep = Post.objects.get(title=instance.parent).dep + 1;
    list = Post.objects.filter(parent=instance.title);
    instance.save();

    for obj in list:
        reset_dep(obj);



