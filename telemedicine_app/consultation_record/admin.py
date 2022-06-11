from django.contrib import admin

from consultation_record.models import *

# Register your models here.
admin.site.register(ConsultationRecord)
# admin.site.register(Link)
admin.site.register(Documents)
admin.site.register(RoomMember)
