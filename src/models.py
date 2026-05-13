"""Data models for the order system."""
from dataclasses import dataclass, field
from typing import List
from datetime import datetime


@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int


@dataclass
class OrderItem:
    product: Product
    quantity: int


@dataclass
class Order:
    id: int
    customer_id: int
    items: List[OrderItem] = field(default_factory=list)
    discount_percent: float = 0.0
    created_at: datetime = field(default_factory=datetime.now)
