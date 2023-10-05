from django import forms
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import (
    Question, Choice, Organization,
    Employee, Project, Location,
    Investor,
)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = [
        'choice_text', 'votes'
    ]
    list_select_related = ['question']


class OrganizationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'base_country',
        'office_locations',
        'domain',
        'employee_count',
        'projects'
    ]

    def employee_count(self, obj):
        count = obj.employee_set.count()
        url = (
            reverse("admin:polls_employee_changelist")
            + "?"
            + urlencode({"organization__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Employees</a>', url, count)

    employee_count.short_description = "Employees Count"


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'age',
        'gender',
        'nationality',
        'experience',
        'skills',
        'org',
    ]
    search_fields = [
        'name',
        'gender',
        'nationality',
    ]

    list_select_related = [
        'org',
    ]


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'start_date',
        'end_date',
        'allocated_budget',
        'team_size',
        'is_deployed',
        'is_completed',
        'stage'
    ]

    list_select_related = [
        'location', 'org'
    ]

    list_filter = [
        'team_size', 'is_deployed', 'stage',
    ]

    Project.stage.short_description = "Project stage"


class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'buildings_count', 'seating_capacity', 'parking_capacity', 'cafeteria_capacity',
    ]
    # list_editable = [
    #     'name', 'buildings_count', 'seating_capacity', 'parking_capacity', 'cafeteria_capacity',
    # ]

    search_fields = [
        'name'
    ]


class InvestorAdminForm(forms.ModelForm):
    class Meta:
        model = Investor
        fields = "__all__"
        labels = {
            "name": "Investor Name",
            "twitter_handle": "Twitter Handle",
            "site_link": "Site Link",
        }


class InvestorAdmin(admin.ModelAdmin):
    form = InvestorAdminForm
    list_display = [
        'name',
        'image_tag',
        'twitter_handle',
        'site_link'
    ]

    exclude = [
        'created_by', 'delete_info', 'mapped_inv_id',
    ]

    search_fields = [
        'name'
    ]

    def image_tag(self, obj):
        return format_html('<img src="{}" width="30" height="30" />'.format(obj.image.url))

    image_tag.short_description = "Logo"


admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Investor, InvestorAdmin)
