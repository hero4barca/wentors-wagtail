from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks.struct_block import StructBlock



class ButtonBlock(blocks.StructBlock):
        text = blocks.CharBlock(default="Click")
        link = blocks.CharBlock(default="#")

# first slide of top image carousel
class CarouselSlideBlock (StructBlock):
        title = blocks.CharBlock(max_length=64, help_text="slide title - h1 text")
        text = blocks.CharBlock(max_length=250,  help_text="slide text - h2 text")
        slider_image = ImageChooserBlock()
        button = ButtonBlock( max_num=1)