from django.db import models
from django.db.models.fields import URLField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

class CourseDetailPage(Page):
    
    class HeaderTopBlock(blocks.StructBlock):

        header_image = ImageChooserBlock(required=True)
        h1_text = blocks.CharBlock(required=False)
        h2_text = blocks.CharBlock(required=False)

    top_header = StreamField([
        ('header', HeaderTopBlock())
            ],
            null=True,
            blank=True,
            block_counts={
                            'header': { 'max_num': 1, 'min_num':0 }, # header image is optional
                                    },
                                help_text="optional: provide image header block for course")


    course_title =  models.CharField(default="Course Title Here",
                                         max_length=250 )
    
    
    
    COURSE_TYPE_CHOICES = [
                ('taught course', 'taught course'),
                ('masterclass', 'masterclass'),
            ]
        
    course_type = models.CharField(choices=COURSE_TYPE_CHOICES, max_length=20)

    course_details_section = RichTextField(default="Provide detailed course description here",
                                            help_text="provide detailed course description here")
    course_price = models.DecimalField(decimal_places=2, default=0.0, max_digits=9, max_length=10)
    course_payment_link = URLField(blank=True, help_text="link to the course payment page")

    overview_and_benefits = RichTextField(blank=True)
    detailed_curriculum = RichTextField(blank=True)

    class AboutFacilitatorBlock(blocks.StructBlock):

        heading = blocks.CharBlock(form_classname="full title")
        paragraph = blocks.RichTextBlock()
        images = blocks.ListBlock(ImageChooserBlock(), max_num=2)
        

    about_facilitator = StreamField([
        ('facilitator', AboutFacilitatorBlock() )      
                ],
              null=True,
              blank=True,
              block_counts={
                        'facilitator': { 'max_num': 1}, 
                            },
                help_text="more details about facilitator" 
                )

    content_panels = Page.content_panels + [

            StreamFieldPanel('top_header'),
            FieldPanel('course_title'),
            FieldPanel('course_details_section'),
            FieldPanel('course_price'),
            FieldPanel('course_payment_link'),
            FieldPanel('course_type'),
            FieldPanel('overview_and_benefits'),   
            FieldPanel('detailed_curriculum'),
            StreamFieldPanel('about_facilitator'),
            ]