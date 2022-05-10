from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel



class IframeEmbedPage(Page):

    partner_name = models.CharField(max_length=50, default="partner name")
    iframe_link = models.URLField(max_length=200, default="https://www.wentors.com" )


    content_panels = Page.content_panels + [
        
        FieldPanel('partner_name'),
        FieldPanel('iframe_link')

    ]
    
