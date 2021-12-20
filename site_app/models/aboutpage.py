from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

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

    
    # // about tiles with icons
    # // first row
    excellence_title = models.CharField(max_length= 50, default="Excellence")
    excellence_text = RichTextField( blank=True)
    compassion_title = models.CharField(max_length= 50, default="Compassion")
    compassion_text = RichTextField( blank=True)

    #second_row = models.BooleanField


    

    # //Call to action
    call_to_action = models.BooleanField( default=True)
    CTA_title = models.CharField(max_length=250, default="CTA Title")
    CTA_text = RichTextField( default="Call to action text here...")
    CTA_button1_text = models.CharField (max_length=25,blank=True)
    CTA_button1_link = models.CharField (max_length=250, default="#")
    CTA_button2_text = models.CharField (max_length=25, blank=True)
    CTA_button2_link = models.CharField (max_length=250, default="#")

    





    content_panels = Page.content_panels + [
        FieldPanel ('first_slide_h1'),
        FieldPanel ('first_slide_h2', classname="full"),
        FieldPanel ('first_slide_button_text'),
        FieldPanel ('first_slide_button_link'),
        ImageChooserPanel('first_slide_img'),

        FieldPanel ('second_slide_h1'),
        FieldPanel ('second_slide_h2', classname="full"),
        FieldPanel ('second_slide_button_text'),
        FieldPanel ('second_slide_button_link'),
        ImageChooserPanel('second_slide_img'),

        FieldPanel('third_slide'),
        FieldPanel ('third_slide_h1'),
        FieldPanel ('third_slide_h2', classname="full"),
        FieldPanel ('third_slide_button_text'),
        FieldPanel ('third_slide_button_link'),
        ImageChooserPanel('third_slide_img'),

        FieldPanel('fourth_slide'),
        FieldPanel ('fourth_slide_h1'),
        FieldPanel ('fourth_slide_h2', classname="full"),
        FieldPanel ('fourth_slide_button_text'),
        FieldPanel ('fourth_slide_button_link'),
        ImageChooserPanel('fourth_slide_img'),

        FieldPanel('fifth_slide'),
        FieldPanel ('fifth_slide_h1'),
        FieldPanel ('fifth_slide_h2', classname="full"),
        FieldPanel ('fifth_slide_button_text'),
        FieldPanel ('fifth_slide_button_link'),
        ImageChooserPanel('fifth_slide_img'),

        FieldPanel('video_section_title', classname="full"),
        FieldPanel('video_section_text', classname="full"),
        FieldPanel('video_url', classname="full"),
        ImageChooserPanel('video_thumbnail_img'),

        FieldPanel('excellence_title'),
        FieldPanel('excellence_text'),
        FieldPanel('compassion_title'),
        FieldPanel('compassion_text'),


        FieldPanel('call_to_action'),
        FieldPanel ('CTA_title', classname="full"),
        FieldPanel ('CTA_text', classname="full"),
        FieldPanel ('CTA_button1_text', classname="full" ),
        FieldPanel ('CTA_button1_link',  ),
        FieldPanel ('CTA_button2_text', classname="full" ),
        FieldPanel ('CTA_button2_link',  ),
            
            
            ]
