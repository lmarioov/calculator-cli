class Calculator:

    def add(self, num1: float, num2: float) -> float:
        return num1 + num2
    
    def subtract(self, num1: float, num2: float) -> float:
        return num1 - num2
    
    def multiply(self, num1: float, num2: float) -> float:
        return num1 * num2
    
    def divide(self, num1: float, num2: float) -> float | str:
        if num2 == 0:
            return "Cannot divide by 0!"
        
        return num1 / num2