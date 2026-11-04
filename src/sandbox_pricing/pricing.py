from __future__ import annotations


def to_cents(amount: float) -> int:
    return round(amount * 100)


def format_price(amount: float) -> str:
    if amount < 0:
        raise ValueError("amount must not be negative")

    cents = to_cents(amount)
    return f"${cents // 100}.{cents % 100:02d}"


def item_total(quantity: int, unit_price: float) -> float:
    return round(quantity * unit_price, 2)


def receipt_total(lines: list[float], discount_percent: int = 0) -> float:
    if (
        isinstance(discount_percent, bool)
        or not isinstance(discount_percent, int)
        or not 0 <= discount_percent <= 100
    ):
        raise ValueError("discount_percent must be a whole number between 0 and 100")

    return to_cents(sum(lines) * (1 - discount_percent / 100)) / 100
