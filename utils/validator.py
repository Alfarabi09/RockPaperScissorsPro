class MoveValidator:
    @staticmethod
    def validate_moves(moves):
        
        if len(moves) < 3 or len(moves) % 2 == 0:
            raise ValueError("Number of moves should be odd and at least 3.")
        
        
        if len(moves) != len(set(moves)):
            raise ValueError("Duplicate moves detected. All moves should be unique.")
