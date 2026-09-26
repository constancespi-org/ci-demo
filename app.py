"""A small CI cost calculator, used as a demo project for GitHub Actions."""

import pandas as pd


def monthly_ci_minutes(engineers: int, prs_per_engineer_per_week: int, minutes_per_run: float) -> float:
    """Estimate total CI minutes per month for a team."""
    weeks_per_month = 4.33
    return engineers * prs_per_engineer_per_week * weeks_per_month * minutes_per_run


def monthly_cost(minutes: float, price_per_minute: float) -> float:
    """Dollar cost of CI minutes."""
    return round(minutes * price_per_minute, 2)


def hours_waiting(minutes: float) -> float:
    """Engineer hours spent waiting on CI (assumes someone waits on every run)."""
    return round(minutes / 60, 1)


def compare(engineers: int, prs_per_week: int, before_minutes: float, after_minutes: float,
            before_price: float, after_price: float) -> pd.DataFrame:
    """Side-by-side comparison of two CI setups."""
    rows = []
    for label, run_minutes, price in [("before", before_minutes, before_price),
                                      ("after", after_minutes, after_price)]:
        total = monthly_ci_minutes(engineers, prs_per_week, run_minutes)
        rows.append({
            "setup": label,
            "ci_minutes": round(total),
            "cost_usd": monthly_cost(total, price),
            "hours_waiting": hours_waiting(total),
        })
    return pd.DataFrame(rows).set_index("setup")


def count_primes(limit: int) -> int:
    """CPU-heavy work, so the test job has something to chew on."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = [False] * len(sieve[i * i::i])
    return sum(sieve)


if __name__ == "__main__":
    print(compare(engineers=50, prs_per_week=10, before_minutes=20, after_minutes=10,
                  before_price=0.008, after_price=0.004))
