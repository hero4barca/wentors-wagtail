from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.blocks.base import Block

from wagtail.core.fields import RichTextField, StreamField

from wagtail.core.models import Page


class BankDetailsPage(Page):
    
    bank_details_text = RichTextField(blank=False, 
                                        default="Wentors bank account details here")


    content_panels = Page.content_panels + [
          FieldPanel('bank_details_text'),
      ]