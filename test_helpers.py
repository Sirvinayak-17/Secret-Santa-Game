import pytest
import pandas as pd
from helpers import assign_secret_santa


def test_assign_secret_santa():
    # Mock data
    employees = pd.DataFrame({
        "Employee_Name": ["Alice", "Bob", "Charlie", "David"],
        "Employee_EmailID": ["alice@example.com", "bob@example.com", "charlie@example.com", "david@example.com"]
    })
    last_year = {
        "Alice": ["Bob"],
        "Bob": ["Charlie"],
        "Charlie": ["David"],
        "David": ["Alice"]
    }

    # Call the function
    assignments = assign_secret_santa(employees, last_year)

    # Assert each employee has a unique child, no one is assigned themselves
    assert len(assignments) == len(employees)
    assert all(assignments["Employee_Name"] != assignments["Secret_Child_Name"])