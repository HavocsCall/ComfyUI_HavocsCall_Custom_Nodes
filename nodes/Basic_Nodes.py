#------------------------------------------------------------------------------------------#
#-----Import Libraries-----
# For HC_Load_Image
import folder_paths
import hashlib
from PIL import Image, ImageOps, ImageSequence
import torch

# For HC_Sampler_Config
import comfy.samplers
#import folder_paths
#import torch

# For HC_Save_Image
import json
import numpy as np
from pathlib import Path
#from PIL import Image
from PIL.PngImagePlugin import PngInfo
import time
#import torch

#------------------------------------------------------------------------------------------#
#-----Float Selector-----
class HC_Float_Selector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Float": ("FLOAT", {"default": 0, "min": 0.0, "max": 100.0})
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("Float",)
    FUNCTION = "float_selector"
    CATEGORY = "HavocsCall/Basic"
    DESCRIPTION = "Select a float value."

    def float_selector(self, Float):
        return (Float,)

#------------------------------------------------------------------------------------------#
#-----Integer Selector-----
class HC_Integer_Selector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Integer": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("Integer",)
    FUNCTION = "integer_selector"
    CATEGORY = "HavocsCall/Basic"
    DESCRIPTION = "Select an integer value."

    def integer_selector(self, Integer):
        return (Integer,)


#------------------------------------------------------------------------------------------#
#-----Load Image-----
class HC_Load_Image:
    @classmethod
    def INPUT_TYPES(cls):
        #Get the input directory
        input_dir = Path(folder_paths.get_input_directory())

        # Get the list of image files in the input directory
        image_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp', '.tiff', '.tif')
        files = [f.name for f in input_dir.iterdir() if f.is_file() and f.suffix.lower() in image_extensions]

        return {
             "required": {
                  "image": (sorted(files), {"image_upload": True})
             }
        }
    
    RETURN_TYPES = ("IMAGE", "MASK", "INT", "INT",)
    RETURN_NAMES = ("Image", "Mask", "Width", "Height",)
    FUNCTION = "load_image"
    CATEGORY = "HavocsCall/Basic"
    DESCRIPTION = "Load an image from the input directory."

    def load_image(self, image):
        image_path = folder_paths.get_annotated_filepath(image)
        img = Image.open(image_path)

        output_images = []
        output_masks = []

        width, height = img.size

        for i in ImageSequence.Iterator(img):
            i = ImageOps.exif_transpose(i)
            
            if i.mode == 'I':
                i = i.point(lambda i: i * (1 / 255))
            
            image = i.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            elif i.mode == 'P' and 'transparency' in i.info:
                mask = np.array(i.convert('RGBA').getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
            
            output_images.append(image)
            output_masks.append(mask.unsqueeze(0))

        if len(output_images) > 1:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]

        return (output_image, output_mask, width, height,)

    @classmethod
    def IS_CHANGED(self, Images):
        image_path = folder_paths.get_annotated_filepath(Images)
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(self, image):
        if not folder_paths.exists_annotated_filepath(image):
            return "Invalid image file: {}".format(image)
        return True

#------------------------------------------------------------------------------------------#
#-----Prompt Combiner-----
class HC_Prompt_Combiner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "Style": ("STRING", {"default": "", "multiline": True}),
                "Face": ("STRING", {"default": "", "multiline": True}),
                "Subject": ("STRING", {"default": "", "multiline": True}),
                "Clothing": ("STRING", {"default": "", "multiline": True}),
                "Action": ("STRING", {"default": "", "multiline": True}),
                "Environment": ("STRING", {"default": "", "multiline": True}),
                "Extra": ("STRING", {"default": "", "multiline": True})
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING",)
    RETURN_NAMES = ("Combined Prompt", "Style", "Face", "Subject", "Clothing", "Action", "Environment", "Extra",)
    FUNCTION = "prompt_combiner"
    CATEGORY = "HavocsCall/Basic"
    DESCRIPTION = "Combine prompt parts into a single prompt."

    def prompt_combiner(self, Face="", Style="", Subject="", Clothing="", Action="", Environment="", Extra=""):
        prompt_parts = [part for part in [Style, Face, Subject, Clothing, Action, Environment, Extra] if part]
        combined_prompt = ", ".join(prompt_parts)
        return (combined_prompt, Style, Face, Subject, Clothing, Action, Environment, Extra,)

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
    def INPUT_TYPES(cls):
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
    DESCRIPTION = "Configure sampler settings."

    def sampler_config(self, seed, Steps, CFG, Sampler, Scheduler, Denoise, Aspect_Ratio, Width, Height, Batch_Size):
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
class HC_Save_Image:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Images": ("IMAGE", {"forceInput": True}),
                "Folder_Name": ("STRING", {"default": ""}),
                "File_Name_Prefix": ("STRING", {"default": "ComfyUI"}),
                "Save_Metadata": ("BOOLEAN", {"default": True, "label_on": "Yes", "label_off": "No"}),
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO"
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "save_images"
    OUTPUT_NODE = True
    CATEGORY = "HavocsCall/Basic"
    DESCRIPTION = "Saves the input images to your ComfyUI output directory."

    def save_images(self, Images, Folder_Name, Save_Metadata, File_Name_Prefix, prompt = None, extra_pnginfo = None):
        output_dir = Path(folder_paths.get_output_directory())
        image_height = Images[0].shape[0]
        image_width = Images[0].shape[1]

        # Create folder if it does not exist
        full_path = output_dir / Folder_Name if Folder_Name else output_dir
        full_path.mkdir(parents=True, exist_ok=True)
        
        # Replace variables in the file name prefix
        File_Name_Prefix = self.replace_variables(File_Name_Prefix, image_width, image_height) if "%" in File_Name_Prefix else File_Name_Prefix

        # Determine counter
        try:
            files = full_path.iterdir()
            counter = max(
                (int(f.stem.split("_")[-1]) for f in files if f.is_file() and f.stem.startswith(File_Name_Prefix)),
                default=0
            ) + 1
        except ValueError:
            counter = 1
        
        results = list()

        # Prepare images
        for image in Images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            # Prepare metadata
            metadata = None
            if Save_Metadata:
                metadata = PngInfo()
                if prompt is not None:
                    metadata.add_text("prompt", json.dumps(prompt))
                if extra_pnginfo is not None:
                    for x in extra_pnginfo:
                        metadata.add_text(x, json.dumps(extra_pnginfo[x]))

            # Add counter to the file name
            file_name = f"{File_Name_Prefix}_{counter:05}.png"

            # Save the image
            img.save(full_path / file_name, pnginfo = metadata, compress_level = 4)
            
            # Add ComfyUI specific stuff
            results.append({
                "filename": file_name,
                "subfolder": str(full_path),
                "type": "output"
            })

            counter += 1
        
        return {"ui": {"images": results}}
    
#------------------------------------------------------------------------------------------#
#-----Text Box-----
class HC_Text_Box:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Text": ("STRING", {"default": "", "multiline": True})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)
    FUNCTION = "text_box"
    CATEGORY = "HavocsCall/Basic"
    DESCRIPTION = "Create a string value"

    def text_box(self, Text):
        return (Text,)
