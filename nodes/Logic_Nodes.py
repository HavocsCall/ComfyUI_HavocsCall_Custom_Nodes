#------------------------------------------------------------------------------------------#
#-----Logic Compare-----
class HC_Logic_Compare:
    @classmethod
    def INPUT_TYPES(cls):
        operations = [
            "Find Greater",
            "Find Lesser",
            "Find Average"
            ]
        
        class AnyType(str):
            def __ne__(self, __value: object) -> bool:
                return False
        
        any = AnyType("*")
    
        return {
            "required": {
                "Number_1": (any, {"forceInput": True}),
                "Number_2": (any, {"forceInput": True}),
                "Operation": (operations,),
            },
        }
    
    RETURN_TYPES = ("FLOAT", "INT",)
    RETURN_NAMES = ("Result Float", "Result Integer",)
    FUNCTION = "compare_numbers"
    CATEGORY = "HavocsCall/Logic"
    DESCRIPTION = "Compares two numbers based on the selected operation."

    def compare_numbers(self, Number_1, Number_2, Operation):
        match Operation:
            case "Find Greater":
                result = max(Number_1, Number_2)
            case "Find Lesser":
                result = min(Number_1, Number_2)
            case "Find Average":
                result = (Number_1 + Number_2) / 2
        
        result_float = float(result)
        result_integer = int(result)

        return (result_float, result_integer,)