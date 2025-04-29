from .nodes.Basic_Nodes import *
from .nodes.Conversion_Nodes import *
from .nodes.Math_Nodes import *
from .nodes.Prompt_Styler_Nodes import *
from .nodes.Switch_Nodes import *

NODE_CLASS_MAPPINGS = {
    #------------------------------------------------------------------------------------------#
    #-----Basic Nodes-----
    "Float Selector": HC_Float_Selector,
    "Integer Selector": HC_Integer_Selector,
    "Prompt Combiner": HC_Prompt_Combiner,
    "Sampler Config": HC_Sampler_Config,
    "Save Image": HC_Save_Image,
    "Text Box": HC_Text_Box,

    #------------------------------------------------------------------------------------------#
    #-----Conversion Nodes-----
    "Float to Integer": HC_Float_to_Integer,
    "Float to String": HC_Float_to_String,
    "Integer to Float": HC_Integer_to_Float,
    "Integer to String": HC_Integer_to_String,
    "String to Float": HC_String_to_Float,
    "String to Integer": HC_String_to_Integer,

    #------------------------------------------------------------------------------------------#
    #-----Math Nodes-----
    "Math Operation": HC_Math_Operation,

    #------------------------------------------------------------------------------------------#
    #-----Prompt Styler Node-----
    "Prompt Styler": HC_Prompt_Styler,

    #------------------------------------------------------------------------------------------#
    #-----Switch Nodes-----
    "Clip Switch": HC_Clip_Switch,
    "Conditioning Switch": HC_Conditioning_Switch,
    "Image Switch": HC_Image_Switch,
    "Latent Switch": HC_Latent_Switch,
    "Model Switch": HC_Model_Switch,
    "String Switch": HC_String_Switch,
    "VAE Switch": HC_VAE_Switch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    #------------------------------------------------------------------------------------------#
    #-----Basic Nodes-----
    "Float Selector": "Float Selector",
    "Integer Selector": "Integer Selector",
    "Prompt Combiner": "Prompt Combiner",
    "Sampler Config": "Sampler Config",
    "Save Image": "Save Image",
    "Text Box": "Text Box",

    #------------------------------------------------------------------------------------------#
    #-----Conversion Nodes-----
    "Float to Integer": "Float to Integer",
    "Float to String": "Float to String",
    "Integer to Float": "Integer to Float",
    "Integer to String": "Integer to String",
    "String to Float": "String to Float",
    "String to Integer": "String to Integer",

    #------------------------------------------------------------------------------------------#
    #-----Math Nodes-----
    "Math Operation": "Math Operation",
    
    #------------------------------------------------------------------------------------------#
    #-----Prompt Styler Node-----
    "Prompt Styler": "Prompt Styler",

    #------------------------------------------------------------------------------------------#
    #-----Switch Nodes-----
    "Clip Switch": "Clip Switch",
    "Conditioning Switch": "Conditioning Switch",
    "Image Switch": "Image Switch",
    "Latent Switch": "Latent Switch",
    "Model Switch": "Model Switch",
    "String Switch": "String Switch",
    "VAE Switch": "VAE Switch"
}