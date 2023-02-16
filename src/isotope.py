from dataclasses import dataclass

@dataclass
class Isotope:
    id: str
    name: str
    symbol: str
    protons: int
    neutrons: int
    mass: float
    abundance: float # % of the population

