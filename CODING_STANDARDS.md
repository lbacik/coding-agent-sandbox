# Coding standards

These rules bind every change to this repository.

1. **Money is `Decimal`, never `float`.** No monetary value, and no factor applied
   to one, may pass through a binary floating point type at any point.
2. **Rounding is explicit.** Round money with
   `value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)`. The built-in
   `round()` is banned on monetary values: it rounds half to even.
3. **Every public function is fully annotated** — every parameter and the return
   type.
4. **No module-level mutable state.** A module may hold constants; it may not
   hold a list, dict or set that anything mutates at runtime.
5. **Invalid input raises `ValueError`** with a message naming the offending
   argument. Never return a sentinel and never silently clamp.
