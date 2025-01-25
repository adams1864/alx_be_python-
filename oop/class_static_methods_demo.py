class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static Method
    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b

    # Class Method
    @classmethod
    def multiply(cls, a, b):
        """Class method to return the product of two numbers, 
        and print the class attribute calculation_type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
