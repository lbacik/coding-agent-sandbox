from __future__ import annotations

import pytest

from sandbox_pricing.pricing import format_price, item_total, to_cents


def test_to_cents_rounds_to_nearest_cent() -> None:
    assert to_cents(19.995) == 2000


def test_item_total_multiplies_quantity_by_unit_price() -> None:
    assert item_total(3, 2.5) == 7.5


def test_item_total_rounds_to_two_decimals() -> None:
    assert item_total(3, 0.1) == 0.3


def test_format_price_adds_dollar_sign_and_two_decimals() -> None:
    assert format_price(7.5) == "$7.50"


def test_format_price_formats_zero() -> None:
    assert format_price(0) == "$0.00"


def test_format_price_rounds_through_to_cents() -> None:
    assert format_price(19.995) == "$20.00"


def test_format_price_rejects_negative_amount() -> None:
    with pytest.raises(ValueError, match="amount"):
        format_price(-1)
