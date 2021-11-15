from django.contrib import admin
from .models import Event


# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'Event_Name', 'Venue',
                    'Date_of_event')
    list_filter = ('Event_Name', 'Venue', 'Date_of_event')
    fieldsets = (
        ('More Info', {
            'fields': ('Event_Name', 'Venue', 'Date_of_event', 'Event_details')
        }),


        ('Event Admin', {

            'fields': ('update_date',
                       'username')
        }),
    )


admin.site.register(Event, EventAdmin)
