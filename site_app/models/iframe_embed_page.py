from django.db import models
from wagtail.core.models import Page



class IframeEmbedPage(Page):

    partner_name = models.CharField(max_length=50, default="partner name")
    iframe_link = models.URLField(max_length=200, default="https://www.wentors.com" )
    
