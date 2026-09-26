from app import compare, count_primes, hours_waiting, monthly_ci_minutes, monthly_cost


def test_monthly_ci_minutes():
    assert monthly_ci_minutes(1, 1, 10) == 43.3


def test_monthly_cost():
    assert monthly_cost(1000, 0.008) == 8.0


def test_hours_waiting():
    assert hours_waiting(120) == 2.0


def test_compare_after_is_cheaper():
    df = compare(50, 10, 20, 10, 0.008, 0.004)
    assert df.loc["after", "cost_usd"] < df.loc["before", "cost_usd"]
    assert df.loc["after", "hours_waiting"] < df.loc["before", "hours_waiting"]


def test_count_primes_small():
    assert count_primes(100) == 25


def test_count_primes_heavy():
    # Deliberately CPU-heavy so runner speed differences show up in timings.
    for _ in range(15):
        assert count_primes(5_000_000) == 348_513
