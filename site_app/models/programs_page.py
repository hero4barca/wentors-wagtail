from typing_extensions import Required
from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks.field_block import RichTextBlock


from .custom_blocks import ButtonBlock, ProgramSubBlock

class ProgramsPage(Page):
    
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
    
    


    class ProgramDetailsBlock(blocks.StructBlock):
        title = blocks.CharBlock(default="Program", help_text="program name" )
        description_text = RichTextBlock(blank=True, help_text="provide detailed course description here")
        button = ButtonBlock()
        program_breakdown = blocks.ListBlock( ProgramSubBlock(), required=False )

    programs_list = StreamField([
                ('programs', blocks.ListBlock( ProgramDetailsBlock(), min_num=1 ) )
                    ],
                block_counts={
                        'programs': { 'max_num': 1}, 
                            },
                #null=True,
                help_text=" list various programs and provide details")

    
    

    #@TODO remove programs_top_description text, replace with structed content area.
    
    
    
    content_panels = Page.content_panels + [   
        
        
        StreamFieldPanel('top_header'),
        StreamFieldPanel('programs_list'),


    ]
