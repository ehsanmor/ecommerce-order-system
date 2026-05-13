"""Order processing service."""
from src.models import Order
from src.pricing import calculate_total
from src.inventory import reserve_stock, check_availability, InsufficientStockError


def process_order(order: Order) -> dict:
    """Process an order: check stock, reserve, calculate total."""
    if not order.items:
        return {"status": "empty", "message": "Empty order"}

    if not check_availability(order.items):
        return {"status": "error", "message": "Insufficient stock"}

    try:
        reserve_stock(order.items)
    except InsufficientStockError as e:
        return {"status": "error", "message": str(e)}

    total = calculate_total(order.items, order.discount_percent)
    return {
        "status": "success",
        "order_id": order.id,
        "total": total,
    }
