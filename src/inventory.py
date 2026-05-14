"""Inventory management."""
from typing import List
from src.models import OrderItem, Product


class InsufficientStockError(Exception):
    """Raised when an order exceeds available stock."""


def check_availability(items: List[OrderItem]) -> bool:
    """Return True if all items have enough stock, False otherwise."""
    for item in items:
        if item.quantity > item.product.stock:
            return False
    return True


def reserve_stock(items: List[OrderItem]) -> List[Product]:
    """Reserve stock for an order. Raises InsufficientStockError if not enough."""
    if not check_availability(items):
        raise InsufficientStockError("Not enough stock")
    updated = []
    for item in items:
        item.product.stock -= item.quantity
        updated.append(item.product)
    return updated
