from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.template import defaultfilters


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
    start_date = models.DateField(auto_now=True)
    start_time = models.TimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=False,auto_now_add=True)
    parent = models.CharField(blank=True,max_length=40,null=True)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]










def create_slug(instance, new_slug=None):
    slug = defaultfilters.slugify((instance.title))
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)