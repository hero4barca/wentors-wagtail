from django.db import models
from django.db.models.fields import BooleanField
from wagtail.core.blocks.base import Block
from wagtail.core.blocks.field_block import RichTextBlock
from wagtail.core.blocks.stream_block import StreamBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class AboutPage(Page):
    # ========= Header Carousel ===============
    #  
    # first slide of top image carousel 
    first_slide_h1 = models.CharField(max_length=50, default='Main Text Here' )
    first_slide_h2 = models.CharField(max_length=250, default='More text here...one sentence')
    first_slide_button_text = models.CharField(max_length=20, default='Click')
    first_slide_button_link = models.CharField(max_length=250, default='/')
    first_slide_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # second slide of top image carousel
    second_slide_h1 = models.CharField(max_length=50, default='Main Text Here' )
    second_slide_h2 = models.CharField(max_length=250,  default='More text here...one sentence' )
    second_slide_button_text = models.CharField(max_length=20, default='Click' )
    second_slide_button_link = models.CharField(max_length=250, default='/' )
    second_slide_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # third slide of top image carousel - optional
    third_slide = models.BooleanField(default=False)
    third_slide_h1 = models.CharField(max_length=50, default='Main Text Here' )
    third_slide_h2 = models.CharField(max_length=250,  default='More text here...one sentence' )
    third_slide_button_text = models.CharField(max_length=20, default='Click' )
    third_slide_button_link = models.CharField(max_length=250, default='/' )
    third_slide_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # fourth slide of top image carousel - optional
    fourth_slide = models.BooleanField(default=False)
    fourth_slide_h1 = models.CharField(max_length=50, default='Main Text Here' )
    fourth_slide_h2 = models.CharField(max_length=250,  default='More text here...one sentence' )
    fourth_slide_button_text = models.CharField(max_length=20, default='Click' )
    fourth_slide_button_link = models.CharField(max_length=250, default='/' )
    fourth_slide_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    # fifth slide of top image carousel - optional
    fifth_slide = models.BooleanField(default=False)
    fifth_slide_h1 = models.CharField(max_length=50, default='Main Text Here' )
    fifth_slide_h2 = models.CharField(max_length=250,  default='More text here...one sentence' )
    fifth_slide_button_text = models.CharField(max_length=20, default='Click' )
    fifth_slide_button_link = models.CharField(max_length=250, default='/' )
    fifth_slide_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
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
    excellence_title = models.CharField(max_length= 50, default="Excellence")
    excellence_text = RichTextField( blank=True)
    compassion_title = models.CharField(max_length= 50, default="Compassion")
    compassion_text = RichTextField( blank=True)

    ati_second_row = models.BooleanField(default=True)
    ati_tile3_title = models.CharField(max_length= 50, default="Tile 3")
    ati_tile3_text = RichTextField( blank=True)
    ati_tile4_title = models.CharField(max_length= 50, default="Tile 4")
    ati_tile4_text = RichTextField( blank=True)

    ati_third_row = models.BooleanField(default=False)
    ati_tile5_title = models.CharField(max_length= 50, default="Tile 5")
    ati_tile5_text = RichTextField( blank=True)
    ati_tile6_title = models.CharField(max_length= 50, default="Tile 6")
    ati_tile6_text = RichTextField( blank=True)
        

    # //Call to action
    call_to_action = models.BooleanField( default=True)
    CTA_title = models.CharField(max_length=250, default="CTA Title")
    CTA_text = RichTextField( default="Call to action text here...")
    CTA_button1_text = models.CharField (max_length=25,blank=True)
    CTA_button1_link = models.CharField (max_length=250, default="#")
    CTA_button2_text = models.CharField (max_length=25, blank=True)
    CTA_button2_link = models.CharField (max_length=250, default="#")

    # //Goals section
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

        # // slide 1
        FieldPanel ('first_slide_h1'),
        FieldPanel ('first_slide_h2', classname="full"),
        FieldPanel ('first_slide_button_text'),
        FieldPanel ('first_slide_button_link'),
        ImageChooserPanel('first_slide_img'),

        # // slide 2
        FieldPanel ('second_slide_h1'),
        FieldPanel ('second_slide_h2', classname="full"),
        FieldPanel ('second_slide_button_text'),
        FieldPanel ('second_slide_button_link'),
        ImageChooserPanel('second_slide_img'),

        # // slide 3
        FieldPanel('third_slide'),
        FieldPanel ('third_slide_h1'),
        FieldPanel ('third_slide_h2', classname="full"),
        FieldPanel ('third_slide_button_text'),
        FieldPanel ('third_slide_button_link'),
        ImageChooserPanel('third_slide_img'),

        #  // slide 4
        FieldPanel('fourth_slide'),
        FieldPanel ('fourth_slide_h1'),
        FieldPanel ('fourth_slide_h2', classname="full"),
        FieldPanel ('fourth_slide_button_text'),
        FieldPanel ('fourth_slide_button_link'),
        ImageChooserPanel('fourth_slide_img'),

        # slide 5
        FieldPanel('fifth_slide'),
        FieldPanel ('fifth_slide_h1'),
        FieldPanel ('fifth_slide_h2', classname="full"),
        FieldPanel ('fifth_slide_button_text'),
        FieldPanel ('fifth_slide_button_link'),
        ImageChooserPanel('fifth_slide_img'),

        # // ============== about section - video  ===============
        FieldPanel('video_section_title', classname="full"),
        FieldPanel('video_section_text', classname="full"),
        FieldPanel('video_url', classname="full"),
        ImageChooserPanel('video_thumbnail_img'),

        # // ============== about section - iconed tiles ===================
        
        # // first row
        FieldPanel('excellence_title'),
        FieldPanel('excellence_text',  classname="full"),
        FieldPanel('compassion_title'),
        FieldPanel('compassion_text',  classname="full"),

        # // second row
        FieldPanel('ati_second_row'),
        FieldPanel('ati_tile3_title'),
        FieldPanel('ati_tile3_text',  classname="full"),
        FieldPanel('ati_tile4_title'),
        FieldPanel('ati_tile4_text',  classname="full"),

        # // third row
        FieldPanel('ati_third_row'),
        FieldPanel('ati_tile5_title'),
        FieldPanel('ati_tile5_text',  classname="full"),
        FieldPanel('ati_tile6_title'),
        FieldPanel('ati_tile6_text',  classname="full"),

        # // =============== call to action section ======================
        FieldPanel('call_to_action'),
        FieldPanel ('CTA_title', classname="full"),
        FieldPanel ('CTA_text', classname="full"),
        FieldPanel ('CTA_button1_text', classname="full" ),
        FieldPanel ('CTA_button1_link',  ),
        FieldPanel ('CTA_button2_text', classname="full" ),
        FieldPanel ('CTA_button2_link',  ),            

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

AboutPage._meta.get_field('ati_second_row').help_text = "Show/hide the second row of the iconed tiles"
AboutPage._meta.get_field('ati_third_row').help_text = "Show/hide the second row of the iconed tiles"
#AboutPage._meta.get_field('').help_text = ""

#@TODO
# Refactoring field names -> make sense and convensions -> update in templates
# Help_text for all appropriate field names 
# RichTextfield instead of Charfield where appropriate
