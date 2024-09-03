from unfold.admin import ModelAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin import register
from unfold.contrib.filters.admin import (RangeDateFilter, RangeDateTimeFilter)
from personnel.models import Projet, Candidature, Affectation, Poste
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm


from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

admin.site.unregister(User)
 
 
@register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('username', 'email_link', 'is_staff', 'is_active')
    list_per_page = 10

    def email_link(self, obj):
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)
    email_link.short_description = 'Email'

# Register your models here.

@register(Projet)
class AdminProjet(ModelAdmin, ImportExportModelAdmin):
    list_display=('nom','description','objectif')
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_per_page = 10
    search_fields = ('nom',)
    list_filter_submit = True
    list_filter = [
        ('date_debut', RangeDateFilter),
        ('date_fin', RangeDateFilter),
        "cloture",
    ]
# admin.site.register(Projet,AdminProjet)


@register(Candidature)
class AdminCandidature(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display=('nom','prenom','email_link','telephone','localisation','statut')
    list_per_page = 10
    list_filter = ['statut']
    search_fields = ('nom',)
    fieldsets = [
       ("Informations personnelles", {"fields": ["user","photo","nom","prenom","telephone","email","localisation"]}),
       ("Médias", {"fields": ["cv","lettre_motivation"]}),
       (None, {"fields": ["statut"]}),
    ]
    def email_link(self, obj):
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)
    email_link.short_description = 'Email'
    import_form_class = ImportForm
    export_form_class = ExportForm
# admin.site.register(Candidature,AdminCandidature)


@register(Affectation)
class AdminAffectation(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    list_display=('projet','poste')
    list_per_page = 10
    filter_horizontal = ("candidature",)
    list_filter = ("projet","poste")
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'projet':
            # Filtrer les projets pour ne montrer que ceux qui ne sont pas terminés
            kwargs["queryset"] = Projet.objects.filter(cloture=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.projet.Mcloture:
            # Rendre tous les champs en lecture seule si le projet est terminé
            return [field.name for field in self.model._meta.fields]
        return super().get_readonly_fields(request, obj)

    def has_change_permission(self, request, obj=None):
        if obj and obj.projet.cloture:
            # Empêcher les modifications si le projet est terminé
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.projet.cloture:
            # Autoriser la suppression si le projet est terminé
            return True
        return super().has_delete_permission(request, obj)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'candidature':
            kwargs["queryset"] = Candidature.objects.validée() 
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    

# admin.site.register(Affectation,AdminAffectation)
    
@register(Poste)
class AdminPoste(ModelAdmin):
    list_display=('nom','description')
    list_per_page = 10
    search_fields = ('nom',)
# admin.site.register(Poste,AdminPoste)