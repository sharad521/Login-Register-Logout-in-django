from django.contrib import admin

# Register your models here.

from .models import Feature
# Register your models here.
admin.site.register(Feature)

from .models import Feature1
admin.site.register(Feature1)

from .models import Feature2
admin.site.register(Feature2)

