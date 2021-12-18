from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class IndexPage (Page):

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