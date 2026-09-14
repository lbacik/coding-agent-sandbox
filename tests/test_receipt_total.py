from __future__ import annotations

import pytest

from sandbox_pricing.pricing import receipt_total


def test_receipt_total_applies_percentage_discount_to_summed_lines() -> None:
    assert receipt_total([19.99, 10.00], 10) == 26.99


def test_receipt_total_rejects_discount_above_100() -> None:
    with pytest.raises(ValueError, match="discount_percent"):
        receipt_total([10.00], 101)


def test_receipt_total_has_no_discount_by_default() -> None:
    assert receipt_total([4.25, 5.75]) == 10.00


def test_receipt_total_rejects_discount_below_zero() -> None:
    with pytest.raises(ValueError, match="discount_percent"):
        receipt_total([10.00], -1)


def test_receipt_total_rejects_fractional_discount() -> None:
    with pytest.raises(ValueError, match="discount_percent"):
        receipt_total([10.00], 12.5)


def test_receipt_total_rounds_discounted_amount_to_cents() -> None:
    assert receipt_total([19.99], 25) == 14.99
