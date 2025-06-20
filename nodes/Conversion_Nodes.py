#------------------------------------------------------------------------------------------#
#-----Float to Integer-----
class HC_Float_to_Integer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Float": ("FLOAT", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("Integer",)
    FUNCTION = "float_to_integer"
    CATEGORY = "HavocsCall/Conversion"
    DESCRIPTION = "Rounds, then converts a float to an integer."

    def float_to_integer(self, Float,):
        result = int(Float)
        return (result,)

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
        result = str(Float)
        return (result,)

#------------------------------------------------------------------------------------------#
#-----Integer to Float-----
class HC_Integer_to_Float:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Integer": ("INT", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("Float",)
    FUNCTION = "integer_to_float"
    CATEGORY = "HavocsCall/Conversion"
    DESCRIPTION = "Convert an integer to a float."

    def integer_to_float(self, Integer,):
        result = float(Integer)
        return (result,)

#------------------------------------------------------------------------------------------#
#-----Integer to String-----
class HC_Integer_to_String:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Integer": ("INT", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("String",)
    FUNCTION = "integer_to_string"
    CATEGORY = "HavocsCall/Conversion"
    DESCRIPTION = "Convert an integer to a string."

    def integer_to_string(self, Integer,):
        result = str(Integer)
        return (result,)

#------------------------------------------------------------------------------------------#
#-----String to Float-----
class HC_String_to_Float:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "String": ("STRING", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("Float",)
    FUNCTION = "string_to_float"
    CATEGORY = "HavocsCall/Conversion"
    DESCRIPTION = "Convert a string to a float."

    def string_to_float(self, String,):
        try:
            result = float(String)
        except ValueError:
            print("String to Float conversion failed. Returning 0.")
            result = 0.0
        return (result,)

#------------------------------------------------------------------------------------------#
#-----String to Integer-----
class HC_String_to_Integer:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "String": ("STRING", {"forceInput": True})
            }
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("Integer",)
    FUNCTION = "string_to_int"
    CATEGORY = "HavocsCall/Conversion"
    DESCRIPTION = "Convert a string to an int."

    def string_to_int(self, String,):
        try:
            result = int(String)
        except ValueError:
            print("String to Integer conversion failed. Returning 0.")
            result = 0
        return (result,)
