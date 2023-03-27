class ConsoleView:

    def __init__(self):
        self.result = None

    def print_result(self, result):
        print(result)
        self.result = result


    def get_expression(self, msg):
        print(msg)
        return input()
