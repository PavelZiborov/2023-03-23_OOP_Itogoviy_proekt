from Model.Model import Model
from View.ConsoleView import ConsoleView


class Presenter:
    def button_click(self):
        view = ConsoleView()
        model = Model()
        expression = view.get_expression("Введите выражение: ")
        result = model.calculate(expression)
        view.print_result(result)

