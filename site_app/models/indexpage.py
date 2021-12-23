
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# project imports here
from .custom_blocks import ButtonBlock, CarouselSlideBlock


class IndexPage (Page):

    # ========= Header Carousel ===============
    #  
    
    carousel_slides = StreamField([
        ('slides', blocks.ListBlock( CarouselSlideBlock(), min_num=1 ) )
            ],
            null=True,
            block_counts={
                    'slides': { 'max_num': 1}, 
                            }
            )

    # //=====Header carousel end=======

    # // about-video section
    video_section_title = models.CharField(null=True, max_length=250, blank=True)
    video_section_text = RichTextField(blank= True )
    video_url = models.CharField(null=True, max_length=250, blank=True)
    video_thumbnail_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # //================ Mid page ================
    mid_section_title = models.CharField(max_length=250, blank=True)
    mid_section_text = RichTextField(blank=True) 

    # // =============== Content rows ======================

    first_row_title = models.CharField(blank=True, max_length=250)
    first_row_text = RichTextField(blank=True)
    first_row_img = models.ForeignKey(
                    'wagtailimages.Image',
                    null=True,
                    blank=True,
                    on_delete=models.SET_NULL,
                    related_name='+'
                )

    second_row_title = models.CharField(blank=True, max_length=250)
    second_row_text = RichTextField(blank=True)
    second_row_img = models.ForeignKey(
                    'wagtailimages.Image',
                    null=True,
                    blank=True,
                    on_delete=models.SET_NULL,
                    related_name='+'
                )

    third_row_title = models.CharField(blank=True, max_length=250)
    third_row_text = RichTextField(blank=True)
    third_row_img = models.ForeignKey(
                    'wagtailimages.Image',
                    null=True,
                    blank=True,
                    on_delete=models.SET_NULL,
                    related_name='+'
                )
    
    fourth_row_title = models.CharField(blank=True, max_length=250)
    fourth_row_text = RichTextField(blank=True)
    fourth_row_img = models.ForeignKey(
                    'wagtailimages.Image',
                    null=True,
                    blank=True,
                    on_delete=models.SET_NULL,
                    related_name='+'
                )


    content_panels = Page.content_panels + [

        # // ========== top carousel ===============
        StreamFieldPanel('carousel_slides'),

        FieldPanel('video_section_title', classname="full"),
        FieldPanel('video_section_text', classname="full"),
        FieldPanel('video_url', classname="full"),
        ImageChooserPanel('video_thumbnail_img'),

        FieldPanel ('first_row_title'),
        FieldPanel ('first_row_text'),
        ImageChooserPanel('first_row_img'),

        FieldPanel ('second_row_title'),
        FieldPanel ('second_row_text'),
        ImageChooserPanel('second_row_img'),

        FieldPanel ('third_row_title'),
        FieldPanel ('third_row_text'),
        ImageChooserPanel('third_row_img'),

        FieldPanel ('fourth_row_title'),
        FieldPanel ('fourth_row_text'),
        ImageChooserPanel('fourth_row_img'),
    ]