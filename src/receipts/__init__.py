"""Receipt arithmetic for the sandbox Target Project."""

from decimal import ROUND_HALF_UP, Decimal


def line_total(unit_price: Decimal, quantity: int) -> Decimal:
    """The cost of one receipt line, rounded to the nearest cent."""
    if quantity < 0:
        raise ValueError("quantity must not be negative")
    return to_cents(unit_price * quantity)


def receipt_total(lines: list[tuple[Decimal, int]]) -> Decimal:
    """The sum of every line on the receipt."""
    total = Decimal("0")
    for unit_price, quantity in lines:
        total += line_total(unit_price, quantity)
    return to_cents(total)


def to_cents(value: Decimal) -> Decimal:
    """Round a monetary value to two decimal places, half away from zero."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
