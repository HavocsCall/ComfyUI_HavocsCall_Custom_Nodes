#------------------------------------------------------------------------------------------#
#-----Float to Int-----
class HC_Float_to_Int:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Float": ("FLOAT", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("Integer",)
    FUNCTION = "float_to_int"
    CATEGORY = "HavocsCall/Conversion"
    DESCRIPTION = "Rounds, then converts a float to an int."

    def float_to_int(self, Float,):
        return (round(Float),)

#------------------------------------------------------------------------------------------#
#-----Float to String-----
class HC_Float_to_String:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Float": ("FLOAT", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("String",)
    FUNCTION = "float_to_string"
    CATEGORY = "HavocsCall/Conversion"
    DESCRIPTION = "Convert a float to a string."

    def float_to_string(self, Float,):
        return (str(Float),)

#------------------------------------------------------------------------------------------#
#-----Int to Float-----
class HC_Int_to_Float:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Integer": ("INT", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("Float",)
    FUNCTION = "int_to_float"
    CATEGORY = "HavocsCall/Conversion"
    DESCRIPTION = "Convert an int to a float."

    def int_to_float(self, Integer,):
        return (float(Integer),)

#------------------------------------------------------------------------------------------#
#-----Int to String-----
class HC_Int_to_String:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Integer": ("INT", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("String",)
    FUNCTION = "int_to_string"
    CATEGORY = "HavocsCall/Conversion"
    DESCRIPTION = "Convert an int to a string."

    def int_to_string(self, Integer,):
        return (str(Integer),)
