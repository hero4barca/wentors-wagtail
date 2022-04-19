from email.policy import default
from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks.field_block import RichTextBlock

from .custom_blocks import ButtonBlock

class JobsPage(Page):

    jobs_partners_descriptrion = RichTextField(default="Jobs partners description here",
                                            help_text="jobs partners description here")


    class JobsPartnerBlock (blocks.StructBlock):
        
        job_partner_name = blocks.CharBlock( default="Job Partner Name")
        job_partner_logo =  ImageChooserBlock(required=True)
        job_partner_description = blocks.RichTextBlock(default="Provide detailed job partner description here",
                                            help_text="provide detailed job partner descriprtion description here")
        job_partner_link = blocks.CharBlock(required=True, default='https://www.wentors.com')

    
    job_partners = StreamField(

                    [  ( 'jobs_partners', blocks.ListBlock( JobsPartnerBlock() )  ) ], 
                    null=True, blank=True,
                    block_counts={ 'jobs_partners': 
                                        {'min_num': 1},
                                 },
                    help_text = "job partner details"
                    
                    )
   
    # about_facilitator = StreamField([
    #     ('facilitator', AboutFacilitatorBlock() )      
    #             ],
    #           null=True,
    #           blank=True,
    #           block_counts={
    #                     'facilitator': { 'max_num': 1}, 
    #                         },
    #             help_text="more details about facilitator" 
    #             )



    content_panels = Page.content_panels + [
        
        FieldPanel('jobs_partners_descriptrion'),
        StreamFieldPanel('job_partners')

    ]

