"""Pricing tests."""
import pytest
from src.models import Product, OrderItem
from src.pricing import (
    calculate_subtotal,
    apply_discount,
    calculate_tax,
    calculate_total,
)


@pytest.fixture
def sample_items():
    p1 = Product(id=1, name="Book", price=20.0, stock=10)
    p2 = Product(id=2, name="Pen", price=5.0, stock=50)
    return [
        OrderItem(product=p1, quantity=2),
        OrderItem(product=p2, quantity=3),
    ]


def test_calculate_subtotal(sample_items):
    # 2 * 20 + 3 * 5 = 55
    assert calculate_subtotal(sample_items) == 55.0


def test_apply_discount_zero(sample_items):
    subtotal = calculate_subtotal(sample_items)
    assert apply_discount(subtotal, 0) == 55.0


def test_apply_discount_ten_percent(sample_items):
    subtotal = calculate_subtotal(sample_items)
    # 55 - (55 * 0.1) = 49.5
    assert apply_discount(subtotal, 10) == 49.5


def test_apply_discount_invalid_negative():
    with pytest.raises(ValueError):
        apply_discount(100.0, -5)


def test_apply_discount_invalid_over_hundred():
    with pytest.raises(ValueError):
        apply_discount(100.0, 150)


def test_calculate_tax():
    # 100 * 0.09 = 9.0
    assert calculate_tax(100.0) == 9.0


def test_calculate_total_no_discount(sample_items):
    # subtotal=55, tax=4.95, total=59.95
    assert calculate_total(sample_items, 0) == 59.95


def test_calculate_total_with_discount(sample_items):
    # subtotal=55, after 10% discount=49.5, tax=4.455, total=53.96
    assert calculate_total(sample_items, 10) == 53.96
