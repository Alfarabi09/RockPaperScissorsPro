from prettytable import PrettyTable

class TableGenerator:
    @staticmethod
    def generate_table(moves):
        table = []
        n = len(moves)
        half_n = n // 2

        for i, move in enumerate(moves):
            row = [move]  
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

        
        ptable = PrettyTable()
        ptable.field_names = ["Move"] + moves

        
        for row in table:
            ptable.add_row(row)
        
        
        print(ptable)