class Converter:
    def convert_text_to_list(self, text):
        text = ' ' + text
        tempList = []
        temp = ''
        i = 0
        while i < len(text):
            # склейка цифр
            if text[i].isdigit():
                temp = text[i]
                j = 1
                while i + j < len(text) and text[i+j].isdigit():
                    temp += text[i+j]
                    j += 1
                tempList.append(temp)
                i += j
            elif text[i] in ['+', '-', '*', '/', '(', ')']:
                tempList.append(text[i])
                i += 1
            else:
                i += 1

        resultList = []
        for i in tempList:
            try:
                resultList.append(int(i))
            except ValueError:
                resultList.append(i)

        return resultList
