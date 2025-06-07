#------------------------------------------------------------------------------------------#
#-----Math Function-----
class HC_Math_Operation:
    @classmethod
    def INPUT_TYPES(cls):
        operations = [
            "Add",
            "Subtract",
            "Multiply",
            "Divide",
            "Round"
            ]

        class AnyType(str):
            def __ne__(self, __value: object) -> bool:
                return False

        any = AnyType("*")

        return {
            "required": {
                "Number": (any, {"forceInput": True}),
                "Operation": (operations, ),
                "Constant": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            },
        }
    
    RETURN_TYPES = ("FLOAT", "INT", "INT",)
    RETURN_NAMES = ("Result Float", "Result Integer", "Constant",)
    FUNCTION = "math_operation"
    CATEGORY = "HavocsCall/Math"
    DESCRIPTION = "Runs a math operation on the input number"

    def math_operation(self, Number, Constant, Operation):
        match Operation:
            case "Add":
                result = Number + Constant
            case "Subtract":
                result = Number - Constant
            case "Multiply":
                result = Number * Constant
            case "Divide":
                if Number == 0:
                    result = 0
                else:
                    result = Number / Constant
            case "Round":
                result = round(Number)
        
        result_float = float(result)
        result_integer = int(result)
        
        return (result_float, result_integer, Constant,)
