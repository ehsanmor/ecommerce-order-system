"""Inventory tests."""
import pytest
from src.models import Product, OrderItem
from src.inventory import check_availability, reserve_stock, InsufficientStockError


def test_check_availability_sufficient():
    p = Product(id=1, name="Book", price=10.0, stock=10)
    items = [OrderItem(product=p, quantity=5)]
    assert check_availability(items) is True


def test_check_availability_insufficient():
    p = Product(id=1, name="Book", price=10.0, stock=3)
    items = [OrderItem(product=p, quantity=5)]
    assert check_availability(items) is False


def test_reserve_stock_success():
    p = Product(id=1, name="Book", price=10.0, stock=10)
    items = [OrderItem(product=p, quantity=3)]
    reserve_stock(items)
    assert p.stock == 7


def test_reserve_stock_failure():
    p = Product(id=1, name="Book", price=10.0, stock=2)
    items = [OrderItem(product=p, quantity=5)]
    with pytest.raises(InsufficientStockError):
        reserve_stock(items)
