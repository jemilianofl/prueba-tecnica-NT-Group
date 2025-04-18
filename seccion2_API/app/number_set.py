class NumberSet:
    def __init__(self):
        self.full_set = set(range(1, 101))
        self.current_set = self.full_set.copy()
        self.extracted = None

    def extract(self, number):
        if not isinstance(number, int):
            raise ValueError("El número debe ser un entero.")
        if number < 1 or number > 100:
            raise ValueError("El número debe estar entre 1 y 100.")
        if number not in self.current_set:
            raise ValueError("El número ya fue extraído o no está en el conjunto.")
        
        self.current_set.remove(number)
        self.extracted = number
        return self.extracted

    def find_missing(self):
        # Return the last extracted number
        return self.extracted
    
    def get_extracted_numbers(self):
        return sorted(list(self.full_set - self.current_set))
