#------------------------------------------------------------------------------------------#
#-----Combine String-----
class HC_Combine_String:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "String_1": ("STRING", {"forceInput": True}),
                "String_2": ("STRING", {"forceInput": True}),
                "Separator": ("STRING", {"default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Combined_String",)
    FUNCTION = "combine_string"
    CATEGORY = "HavocsCall/Combination"
    DESCRIPTION = "Combine two strings into one."
    
    def combine_string(self, String_1, String_2, Separator):
        combined_String = String_1 + Separator + String_2
        return (combined_String,)