"""Pricing and discount calculations."""
from typing import List
from src.models import OrderItem


def calculate_subtotal(items: List[OrderItem]) -> float:
    """Sum of (price * quantity) for each item."""
    return sum(item.product.price * item.quantity for item in items)


def apply_discount(subtotal: float, discount_percent: float) -> float:
    """Apply a percentage discount to a subtotal."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    discount_amount = subtotal * (discount_percent / 100)
    return subtotal - discount_amount


def calculate_tax(amount: float, tax_rate: float = 0.09) -> float:
    """Calculate tax on an amount."""
    return amount * tax_rate


def calculate_total(items: List[OrderItem], discount_percent: float = 0.0) -> float:
    """Calculate final order total including discount and tax."""
    subtotal = calculate_subtotal(items)
    after_discount = apply_discount(subtotal, discount_percent)
    tax = calculate_tax(after_discount)
    return round(after_discount + tax, 2)