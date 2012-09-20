from polls.models import Poll, Choice
from django.contrib import admin


class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    #on edit and new page
    fieldsets = [
        (None, {"fields": ["question"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    # for choices to show up on new/edit poll page
    inlines = [ChoiceInline]

    # on view page -> order of the columns
    list_display = ("question", "pub_date", "was_published_today")

    # on view page -> capability to filter table by pub_date
    list_filter = ["pub_date"]
    # on view page
    search_fields = ["question"]
    # shws some link with date categories
    date_hierarchy = "pub_date"

admin.site.register(Poll, PollAdmin)
