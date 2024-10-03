#------------------------------------------------------------------------------------------#
#-----Float to Int-----
class HC_Float_to_Int:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Float": ("FLOAT", {
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("Integer",)

    FUNCTION = "Float_to_Int"

    OUTPUT_NODE = True

    CATEGORY = "HavocsCall/Conversion"

    def Float_to_Int(self, Float,):
        return (round(Float),)

#------------------------------------------------------------------------------------------#
#-----Float to String-----
class HC_Float_to_String:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Float": ("FLOAT", {
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("String",)

    FUNCTION = "Float_to_String"

    OUTPUT_NODE = True 

    CATEGORY = "HavocsCall/Conversion"

    def Float_to_String(self, Float,):
        return (str(Float),)

#------------------------------------------------------------------------------------------#
#-----Int to Float-----
class HC_Int_to_Float:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Integer": ("INT", {
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("Float",)

    FUNCTION = "Int_to_Float"

    OUTPUT_NODE = True

    CATEGORY = "HavocsCall/Conversion"

    def Int_to_Float(self, Integer,):
        return (float(Integer),)

#------------------------------------------------------------------------------------------#
#-----Int to String-----
class HC_Int_to_String:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Integer": ("INT", {
                    "forceInput": True
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("String",)

    FUNCTION = "Int_to_String"

    OUTPUT_NODE = True

    CATEGORY = "HavocsCall/Conversion"

    def Int_to_String(self, Integer,):
        return (str(Integer),)