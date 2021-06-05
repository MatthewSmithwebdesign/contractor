from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField


@register_setting
class LicenseSettings(BaseSetting):

    license = RichTextField(
        blank=True,
        null=True,
        features=[],
        )
    panels = [
        FieldPanel("license")
    ]


@register_setting
class ContactSettings(BaseSetting):

    contact = RichTextField(
        blank=True,
        null=True,
        features=['link'],
        )
    panels = [
        FieldPanel("contact")
    ]




@register_setting
class SocialMediaSettings(BaseSetting):

    facebook = models.URLField(
        blank=True,
        help_text='enter your Facebook URL'
    )
    twitter = models.URLField(
        blank=True,
        help_text='enter your Twitter URL'
    )
    instagram = models.URLField(
        blank=True,
        help_text='enter your Instagram URL'
    )




    panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("instagram"),


    ]
