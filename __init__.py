from .nodes.Basic_Nodes import *
from .nodes.Conversion_Nodes import *
from .nodes.Switch_Nodes import *

NODE_CLASS_MAPPINGS = {
    #------------------------------------------------------------------------------------------#
    #-----Basic Nodes-----
    "Float Selector": HC_Float_Selector,
    "Int Selector": HC_Int_Selector,
    "Prompt Combiner": HC_Prompt_Combiner,
    "Sampler Config": HC_Sampler_Config,
    "Text Box": HC_Text_Box,

    #------------------------------------------------------------------------------------------#
    #-----Conversion Nodes-----
    "Float to Int": HC_Float_to_Int,
    "Float to String": HC_Float_to_String,
    "Int to Float": HC_Int_to_Float,
    "Int to String": HC_Int_to_String,

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
    "Int Selector": "Int Selector",
    "Prompt Combiner": "Prompt Combiner",
    "Sampler Config": "Sampler Config",
    "Text Box": "Text Box",

    #------------------------------------------------------------------------------------------#
    #-----Conversion Nodes-----
    "Float to Int": "Float to Int",
    "Float to String": "Float to String",
    "Int to Float": "Int to Float",
    "Int to String": "Int to String",

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