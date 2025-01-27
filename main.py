from helpers import read_csv, write_csv, assign_secret_santa


def main():
    # File paths
    employee_file = "data/employees.csv"
    last_year_file = "data/last_year.csv"
    output_file = "data/output.csv"

    try:
        # Read input files
        employees = read_csv(employee_file)
        last_year_data = read_csv(last_year_file)

        # Create a dictionary of last year's assignments
        last_year_assignments = last_year_data.set_index("Employee_Name")["Secret_Child_Name"].to_dict()

        # Assign Secret Santa pairs
        assignments = assign_secret_santa(employees, last_year_assignments)

        # Write the output to a CSV file
        write_csv(output_file, assignments)
        print(f"Secret Santa assignments saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()