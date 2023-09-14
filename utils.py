class Utils:
    
    @staticmethod
    def reversed(number: int) -> int:
        return int(str(number)[::-1])
    
    @staticmethod
    def formatter(number: int) -> tuple:
        binary_format = bin(number)
        octal_format = oct(number)
        return binary_format, octal_format