from typing_extensions import Required
from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from django.utils.translation import gettext_lazy as _
from wagtail.images.blocks import ImageChooserBlock




class ContactPage(Page):
    
    top_text = RichTextField( default="Reach us via email or with any of the social media handles below" )

    class ContactInfoBlock(blocks.StructBlock):

        class ContactTypeBlock(blocks.ChoiceBlock):
            choices = [
                ('email', 'email'),
                ('social media', 'social media'),
                ('other', 'other'),
            ]

        type = ContactTypeBlock()
        address_or_link = blocks.CharBlock()
        handle = blocks.CharBlock(required=False)
        img = ImageChooserBlock(required=False)

        

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
            StreamFieldPanel('contact_info'),
        ]