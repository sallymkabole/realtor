from django.contrib import admin
from .models import Property
from .models import Role
from .models import User
from .models import Letter


# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Letter)
admin.site.register(Property)
