from Model.Calculator import Calculator
from Model.Converter import Converter


class Model:
    def calculate(self, expression):
        convertor = Converter()
        calculator = Calculator()

        temp_list = convertor.convert_text_to_list(expression)
        result = calculator.calculate(temp_list)
        return result
