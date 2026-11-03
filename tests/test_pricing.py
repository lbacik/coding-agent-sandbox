from __future__ import annotations

from sandbox_pricing.pricing import item_total, to_cents


def test_to_cents_rounds_to_nearest_cent() -> None:
    assert to_cents(19.995) == 2000


def test_item_total_multiplies_quantity_by_unit_price() -> None:
    assert item_total(3, 2.5) == 7.5


def test_item_total_rounds_to_two_decimals() -> None:
    assert item_total(3, 0.1) == 0.3


def test_item_total_applies_discount_percent() -> None:
    assert item_total(2, 10, discount_percent=25) == 15.0


def test_item_total_defaults_to_no_discount() -> None:
    assert item_total(2, 10) == 20.0


def test_item_total_rejects_discount_percent_above_100() -> None:
    try:
        item_total(2, 10, discount_percent=101)
    except ValueError as exc:
        assert "discount_percent" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_item_total_rejects_discount_percent_below_0() -> None:
    try:
        item_total(2, 10, discount_percent=-1)
    except ValueError as exc:
        assert "discount_percent" in str(exc)
    else:
        raise AssertionError("expected ValueError")


def test_item_total_rejects_non_whole_discount_percent() -> None:
    try:
        item_total(2, 10, discount_percent=12.5)
    except ValueError as exc:
        assert "discount_percent" in str(exc)
    else:
        raise AssertionError("expected ValueError")
