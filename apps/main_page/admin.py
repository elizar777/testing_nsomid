from django import forms
from django.contrib import admin, messages
from django.db import models
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TabbedTranslationAdmin, TranslationStackedInline
from django.contrib.auth.models import User, Group
from .models.counters_model import Counter
from .models.contacts_model import Contacts, SocialMedia
from .models.banners_model import Banner
from .models.blocks_and_departments_model import Block, Department
from .models.general_structure_model import GeneralStructure
from .models.scientific_activity_models import (ScientificActivity,
                                                ScientificActivityContent)
from .models.about_us_models import (AboutNCOMID,
                                     AboutUs,
                                     Charter,
                                     Directorate,
                                     History)
from .models.resources_model import (Report,
                                     Journal,
                                     Link,
                                     Resource)


class TranslatorMediaMixin(TranslationAdmin):
    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }



class ScientificActivityContentInline(TranslationStackedInline):
    model = ScientificActivityContent
    extra = 1


class HistoryInline(TranslationStackedInline):
    model = History
    extra = 1
    max_num = 1

    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }

class AboutUsInline(TranslationStackedInline):
    model = AboutUs
    extra = 1
    max_num = 2

    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }

class CharterInline(admin.StackedInline):
    model = Charter
    extra = 1

    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }

class DirectorateInline(TranslationStackedInline):
    model = Directorate
    extra = 1
    max_num = 1

    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


class AboutNCOMIDForm(forms.ModelForm):
    Информация = forms.CharField(max_length=255,
                                 required=False,
                                 disabled=True,
                                 initial='Информация страницы Все об НЦОМиД')

    class Meta:
        model = AboutNCOMID
        fields = '__all__'


@admin.register(AboutNCOMID)
class AboutNCOMIDAdmin(admin.ModelAdmin):
    form = AboutNCOMIDForm
    inlines = [HistoryInline, AboutUsInline, CharterInline, DirectorateInline]
    exclude = ('',)

    def has_add_permission(self, request):
        if AboutNCOMID.objects.all().count() == 1:
            return False
        return True


class RecourseForm(forms.ModelForm):
    Информация = forms.CharField(max_length=255,
                                 required=False,
                                 disabled=True,
                                 initial='Информация страницы Ресурсы')

    class Meta:
        model = Resource
        fields = '__all__'


class JournalInline(TranslationStackedInline):
    model = Journal
    extra = 1
    max_num = 1

    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


class ReportInline(TranslationStackedInline):
    model = Report
    extra = 1
    max_num = 1

    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


class LinkInline(TranslationStackedInline):
    model = Link
    extra = 1
    max_num = 1

    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
            "adminsortable2/js/plugins/admincompat.js",
            "adminsortable2/js/libs/jquery.ui.core-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.widget-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.mouse-1.11.4.js",
            "adminsortable2/js/libs/jquery.ui.touch-punch-0.2.3.js",
            "adminsortable2/js/libs/jquery.ui.sortable-1.11.4.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    form = RecourseForm
    inlines = [JournalInline, ReportInline, LinkInline]
    exclude = ('',)

    def has_add_permission(self, request):
        if Resource.objects.all().count() == 1:
            return False
        return True


class ScientificActivityAdmin(TranslatorMediaMixin, TabbedTranslationAdmin):
    def has_add_permission(self, request):
        if ScientificActivity.objects.all().count() == 4:
            return False
        return True

    # fieldsets = [
    #     (u'Ky', {'fields': ('title_ky', 'icon')}),
    #     (u'Ru', {'fields': ('title_ru',)}),
    #     (u'En', {'fields': ('title_en',)}),
    # ]

    inlines = [ScientificActivityContentInline]


class CounterAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if Counter.objects.all().count() == 1:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if Counter.objects.count() >= 1 and not change:
            self.message_user(request, 'Вы не можете добавлять более 1 счетчика, вы можете только изменять существующий счетчик.', level=messages.ERROR)
            return
        super().save_model(request, obj, form, change)

    # fieldsets = [
    #     (u'Ky', {'fields': ('main_title_ky', 'contacted_title_ky', 'discharged_title_ky', 'born_title_ky', 'operated_title_ky', 'contacted', 'contacted_icon', 'discharged', 'discharged_icon', 'born', 'born_icon', 'operated', 'operated_icon')}),
    #     (u'Ru', {'fields': ('main_title_ru', 'contacted_title_ru', 'discharged_title_ru', 'born_title_ru', 'operated_title_ru')}),
    #     (u'En', {'fields': ('main_title_en', 'contacted_title_en', 'discharged_title_en', 'born_title_en', 'operated_title_en')}),
    # ]


class ContactsAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if Contacts.objects.all().count() == 5:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if Contacts.objects.count() >= 5 and not change:
            self.message_user(request, 'Вы не можете добавлять более 5 контакт, вы можете только изменять существующий контакт.', level=messages.ERROR)
            return
        super().save_model(request, obj, form, change)

    # fieldsets = [
    #     (u'Ky', {'fields': ('address_1_title_ky', 'address_2_title_ky', 'phone_number_title_ky', 'email_title_ky', 'address_1', 'address_2', 'address_icon', 'phone_number', 'phone_icon', 'email', 'email_icon', 'instagram', 'instagram_icon', 'facebook', 'facebook_icon', 'youtube', 'youtube_icon')}),
    #     (u'Ru', {'fields': ('address_1_title_ru', 'address_2_title_ru', 'phone_number_title_ru', 'email_title_ru',)}),
    #     (u'En', {'fields': ('address_1_title_en', 'address_2_title_en', 'phone_number_title_en', 'email_title_en',)}),
    # ]


class SocialMediaAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if SocialMedia.objects.all().count() == 3:
            return False
        return True
    
    def save_model(self, request, obj, form, change):
        if SocialMedia.objects.count() >= 3 and not change:
            self.message_user(request, 'Вы не можете добавлять более 3 социальных сетей, вы можете только изменять существующий социальные сети.', level=messages.ERROR)
            return
        super().save_model(request, obj, form, change)


class BannerAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if Banner.objects.all().count() == 1:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if Banner.objects.count() >= 1 and not change:
            self.message_user(request, 'Вы не можете добавлять более 1 баннер, вы можете только изменять существующие баннеры.', level=messages.ERROR)
            return 
        super().save_model(request, obj, form, change)

    # fieldsets = [
    #     (u'Ky', {'fields': ('title_ky', 'text_ky', 'images')}),
    #     (u'Ru', {'fields': ('title_ru', 'text_ru')}),
    #     (u'En', {'fields': ('title_en', 'text_en')}),
    # ]
    
    

class BlockAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if Block.objects.all().count() == 4:
            return False
        return True
    def save_model(self, request, obj, form, change):
        if change:
            Department.objects.filter(block=obj).delete()

        if Block.objects.count() >= 4 and not change:
            self.message_user(request, "Вы не можете добавлять более 4 блоков, вы можете только изменить существующие блоки.", level=messages.ERROR)
        else:
            super().save_model(request, obj, form, change)

    # fieldsets = [
    #     (u'Ky', {'fields': ('title_ky', 'photo_url' )}),
    #     (u'Ru', {'fields': ('title_ru', )}),
    #     (u'En', {'fields': ('title_en', )}),
    # ]


class DepartmentAdmin(TranslatorMediaMixin, TranslationAdmin):
    pass


class GeneralStructureAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if GeneralStructure.objects.all().count() == 4:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if GeneralStructure.objects.count() >= 4 and not change:
            self.message_user(request, "Вы не можете добавлять более 4 блоков, вы можете только изменить существующие блоки.", level=messages.ERROR)
        else:
            super().save_model(request, obj, form, change)
    # fieldsets = [
    #     (u'Ky', {'fields': ('title_ky', 'description_ky',)}),
    #     (u'Ru', {'fields': ('title_ru', 'description_ru', )}),
    #     (u'En', {'fields': ('title_en', 'description_en', )}),
    # ]

admin.site.register(Block, BlockAdmin)
admin.site.register(GeneralStructure, GeneralStructureAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Counter, CounterAdmin)
admin.site.register(ScientificActivity, ScientificActivityAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
# admin.site.register(History, HistoryInline)
# admin.site.register(Charter, CharterInline)
# admin.site.register(Directorate, DirectorateInline)
# admin.site.register(AboutUs, AboutUsInline)
admin.site.unregister(User)
admin.site.unregister(Group)
