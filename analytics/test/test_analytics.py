from datetime import datetime
import pytest
from analytics import analytics

def test_case_one():
    now = datetime(2019, 10, 10, 10, 10, 10)
    result = analytics.length_of_storage_time_in_seconds(now)
    assert 600 == result