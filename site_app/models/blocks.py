from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks.struct_block import StructBlock



class ButtonBlock(blocks.StructBlock):
        text = blocks.CharBlock(default="Click")
        link = blocks.CharBlock(default="#")

