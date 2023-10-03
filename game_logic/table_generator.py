class TableGenerator:
    @staticmethod
    def generate_table(moves):
        table = []
        n = len(moves)
        half_n = n // 2

        for i, move in enumerate(moves):
            row = [move]  # Добавляем текущий ход как первый элемент строки
            for j, opponent in enumerate(moves):
                if i == j:
                    row.append("Draw")
                elif (i < j and j - i <= half_n) or (i > j and i - j > half_n):
                    row.append("Win")
                else:
                    row.append("Lose")
            table.append(row)

        return table
    
    @staticmethod
    def print_table(moves):
        table = TableGenerator.generate_table(moves)
        n = len(moves)
    
        # Определите максимальную длину строки хода для корректного форматирования
        max_len = max(len(move) for move in moves)
    
        # Шаблон строки
        header_format = "| {0:" + str(max_len) + "} " + " ".join(["{" + str(i+1) + ":" + str(max_len) + "}" for i in range(n)]) + " |"
        separator = "+-" + "-" * max_len + "-+" + ("-" + "-" * max_len + "-+") * n
    
        # Печать таблицы
        print(separator)
        print(header_format.format("", *moves))  # Выводим заголовок
        print(separator)
        for row in table:
            print(header_format.format(*row))
            print(separator)