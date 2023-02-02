from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks.struct_block import StructBlock
from wagtail.core.blocks.field_block import RichTextBlock

class CohortTypesBlock(blocks.StructBlock):
        title = blocks.CharBlock(default="cohort name", help_text="sub-title" )
        text = RichTextBlock(help_text="description")

# struct logo image and website link 
class SnpLogoStruct(blocks.StructBlock):
       website_link = blocks.CharBlock( default="#", help_text="link to partner/sponsor website")
       logo_img = ImageChooserBlock()

class ButtonBlock(blocks.StructBlock):
        text = blocks.CharBlock(default="Click")
        link = blocks.CharBlock(default="#")

# first slide of top image carousel
class CarouselSlideBlock (StructBlock):
        title = blocks.CharBlock(max_length=64, help_text="slide title - h1 text")
        text = blocks.CharBlock(max_length=250,  help_text="slide text - h2 text")
        slider_image = ImageChooserBlock()
        button = ButtonBlock( max_num=1)