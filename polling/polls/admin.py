from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 0


class PollAdmin(admin.ModelAdmin):
	search_fields = ['question']
	date_hierachy = ['pub_date']
	fieldsets = [
		('Question',{'fields': ['question']}),
		('Date Information', {'fields': ['pub_date']}),]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)