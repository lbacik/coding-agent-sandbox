from __future__ import annotations

from sandbox_pricing.pricing import item_total, to_cents


def test_to_cents_rounds_to_nearest_cent() -> None:
    assert to_cents(19.995) == 2000


def test_item_total_multiplies_quantity_by_unit_price() -> None:
    assert item_total(3, 2.5) == 7.5


def test_item_total_rounds_to_two_decimals() -> None:
    assert item_total(3, 0.1) == 0.3


def test_item_total_applies_bulk_discount() -> None:
    assert item_total(10, 2.0, discount_percent=10) == 18.0


def test_item_total_rejects_discount_above_100() -> None:
    try:
        item_total(10, 2.0, discount_percent=101)
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "discount_percent" in str(exc)


def test_item_total_rejects_negative_discount() -> None:
    try:
        item_total(10, 2.0, discount_percent=-1)
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "discount_percent" in str(exc)


def test_item_total_rounds_discounted_total_to_two_decimals() -> None:
    assert item_total(3, 1.0, discount_percent=10) == 2.7
