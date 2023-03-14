class Item:
    def __init__(self,id: int, name: str, price: float, measure_unit: str) -> None:
        self.id=id
        self.name= name
        self.price= price
        self.measure_unit=measure_unit
    
    def __str__(self) -> str:
        return f"{self.name}: ${self.price}/{self.measure_unit}"