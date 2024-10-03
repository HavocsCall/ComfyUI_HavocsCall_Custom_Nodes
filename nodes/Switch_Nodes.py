# TODO
# - Make each switch bypass the non-slected nodes - No idea how yet.

#------------------------------------------------------------------------------------------#
#-----Clip Switch-----
class HC_Clip_Switch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Selection": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 2
                }),
                "Clip_1": ("CLIP", {
                    "forceInput": True
                }),
            },
            "optional": {
                "Clip_2": ("CLIP", {
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("CLIP", "INT",)
    RETURN_NAMES = ("Clip", "Selection",)

    FUNCTION = "Clip_Switch"

    CATEGORY = "HavocsCall/Switches"

    def Clip_Switch(self, Selection, Clip_1, Clip_2,):
        match Selection:
            case 1:
                return (Clip_1, Selection,)
            case 2:
                return (Clip_2, Selection,)
#------------------------------------------------------------------------------------------#
#-----Conditioning Switch-----
class HC_Conditioning_Switch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Selection": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 2
                }),
                "Conditioning_1": ("CONDITIONING", {
                    "forceInput": True
                }),
            },
            "optional": {
                "Conditioning_2": ("CONDITIONING", {
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("CONDITIONING", "INT",)
    RETURN_NAMES = ("Conditioning", "Selection",)

    FUNCTION = "Conditioning_Switch"

    CATEGORY = "HavocsCall/Switches"

    def Conditioning_Switch(self, Selection, Conditioning_1, Conditioning_2,):
        match Selection:
            case 1:
                return (Conditioning_1, Selection,)
            case 2:
                return (Conditioning_2, Selection,)

#------------------------------------------------------------------------------------------#
#-----Image Switch-----
class HC_Image_Switch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Selection": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 2
                }),
                "Image_1": ("IMAGE", {
                    "forceInput": True
                })
            },
            "optional": {
                "Image_2": ("IMAGE", {
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("IMAGE", "INT",)
    RETURN_NAMES = ("Image", "Selection",)

    FUNCTION = "Image_Switch"

    CATEGORY = "HavocsCall/Switches"

    def Image_Switch(self, Selection, Image_1, Image_2,):
        match Selection:
            case 1:
                return (Image_1, Selection,)
            case 2:
                return (Image_2, Selection,)

#------------------------------------------------------------------------------------------#
#-----Latent Switch-----
class HC_Latent_Switch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Selection": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 2
                }),
                "Latent_1": ("LATENT", {
                    "forceInput": True
                })
            },
            "optional": {
                "Latent_2": ("LATENT", {
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("LATENT", "INT",)
    RETURN_NAMES = ("Latent", "Selection",)

    FUNCTION = "Latent_Switch"

    CATEGORY = "HavocsCall/Switches"

    def Latent_Switch(self, Selection, Latent_1, Latent_2,):
        match Selection:
            case 1:
                return (Latent_1, Selection,)
            case 2:
                return (Latent_2, Selection,)

#------------------------------------------------------------------------------------------#
#-----Model Switch-----
class HC_Model_Switch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Selection": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 2
                }),
                "Model_1": ("MODEL", {
                    "forceInput": True
                })
            },
            "optional": {
                "Model_2": ("MODEL", {
                    "forceInput": True
                })
            }
        }    
    RETURN_TYPES = ("MODEL", "INT",)
    RETURN_NAMES = ("Model", "Selection",)

    FUNCTION = "Model_Switch"

    CATEGORY = "HavocsCall/Switches"

    def Model_Switch(self, Selection, Model_1, Model_2,):
        match Selection:
            case 1:
                return (Model_1, Selection,)
            case 2:
                return (Model_2, Selection,)

#------------------------------------------------------------------------------------------#
#-----String Switch-----
class HC_String_Switch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Selection": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 2
                }),
                "String_1": ("STRING", {
                    "forceInput": True
                })
            },
            "optional": {
                "String_2": ("STRING", {
                    "forceInput": True
                })
            }    
        }
    
    RETURN_TYPES = ("STRING", "INT",)
    RETURN_NAMES = ("String", "Selection",)

    FUNCTION = "String_Switch"

    CATEGORY = "HavocsCall/Switches"

    def String_Switch(self, Selection, String_1, String_2,):
        match Selection:
            case 1:
                return (String_1, Selection,)
            case 2:
                return (String_2, Selection,)

#------------------------------------------------------------------------------------------#
#-----VAE Switch-----
class HC_VAE_Switch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Selection": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 2
                }),
                "VAE_1": ("VAE", {
                    "forceInput": True
                })
            },
            "optional": {
                "VAE_2": ("VAE", {
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("VAE", "INT",)
    RETURN_NAMES = ("VAE", "Selection",)

    FUNCTION = "VAE_Switch"

    CATEGORY = "HavocsCall/Switches"

    def VAE_Switch(self, Selection, VAE_1=None, VAE_2=None,):
        match Selection:
            case 1:
                return (VAE_1, Selection,)
            case 2:
                return (VAE_2, Selection,)