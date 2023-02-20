from django.contrib import admin
from soesite.models import  branch
from soesite.models import  subject
from soesite.models import  resource
from soesite.models import review
admin.site.register(branch)
admin.site.register(subject)
admin.site.register(resource)
admin.site.register(review)
# Register your models here.
