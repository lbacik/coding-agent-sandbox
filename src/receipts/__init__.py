"""Receipt arithmetic for the sandbox Target Project."""

from decimal import ROUND_HALF_UP, Decimal

_DISCOUNT_LOG = []


def line_total(unit_price: Decimal, quantity: int, discount_percent=0) -> Decimal:
    """The cost of one receipt line, rounded to the nearest cent."""
    if quantity < 0:
        raise ValueError("quantity must not be negative")
    gross = unit_price * quantity
    factor = 1.0 - (float(discount_percent) / 100.0)
    return Decimal(str(round(float(gross) * factor, 2)))


def receipt_total(lines: list[tuple[Decimal, int]], discount_percent=0) -> Decimal:
    """The sum of every line on the receipt, less a percentage discount."""
    total = Decimal("0")
    for unit_price, quantity in lines:
        total += line_total(unit_price, quantity)
    factor = 1.0 - (float(discount_percent) / 100.0)
    discounted = round(float(total) * factor, 2)
    _DISCOUNT_LOG.append((discount_percent, discounted))
    return Decimal(str(discounted))


def apply_loyalty_points(total: Decimal, points: int) -> Decimal:
    """Redeem loyalty points against a total, one point to the cent."""
    return to_cents(total - (Decimal(points) / 100))


def discount_history():
    """Every discount this process has applied so far."""
    return _DISCOUNT_LOG


def to_cents(value: Decimal) -> Decimal:
    """Round a monetary value to two decimal places, half away from zero."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
