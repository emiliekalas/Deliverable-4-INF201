class Temperature:

    _TOLERANCE = 1e-9
    _VALID_UNITS = {"C", "F", "K"}


    def __init__(self, value: float, unit: str):
        unit = unit.upper()
        if unit not in self._VALID_UNITS:
            raise ValueError(f"Invalid unit '{unit}'. Valid units are: {', '.join(self._VALID_UNITS)}")
        self._value = value
        self._unit = unit


    @property
    def value(self) -> float:
        return self._value

    @property
    def unit(self) -> str:
        return self._unit



    def to_celsius(self) -> float:
        if self._unit == "C":
            return self._value
        elif self._unit == "F":
            return (self._value - 32) * 5 / 9
        elif self._unit == "K":
            return self._value - 273.15

    def to_fahrenheit(self) -> float:  
        if self._unit == "C":
            return (self._value * 9 / 5) + 32
        elif self._unit == "F":
            return self._value
        elif self._unit == "K":
            return (self._value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        if self._unit == "C":
            return self._value + 273.15
        elif self._unit == "F":
            return (self._value - 32) * 5 / 9 + 273.15
        elif self._unit == "K":
            return self._value
        
  

    
    
