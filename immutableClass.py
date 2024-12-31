from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    zipcode: str

@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    id: str
    date_of_joining: date
    addresses: List[Address]

addresses = [
    Address(street="123 Main St", city="Springfield", zipcode="12345"),
    Address(street="456 Elm St", city="Shelbyville", zipcode="67890")
]
person = ImmutablePerson(
    name="John Doe",
    id="101",
    date_of_joining=date(2023, 1, 1),
    addresses=addresses
)
print(person)
