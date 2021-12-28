from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from django.utils.translation import gettext_lazy as _



class ContactPage(Page):
    
    top_text = RichTextField( default="Reach us via email or with any of the social media handles below" )

    class ContactInfoBlock(blocks.StructBlock):

        class ContactPlatform(models.TextChoices):
            EMAIL = 'email', _('email')
            SOCIAL_MEDIA = 'social_media', _('social_media')

        type = models.CharField(max_length=30, 
                                    choices=ContactPlatform.choices, 
                                    default=ContactPlatform.SOCIAL_MEDIA)
        address_or_link = models.CharField(max_length=50)
        handle = models.CharField(max_length=50)
        img = models.ForeignKey(
                'wagtailimages.Image',
                null=True,
                blank=True,
                on_delete=models.SET_NULL,
                related_name='+'
            )

    contact_info = StreamField([ 
        ('contacts', blocks.ListBlock( ContactInfoBlock(), min_num=2 ))
            ],
            null=True,
            block_counts={
                        'contacts': { 'max_num': 1, 'min_num': 1}, 
                            }
            )


    content_panels = Page.content_panels + [

            FieldPanel('top_text', classname="full"),
            StreamFieldPanel('contact_info')
        ]