from django.contrib import admin

from users.models import User
from tuites.models import Tuite


class InlineTuiteAdmin(admin.StackedInline):
    model = Tuite


class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('following', )
    readonly_fields = ('username', )
    inlines = [InlineTuiteAdmin, ]
    fieldsets = (
        ('Dados pessoais', {
            'fields': ('username', 'email', 'date_joined'),
        }),
        ('Tuirer', {
            'fields': ('following', ),
            'description': 'Coisas relacionadas ao nosso sistema',
        })
    )


admin.site.register(User, UserAdmin)
