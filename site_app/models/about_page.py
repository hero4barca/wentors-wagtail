from django.db import models
from django.db.models.fields import BooleanField
from wagtail.core.blocks.base import Block
from wagtail.core.blocks.field_block import RichTextBlock
from wagtail.core.blocks.stream_block import StreamBlock
from wagtail.core.blocks.struct_block import StructBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# project imports here
from .custom_blocks import ButtonBlock, CarouselSlideBlock


class AboutPage(Page):

    # ========= Header Carousel ===============  

        
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

    
    # // ATI : About Tiles with Icons
    # // first row

    class IconCardBlock (blocks.StructBlock):

        left_card_title = blocks.CharBlock(default="Value")
        left_card_text = blocks.CharBlock(default="Brief description of satated value here" )
        left_card_icon_class = blocks.CharBlock(default="bi-123")
        left_card_icon_color_hex = blocks.CharBlock(default="#41cf2e")

        right_card_title = blocks.CharBlock(default="Value")
        right_card_text = blocks.CharBlock(default="Brief description of stated value here")
        right_card_icon_class = blocks.CharBlock(default="bi-123")
        right_card_icon_color_hex = blocks.CharBlock(default="#41cf2e")
    
    values_rows = StreamField([
                ('values', blocks.ListBlock( IconCardBlock(), max_num=3 ) )
            ],
            null=True,
            block_counts={
                'values': { 'max_num': 1}, 
                    }
            )

        

    # //Section: Call to action    
    call_to_action = models.BooleanField( default=True)
    cta_title = models.CharField(max_length=250, default="CTA Title")
    cta_text = RichTextField( blank=True)
        
    cta_buttons = StreamField([
                ('buttons', blocks.ListBlock( ButtonBlock(), max_num=2 ) )
            ],
            null = True,
            block_counts={
                'buttons': { 'max_num': 1}, 
                    }
            )


    # //Section: Goals 
    goals_title_text = RichTextField( blank=True)
    
    class GoalsCardBlock(blocks.StructBlock):
        title = blocks.CharBlock(default="skill")
        text = RichTextBlock()
        img = ImageChooserBlock(required=False)

       
    
    goals_cards = StreamField([
                ('goals', blocks.ListBlock( GoalsCardBlock(), max_num=4 ) )
                    ],
                block_counts={
                        'goals': { 'max_num': 1}, 
                            },
                null=True)

    

    # //Section:  What We Do (Expertise)
    expertise_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    expertise_top_text = RichTextField(blank=True)
    expertise_right_title = RichTextField(blank=True)
    expertise_right_text = RichTextField(blank=True)

    class SkillProgressBlock(blocks.StructBlock):
        skill = blocks.CharBlock(default="skill")
        value = blocks.IntegerBlock(default=100)

    
    expertise_progress_bars = BooleanField(default=True)
    skills_and_progress = StreamField([
                ('progress', blocks.ListBlock( SkillProgressBlock(), max_num=4 ) )
                        ],
                    block_counts={
                            'progress': { 'max_num': 1}, 
                                },
                    null=True,
                        )



    # Section: Sponsor and partnets
    snp_section = BooleanField(default=True)
    snp_top_text = RichTextField(blank=True)
    snp_logo_images = StreamField([
        ('logos', blocks.ListBlock(ImageChooserBlock())),
    ],
    null=True)


    # Section: Team members
    class TeamMemberBlock (blocks.StructBlock):
        firstname = blocks.CharBlock(default="firstname")
        surname = blocks.CharBlock(default="lastname")
        photo = ImageChooserBlock(required=False)
        biography = blocks.RichTextBlock(default="short bio here")
        position =  blocks.CharBlock(default="team member position here")
        linkedin_link =  blocks.CharBlock(required=False)
        twitter_link =  blocks.CharBlock(required=False)

        class Meta:
            icon = 'user'
    
    team_top_text = RichTextField(blank=True)
    team_members = StreamField([
                ('members', blocks.ListBlock( TeamMemberBlock() ) )
                        ],
                        null=True)
        


    content_panels = Page.content_panels + [

        #// slider section

        StreamFieldPanel('carousel_slides'),


        # // ============== about section - video  ===============
        FieldPanel('video_section_title', classname="full"),
        FieldPanel('video_section_text', classname="full"),
        FieldPanel('video_url', classname="full"),
        ImageChooserPanel('video_thumbnail_img'),

        #  iconed tiles 
        StreamFieldPanel('values_rows'),
        

        # // =============== call to action section ======================
        FieldPanel('call_to_action'),
        FieldPanel ('cta_title', classname="full"),
        FieldPanel ('cta_text', classname="full"),
        StreamFieldPanel('cta_buttons'),                   

        # // ================== Goals section====================
                
        FieldPanel('goals_title_text', classname="full"),
        StreamFieldPanel('goals_cards'),

        # // ================== Expertise section====================

        ImageChooserPanel('expertise_img'),
        FieldPanel('expertise_top_text', classname="full"),
        FieldPanel('expertise_right_title', classname="full"),
        FieldPanel('expertise_right_text', classname="full"),

        FieldPanel('expertise_progress_bars'),
        StreamFieldPanel('skills_and_progress'),


        # // ================ Partners and Sponsors ===================

        FieldPanel('snp_section'),
        FieldPanel('snp_top_text', classname="full"),
        StreamFieldPanel('snp_logo_images'),

        
        # // ===================== Team ===========================
        FieldPanel('team_top_text'),
        StreamFieldPanel('team_members'),

            ]

#AboutPage._meta.get_field('ati_second_row').help_text = "Show/hide the second row of the iconed tiles"
#AboutPage._meta.get_field('ati_third_row').help_text = "Show/hide the second row of the iconed tiles"
#AboutPage._meta.get_field('').help_text = ""

#@TODO
# maxcount to allstream fields
# helptext to all model fields
# heroku deploy

