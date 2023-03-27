class Calculator:
    # Метод который считает + - * /
    def calculate_simple_operations(self, lst):
        temp = 0
        # Умножение
        while '*' in lst:
            index = lst.index('*')
            temp = lst[index - 1] * lst[index + 1]
            lst[index - 1:index + 2] = [temp]
        # Деление
        while '/' in lst:
            index = lst.index('/')
            temp = lst[index - 1] / lst[index + 1]
            lst[index - 1:index + 2] = [temp]
        # Сложение
        while '+' in lst:
            index = lst.index('+')
            try:
                temp = lst[index - 1] + lst[index + 1]
            except IndexError:
                raise ValueError("Invalid input expression")
            lst[index - 1:index + 2] = [temp]
        # Вычитание
        while '-' in lst:
            index = lst.index('-')
            try:
                temp = lst[index - 1] - lst[index + 1]
            except IndexError:
                raise ValueError("Invalid input expression")
            lst[index - 1:index + 2] = [temp]
        return lst[0]

    # Метод который считает с учетом скобок
    def calculate(self, lst):
        tempList = []
        if '(' in lst or ')' in lst:
            # находим первую закрывающую скобку
            first_close_parenthesis_index = lst.index(')')
            # находим последнюю открывающую скобку
            i = first_close_parenthesis_index - 1
            while i >= 0:
                if lst[i] == '(':
                    break
                i -= 1
            # добавляем элементы между скобками во временный список, вычисляем, заменяем и удаляем скобки
            for j in range(i+1, first_close_parenthesis_index):
                tempList.append(lst[j])
            lst[i:first_close_parenthesis_index+1] = [self.calculate_simple_operations(tempList)]
            # рекурсия позволяет вычислить и удалить все скобки
            return self.calculate(lst)
        else:
            return self.calculate_simple_operations(lst)
