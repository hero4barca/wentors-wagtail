from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class LandingPage(Page):

    class HeaderTopBlock(blocks.StructBlock):

        header_image = ImageChooserBlock(required=True)
        h1_text = blocks.CharBlock(required=False)
        h2_text = blocks.CharBlock(required=False)

    top_header = StreamField([
        ('header', HeaderTopBlock())
            ],
            null=True,
            blank=True,
            block_counts={
                            'header': { 'max_num': 1, 'min_num':0 }, # header image is optional
                                    },
                                help_text="optional: provide image header block for course")


    landing_page_title =  models.CharField(default="Landing Page Title ",
                                         max_length=250 )
    
    main_description = RichTextField(default="Main description here",
                                            help_text="main description here")

    description_image = models.ForeignKey( 
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="descriptive image"
    )



    content_panels = Page.content_panels + [

                StreamFieldPanel('top_header'),
                FieldPanel('landing_page_title'),
                FieldPanel('main_description'),
                ImageChooserPanel('description_image'),
                
                ]