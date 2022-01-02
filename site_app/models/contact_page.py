from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock




class ContactPage(Page):
    
    top_text = RichTextField( default="We would love the heard form you. Reach us via email or any of our social media handles displayed below" )

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
                            },
            help_text="provide email and various social media contact info"
            )




    content_panels = Page.content_panels + [

            FieldPanel('top_text', classname="full"),
            StreamFieldPanel('contact_info'),
        ]