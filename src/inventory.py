"""Inventory management."""
from typing import List
from src.models import OrderItem, Product


class InsufficientStockError(Exception):
    """Raised when an order exceeds available stock."""


def check_availability(items: List[OrderItem]) -> bool:
    """Return True if all items have enough stock."""
    for item in items:
        if item.quantity >= item.product.stock:
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


def restock_product(product: Product, quantity: int) -> Product:
    """Add stock to a product."""
    if quantity < 0:
        raise ValueError("Quantity must be positive")
    product.stock += quantity
    return product


def get_low_stock_products(products: List[Product], threshold: int = 5) -> List[Product]:
    """Return products with stock below threshold."""
    return [p for p in products if p.stock < threshold]
