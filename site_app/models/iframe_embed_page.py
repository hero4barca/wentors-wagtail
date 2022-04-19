from django.db import models
from wagtail.core.models import Page



class IframeEmbedPage(Page):

    partner_name = models.CharField(max_length=1000, default="partner name")
    
