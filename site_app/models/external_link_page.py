from wagtail.core.models import Page
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

class ExternalLinkPage(Page):
    
    link = models.URLField(max_length=255, default='https://www.wentors.com',  help_text='Optional.  Leave blank if serving as a parent page')

    content_panels = Page.content_panels + [
        FieldPanel('link')
    ]

    def get_url(self, **kwargs):
        if self.link != '':
            return self.link
        else:
            return super().get_url(self, **kwargs)
    
    url = property(get_url)