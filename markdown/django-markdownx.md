`pip install django-markdownx`

    INSTALLED_APPS = (
        [...]
        'markdownx',
    )
    
    urlpatterns = [
        [...]
     
        url(r'^markdownx/', include('markdownx.urls')),
    ]
    
    
   `python manage.py collectstatic`
   
   Model

#models.py
    from markdownx.models import MarkdownxField
    
    class MyModel(models.Model):
    
        myfield = MarkdownxField()
...and then, include a form's required media in the template using {{ form.media }}:


