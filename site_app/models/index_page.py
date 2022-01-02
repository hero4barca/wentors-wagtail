
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks.field_block import RichTextBlock

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
                            },
            help_text="for top header carousel"
            )

    # //=====Header carousel end=======

    # // about-video section
    video_section_title = models.CharField(null=True, max_length=250, blank=True,
                                help_text="title for video section")
    video_section_text = RichTextField(blank= True,
                                     help_text="text with more about info beside video")
    video_url = models.CharField(null=True, max_length=250, blank=True, help_text="embed url for video")
    video_thumbnail_img = models.ForeignKey( 
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="image to replace video if preferred"
    )

    # //================ Mid page ================
    mid_section_title = models.CharField(max_length=250, blank=True, 
                                            help_text="title for page mid-section")
    mid_section_text = RichTextField(blank=True, help_text="text for page mid-section") 

    # // =============== Content rows ======================

    class RowBlock(blocks.StructBlock):
        title = blocks.CharBlock(default="Title Here")
        text = RichTextBlock(blank=True)
        img = ImageChooserBlock(required=False)
        button = ButtonBlock()

    work_process_rows = StreamField([
        ('rows', blocks.ListBlock( RowBlock(), max_num=4, min_num=1  ) )
            ],
            null=True,
                    block_counts={
                        'rows': { 'max_num': 1, 'min_num': 1}, 
                            },
                        help_text="defines rows of paragraphs and images for home page"                  
    )

    

    
    content_panels = Page.content_panels + [

        # // ========== top carousel ===============
        StreamFieldPanel('carousel_slides'),

        # // =========== about-video section ============
        FieldPanel('video_section_title', classname="full"),
        FieldPanel('video_section_text', classname="full"),
        FieldPanel('video_url', classname="full"),
        ImageChooserPanel('video_thumbnail_img'),

        # // =========== mid section ============
        FieldPanel('mid_section_title'),
        FieldPanel('mid_section_text'),


    # // =========== work process============ 
        StreamFieldPanel('work_process_rows'),
       
    ]