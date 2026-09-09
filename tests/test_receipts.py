from decimal import Decimal

import pytest

from receipts import line_total, receipt_total


def test_line_total_multiplies() -> None:
    assert line_total(Decimal("2.50"), 3) == Decimal("7.50")


def test_line_total_rejects_negative_quantity() -> None:
    with pytest.raises(ValueError):
        line_total(Decimal("2.50"), -1)


def test_receipt_total_sums_lines() -> None:
    lines = [(Decimal("2.50"), 3), (Decimal("1.05"), 2)]
    assert receipt_total(lines) == Decimal("9.60")
