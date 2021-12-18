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

    # first slide of image heaader bootsrap carousel 
    first_slide_h1 = models.CharField(max_length=30, default='Main Text Here' )
    first_slide_h2 = models.CharField(max_length=50, default='More text here...one sentence')
    first_slide_button_text = models.CharField(max_length=20, default='CTA text')
    first_slide_button_link = models.CharField(max_length=250, default='/')
    first_slide_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    second_slide_h1 = models.CharField(max_length=30, default='Main Text Here' )
    second_slide_h2 = models.CharField(max_length=50,  default='More text here...one sentence' )
    second_slide_button_text = models.CharField(max_length=20, default='CTA text' )
    second_slide_button_link = models.CharField(max_length=250, default='/' )
    second_slide_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    video_text = RichTextField(blank= True)
    

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

        FieldPanel('video_text', classname="full")
    ]