import comfy.samplers
import torch

#------------------------------------------------------------------------------------------#
#-----Float Selector-----
class HC_Float_Selector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Float": ("FLOAT", {"default": 0, "min": 0.0, "max": 100.0})
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("Float",)
    FUNCTION = "float_selector"
    CATEGORY = "HavocsCall/Basic"

    def float_selector(self, Float,):
        return (Float,)
#------------------------------------------------------------------------------------------#
#-----Int Selector-----
class HC_Int_Selector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Int": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("Int",)
    FUNCTION = "int_selector"
    CATEGORY = "HavocsCall/Basic"

    def int_selector(self, Int,):
        return (Int,)

#------------------------------------------------------------------------------------------#
#-----Prompt Combiner-----
class HC_Prompt_Combiner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "Style": ("STRING", {"default": "", "multiline": True}),
                "Subject": ("STRING", {"default": "", "multiline": True}),
                "Clothing": ("STRING", {"default": "", "multiline": True}),
                "Action": ("STRING", {"default": "", "multiline": True}),
                "Environment": ("STRING", {"default": "", "multiline": True}),
                "Extra": ("STRING", {"default": "", "multiline": True})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)
    FUNCTION = "prompt_combiner"
    CATEGORY = "HavocsCall/Basic"

    def prompt_combiner(self, Style="", Subject="", Clothing="", Action="", Environment="", Extra=""):
        prompt_parts = [part for part in [Style, Subject, Clothing, Action, Environment, Extra] if part]
        prompt = ", ".join(prompt_parts)
        return (prompt,)

#------------------------------------------------------------------------------------------#
#-----Sampler Config-----
class HC_Sampler_Config:
    Aspect_Ratios = [
        "Custom",
        "SD1.5 - 1:1 square 512x512",
        "SD1.5 - 1:1 square 1024x1024",
        "SD1.5 - 2:3 portrait 512x768",
        "SD1.5 - 3:4 portrait 512x682",
        "SD1.5 - 3:2 landscape 768x512",
        "SD1.5 - 4:3 landscape 682x512",
        "SD1.5 - 16:9 cinema 910x512",
        "SD1.5 - 1.85:1 cinema 952x512",
        "SD1.5 - 2:1 cinema 1024x512",
        "SD1.5 - 2.39:1 anamorphic 1224x512",
        "SDXL - 1:1 Square 1024 x 1024",
        "SDXL - 3:4 Portrait 896 x 1152",
        "SDXL - 5:8 Portrait 832 x 1216",
        "SDXL - 9:16 Portrait 768 x 1344",
        "SDXL - 9:21 Portrait 640 x 1536",
        "SDXL - 4:3 Landscape 1152 x 896",
        "SDXL - 3:2 Landscape 1216 x 832",
        "SDXL - 16:9 Landscape 1344 x 768",
        "SDXL - 21:9 Landscape 1536 x 640"
    ]

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "Steps": ("INT", {"default": 30, "min": 1, "max": 1000}),
                "CFG": ("FLOAT", {"default": 8.0, "min": 1.0, "max": 30.0, "step": 0.1}),
                "Sampler": (comfy.samplers.KSampler.SAMPLERS,),
                "Scheduler": (comfy.samplers.KSampler.SCHEDULERS,),
                "Denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0}),
                "Aspect_Ratio": (HC_Sampler_Config.Aspect_Ratios,),
                "Width": ("INT", {"default": 1024, "min": 64, "max": 8192, "tooltip": "This only matters if you picked a custom Aspect Ratio."}),
                "Height": ("INT", {"default": 1024, "min": 64, "max": 8192, "tooltip": "This only matters if you picked a custom Aspect Ratio."}),
                "Batch_Size": ("INT", {"default": 1, "min": 1, "max": 64})
            }
        }
    
    RETURN_TYPES = ("LATENT", "INT", "INT", "FLOAT", comfy.samplers.KSampler.SAMPLERS, comfy.samplers.KSampler.SCHEDULERS, "FLOAT", "INT", "INT", "INT",)
    RETURN_NAMES = ("Empty_Latent", "Seed", "Steps", "CFG","Sampler", "Scheduler", "Denoise", "Width", "Height", "Batch_Size",)
    FUNCTION = "sampler_config"
    CATEGORY = "HavocsCall/Basic"

    def sampler_config(self, seed, Steps, CFG, Sampler, Scheduler, Denoise, Aspect_Ratio, Width, Height, Batch_Size,):
        match Aspect_Ratio:
            case "Custom":
                Width, Height = Width, Height
            case "SD1.5 - 1:1 square 512x512":
                Width, Height = 512, 512
            case "SD1.5 - 1:1 square 1024x1024":
                Width, Height = 1024, 1024
            case "SD1.5 - 2:3 portrait 512x768":
                Width, Height = 512, 768
            case "SD1.5 - 3:4 portrait 512x682":
                Width, Height = 512, 682
            case "SD1.5 - 3:2 landscape 768x512":
                Width, Height = 768, 512
            case "SD1.5 - 4:3 landscape 682x512":
                Width, Height = 682, 512
            case "SD1.5 - 16:9 cinema 910x512":
                Width, Height = 910, 512
            case "SD1.5 - 1.85:1 cinema 952x512":
                Width, Height = 952, 512
            case "SD1.5 - 2:1 cinema 1024x512":
                Width, Height = 1024, 512
            case "SD1.5 - 2.39:1 anamorphic 1224x512":
                Width, Height = 1224, 512
            case "SDXL - 1:1 Square 1024 x 1024":
                Width, Height = 1024, 1024
            case "SDXL - 3:4 Portrait 896 x 1152":
                Width, Height = 896, 1152
            case "SDXL - 5:8 Portrait 832 x 1216":
                Width, Height = 832, 1216
            case "SDXL - 9:16 Portrait 768 x 1344":
                Width, Height = 768, 1344
            case "SDXL - 9:21 Portrait 640 x 1536":
                Width, Height = 640, 1536
            case "SDXL - 4:3 Landscape 1152 x 896":
                Width, Height = 1152, 896
            case "SDXL - 3:2 Landscape 1216 x 832":
                Width, Height = 1216, 832
            case "SDXL - 16:9 Landscape 1344 x 768":
                Width, Height = 1344, 768
            case "SDXL - 21:9 Landscape 1536 x 640":
                Width, Height = 1536, 640

        Latent = torch.zeros([Batch_Size, 4, Height // 8, Width // 8])
        
        return ({"samples":Latent}, seed, Steps, CFG, Sampler, Scheduler, Denoise, Width, Height, Batch_Size,)

#------------------------------------------------------------------------------------------#
#-----Save Image-----
# Work in progress, not fully functional yet.
class HC_Save_Image:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Image": ("IMAGE",),
                "Folder_Name": ("STRING", {"default": ""}),
                "File_Name": ("STRING", {"default": "",})
            },
            "hidden": {
                "Prompt": "PROMPT",
                "Extra_PNG_Info": "EXTRA_PNGINFO"
            }
        }
    
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "save_image"
    CATEGORY = "HavocsCall/Basic"

    def save_image(self, Image, Folder_Name="", File_Name=""):
        Path_Parts = [part for part in [Folder_Name, File_Name,] if part]
        Full_Path = "/".join(Path_Parts)
        return (Full_Path,)

#------------------------------------------------------------------------------------------#
#-----Text Box-----
class HC_Text_Box:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Text": ("STRING", {"default": "", "multiline": True})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)
    FUNCTION = "text_box"
    CATEGORY = "HavocsCall/Basic"

    def text_box(self, Text,):
        return (Text,)