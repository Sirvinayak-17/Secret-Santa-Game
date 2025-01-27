import pandas as pd
import random


def read_csv(file_path):
    """Reads a CSV file and returns a DataFrame."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f"Error reading file {file_path}: {e}")


def write_csv(file_path, data):
    """Writes a DataFrame to a CSV file."""
    try:
        data.to_csv(file_path, index=False)
    except Exception as e:
        raise Exception(f"Error writing to file {file_path}: {e}")


def assign_secret_santa(employees, last_year_assignments):
    """
    Assign Secret Santa pairs, avoiding self-assignments and last year's assignments.
    :param employees: DataFrame of employees.
    :param last_year_assignments: Dictionary of last year's Secret Santa pairs.
    :return: DataFrame of Secret Santa assignments.
    """
    available = employees["Employee_Name"].tolist()
    assignments = []

    for index, row in employees.iterrows():
        giver_name = row["Employee_Name"]
        giver_email = row["Employee_EmailID"]

        # Filter out the giver and last year's assignment
        options = [
            person for person in available
            if person != giver_name and person not in last_year_assignments.get(giver_name, [])
        ]

        if not options:
            raise ValueError(f"Cannot assign Secret Santa for {giver_name}")

        # Randomly pick a Secret Santa
        secret_child = random.choice(options)
        available.remove(secret_child)

        # Find email for the assigned child
        secret_child_email = employees.loc[
            employees["Employee_Name"] == secret_child, "Employee_EmailID"
        ].values[0]

        # Save the assignment
        assignments.append({
            "Employee_Name": giver_name,
            "Employee_EmailID": giver_email,
            "Secret_Child_Name": secret_child,
            "Secret_Child_EmailID": secret_child_email
        })

    return pd.DataFrame(assignments)