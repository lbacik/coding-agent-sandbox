from __future__ import annotations

from sandbox_pricing.pricing import item_total, to_cents


def test_to_cents_rounds_to_nearest_cent() -> None:
    assert to_cents(19.995) == 2000


def test_item_total_multiplies_quantity_by_unit_price() -> None:
    assert item_total(3, 2.5) == 7.5


def test_item_total_rounds_to_two_decimals() -> None:
    assert item_total(3, 0.1) == 0.3
