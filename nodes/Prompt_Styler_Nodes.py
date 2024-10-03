import json
import pathlib
from collections import defaultdict

#------------------------------------------------------------------------------------------#
#-----Prompt Styler-----
# This is copied from https://github.com/TripleHeadedMonkey/ComfyUI_MileHighStyler, thank you very much.
# I am learning about this and will recreate it in the future.
class Template:
    def __init__(self, positive_prompt, negative_prompt, **kwargs):
        self.positive_prompt = positive_prompt
        self.negative_prompt = negative_prompt

    def replace_prompts(self, positive_prompt, negative_prompt):
        positive_result = self.positive_prompt.replace('{prompt}', positive_prompt)
        negative_result = self.negative_prompt.replace('{prompt}', negative_prompt)
        return positive_result, negative_result


class StylerData:
    def __init__(self, datadir=None):

        self._data = defaultdict(dict)
        datadir = pathlib.Path(__file__).parent / 'styler_data'

        for j in datadir.glob('*/*.json'):
            try:
                with j.open('r') as f:
                    content = json.load(f)
                    group = j.parent.name
                    for template in content:
                        self._data[group][template['name']] = Template(**template)
            except PermissionError:
                print(f"Warning: No read permissions for file {j}")
            except KeyError:
                print(f"Warning: Malformed data in {j}")

    def __getitem__(self, item):
        return self._data[item]

    def keys(self):
        return self._data.keys()

styler_data = StylerData()

class SDXLPromptStyler:
    menus = ()

    @classmethod
    def INPUT_TYPES(cls):

        menus = {menu: (list(styler_data[menu].keys()), ) for menu in cls.menus}

        inputs = {
            "required": {
                "text_positive": ("STRING", {"default": "", "forceInput": True}),
                "text_negative": ("STRING", {"default": "", "forceInput": True}),
                **menus,
            },
        }
        return inputs

    RETURN_TYPES = ('STRING','STRING',)
    RETURN_NAMES = ('text_positive','text_negative',)

    FUNCTION = 'prompt_styler'
    
    CATEGORY = 'HavocsCall/Prompt Stylers'

    def prompt_styler(self, text_positive, text_negative, **kwargs):
        text_positive_styled, text_negative_styled = text_positive, text_negative
        for menu, selection in kwargs.items():
            text_positive_styled, text_negative_styled = styler_data[menu][selection].replace_prompts(text_positive_styled, text_negative_styled)
        return text_positive_styled, text_negative_styled

NODES = {
    # define your nodes here
    # first the friendly name, then a sequence of strings
    # corresponding to subdirectories of the data dir.

    # individual stylers have one menu item
    # build them automatically from the scanned directories
    **{f'{name.title()} Styler': (name, ) for name in styler_data.keys()},

    # alternatively you can list every single-menu node like this:
    # 'Camera Styler': ('camera', ),
    # etc...

    # perfection styler has everything except artist and milehigh
    # we can define it by excluding those
    # downside of this method is you have no control over the order
    #'Perfection Styler': [x for x in styler_data.keys() if x not in ('artist', 'milehigh')],

    # alternatively define it manually, and you can reorder the items
}

for k, v in NODES.items():
    assert not isinstance(v, str), f"Error: {k} has a string instead of a sequence for its menu list. Did you forget a comma?"