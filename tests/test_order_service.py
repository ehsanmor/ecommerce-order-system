"""Order service tests."""

from src.models import Product, OrderItem, Order
from src.order_service import process_order


def test_process_empty_order():
    order = Order(id=1, customer_id=100, items=[])
    result = process_order(order)
    assert result["status"] == "error"
    assert "Empty" in result["message"]


def test_process_successful_order():
    p = Product(id=1, name="Book", price=20.0, stock=10)
    items = [OrderItem(product=p, quantity=2)]
    order = Order(id=1, customer_id=100, items=items, discount_percent=0)
    result = process_order(order)
    assert result["status"] == "success"
    # 2*20=40, tax=3.6, total=43.6
    assert result["total"] == 43.6


def test_process_order_with_discount():
    p = Product(id=1, name="Book", price=100.0, stock=10)
    items = [OrderItem(product=p, quantity=1)]
    order = Order(id=1, customer_id=100, items=items, discount_percent=20)
    result = process_order(order)
    assert result["status"] == "success"
    # 100, after 20% = 80, tax = 7.2, total = 87.2
    assert result["total"] == 87.2


def test_process_order_insufficient_stock():
    p = Product(id=1, name="Book", price=20.0, stock=1)
    items = [OrderItem(product=p, quantity=5)]
    order = Order(id=1, customer_id=100, items=items)
    result = process_order(order)
    assert result["status"] == "error"
    assert "stock" in result["message"].lower()
