#------------------------------------------------------------------------------------------#
# For HC_Prompt_Styler
import json
from pathlib import Path

#------------------------------------------------------------------------------------------#
#-----Prompt Styler-----
class HC_Prompt_Styler:
    # Set a None option
    none_json = '''
    [
        {
            "Name": "None",
            "Positive_Style": "{prompt}",
            "Negative_Style": "{prompt}"
        }
    ]
    '''
    # Get the styles directory
    styles_dir = Path(__file__).parent / "Styler Data"

    # Load all of the json data from the styles directory
    json_data = json.loads(none_json)
    
    for file in styles_dir.glob("*.json"):
        if file.name != "Example.json":
            with open(file, "r") as f:
                try:
                    data = json.load(f)
                    # Add the file name as a prefix to the name of each style
                    for style_name in data:
                        style_name["Name"] = f"{file.stem} - {style_name['Name']}"
                    json_data.extend(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {file}: {e}")

    # Get the style names and add a suffix number to duplicates
    style_names = []
    name_count = {}

    for style in json_data:
        name = style["Name"]
        if name in name_count:
            name_count[name] += 1
            name = f"{name} {name_count[name]}"
            style["Name"] = name
        else:
            name_count[name] = 1
        style_names.append(name)

    # Alphabetize style names but keep "None" at the top
    style_names = sorted(style_names, key=lambda name: (name != "None", name))

    # Function to style the prompt
    def style_prompt(self, prompt, style):
        styled_prompt = style.replace("{prompt}", prompt)
        return styled_prompt

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Positive_Prompt": ("STRING", {"forceInput": True}),
                "Negative_Prompt": ("STRING", {"forceInput": True}),
                "Style": (HC_Prompt_Styler.style_names,),
                "Style_Positive": ("BOOLEAN", {"default": True, "label_on": "Yes", "label_off": "No", "tooltip": "Apply the style to the positive prompt"}),
                "Style_Negative": ("BOOLEAN", {"default": True, "label_on": "Yes", "label_off": "No", "tooltip": "Apply the style to the negative prompt"}),
                "Log_Prompts": ("BOOLEAN", {"default": False, "label_on": "Yes", "label_off": "No", "tooltip": "Log the prompt (before and after)"})
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("Styled_Positive_Prompt", "Styled_Negative_Prompt")
    FUNCTION = "prompt_styler"
    CATEGORY = "HavocsCall/Prompt Styler"
    DESCRIPTION = "Style prompts using a style from the json data."

    def prompt_styler(self, Positive_Prompt, Negative_Prompt, Style, Style_Positive, Style_Negative, Log_Prompts):
        # Get the style data from the json data
        style_dict = {item["Name"]: item for item in self.json_data}
        style_data = style_dict.get(Style)

        # Get the positive and negative styles from the json data
        positive_style = style_data["Positive_Style"]
        negative_style = style_data["Negative_Style"]

        # Apply the styles to the prompts
        styled_positive = self.style_prompt(Positive_Prompt, positive_style) if Style_Positive else Positive_Prompt
        styled_negative = self.style_prompt(Negative_Prompt, negative_style) if Style_Negative else Negative_Prompt

        # Log the prompts if requested
        if Log_Prompts:
            print(f"-----PROMPT VALUES-----:")
            print(f'Positive Prompt: {Positive_Prompt}')
            print(f'Negative Prompt: {Negative_Prompt}')
            print(f'Styled Positive: {styled_positive}')
            print(f'Styled Negative: {styled_negative}')
            print()
        
        return (styled_positive, styled_negative)
