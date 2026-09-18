# Build: 2674800bfc73f253ce00fbbc79a6a830

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
