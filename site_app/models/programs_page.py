from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.blocks.field_block import RichTextBlock


from .custom_blocks import ButtonBlock, ProgramSubBlock, CohortTypesBlock

class ProgramsPage(Page):       

    class CohortsBlock(blocks.StructBlock):
        cohorts_description = RichTextBlock(blank=True, help_text="Description for cohorts")
        cohorts_image = ImageChooserBlock(required=False)
        button = ButtonBlock()
        cohorts_list = blocks.ListBlock( CohortTypesBlock(), required=False )
    
    cohorts = StreamField([
                ('cohorts', blocks.ListBlock( CohortsBlock(), min_num=1 ) )
                    ],
                block_counts={
                        'cohorts': { 'max_num': 1}, 
                            },
                null=True,
                help_text="cohorts description and details")


    class MembersDetailsBlock(blocks.StructBlock):
        description = RichTextBlock(blank=True, help_text="Description of membership platform")
        image = ImageChooserBlock(required=False)
        button = ButtonBlock()
        features_table = blocks.BooleanBlock(default=False,
                                            required=False, 
                                            help_text="does this program have a comparison table to display?")

    
    membership_info = StreamField([
                ('membership', MembersDetailsBlock())
                    ],
                block_counts={
                        'membership': { 'max_num': 1}, 
                            },
                null=True,
                help_text="membership portal info")


       
    
    
    content_panels = Page.content_panels + [   
        
        StreamFieldPanel('cohorts'),
        StreamFieldPanel('membership_info'),

    ]
