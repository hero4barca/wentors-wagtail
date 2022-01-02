from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel



class MainCoursePage(Page):
    
    class HeaderTopBlock(blocks.StructBlock):

        header_image = ImageChooserBlock(required=True)
        h1_text = blocks.CharBlock(required=False)
        h2_text = blocks.CharBlock(required=False)

    top_header = StreamField([
        ('header', HeaderTopBlock())
            ],
            null=False,
            block_counts={
                            'header': { 'max_num': 1, 'min_num':1 }, 
                                    })
    
    courses_image = models.ForeignKey(
                        'wagtailimages.Image',
                        null=True,
                        blank=True,
                        on_delete=models.SET_NULL,
                        related_name='+'
                    )
    courses_top_text = RichTextField(blank=True,
                            help_text="general description for courses provided" )

   


    content_panels = Page.content_panels + [

            StreamFieldPanel('top_header'),
            FieldPanel('courses_top_text', classname="full"),
            ImageChooserPanel('courses_image'),

        ]
       