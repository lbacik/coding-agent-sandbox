from __future__ import annotations

import pytest

from sandbox_pricing.pricing import from_cents, item_total, to_cents


def test_to_cents_rounds_to_nearest_cent() -> None:
    assert to_cents(19.995) == 2000


def test_from_cents_converts_positive_amount() -> None:
    assert from_cents(1999) == 19.99


def test_from_cents_converts_zero() -> None:
    assert from_cents(0) == 0.0


def test_from_cents_converts_negative_amount() -> None:
    assert from_cents(-150) == -1.5


def test_from_cents_rejects_non_int() -> None:
    with pytest.raises(ValueError):
        from_cents(19.99)


def test_from_cents_rejects_bool() -> None:
    with pytest.raises(ValueError):
        from_cents(True)


def test_item_total_multiplies_quantity_by_unit_price() -> None:
    assert item_total(3, 2.5) == 7.5


def test_item_total_rounds_to_two_decimals() -> None:
    assert item_total(3, 0.1) == 0.3
