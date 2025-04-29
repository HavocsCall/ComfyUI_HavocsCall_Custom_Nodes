#------------------------------------------------------------------------------------------#
#-----Math Function-----
class HC_Math_Operation:
    operations = [
        "Add",
        "Subtract",
        "Multiply",
        "Divide",
    ]

    class AnyType(str):
        def __ne__(self, __value: object) -> bool:
            return False

    any = AnyType("*")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Number_Input": (HC_Math_Operation.any, {"forceInput": True}),
                "Number": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "Operation": (HC_Math_Operation.operations, {"default": "Add"})
            },
        }
    
    RETURN_TYPES = ("FLOAT", "INT",)
    RETURN_NAMES = ("Result Float", "Result Integer",)
    FUNCTION = "math_operation"
    CATEGORY = "HavocsCall/Math"
    DESCRIPTION = "Runs a math operation on the input number"

    def math_operation(self, Number_Input, Number, Operation):
        match Operation:
            case "Add":
                result = Number_Input + Number
            case "Subtract":
                result = Number_Input - Number
            case "Multiply":
                result = Number_Input * Number
            case "Divide":
                if Number == 0:
                    result = 0
                else:
                    result = Number_Input / Number
        result_float = float(result)
        result_integer = int(result)
        return (result_float, result_integer,)
