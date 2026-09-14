from __future__ import annotations


def to_cents(amount: float) -> int:
    return round(amount * 100)


def item_total(quantity: int, unit_price: float) -> float:
    return round(quantity * unit_price, 2)
