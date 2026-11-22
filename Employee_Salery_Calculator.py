
# Function 1: Calculate House Rent
def calculate_house_rent(basic_salary):
    house_rent = basic_salary * 40 / 100
    return house_rent


# Function 2: Calculate Medical Allowance
def calculate_medical_allowance(basic_salary):
    medical_allowance = basic_salary * 10 / 100
    return medical_allowance


# Function 3: Calculate Gross Salary
def calculate_gross_salary(basic_salary, house_rent, medical_allowance):
    gross_salary = basic_salary + house_rent + medical_allowance
    return gross_salary


# Function 4: Calculate Tax
def calculate_tax(gross_salary):

    if gross_salary >= 50000:
        tax = gross_salary * 10 / 100

    elif gross_salary >= 30000:
        tax = gross_salary * 5 / 100

    else:
        tax = 0

    return tax


# Function 5: Calculate Net Salary
def calculate_net_salary(gross_salary, tax):
    net_salary = gross_salary - tax
    return net_salary


# Function 6: Add Employee Salary
def add_employee_salary():

    print("\n========== ADD EMPLOYEE SALARY ==========")

    # Take Employee Information
    employee_name = input("Enter Employee Name: ").strip()
    employee_id = input("Enter Employee ID: ").strip()
    designation = input("Enter Designation: ").strip()

    # Validate Employee Information
    if not employee_name or not employee_id or not designation:
        print("\nError: Employee information cannot be empty!")
        return

    # Input and Validate Basic Salary
    try:
        basic_salary = float(input("Enter Basic Salary: "))

        if not (basic_salary > 0 and basic_salary < float("inf")):
            print("\nError: Basic Salary must be a positive number!")
            return

    except ValueError:
        print("\nError: Please enter a valid numeric salary!")
        return

    # Calculate House Rent
    house_rent = calculate_house_rent(basic_salary)

    # Calculate Medical Allowance
    medical_allowance = calculate_medical_allowance(basic_salary)

    # Calculate Gross Salary
    gross_salary = calculate_gross_salary(
        basic_salary, house_rent, medical_allowance
    )

    # Calculate Tax
    tax = calculate_tax(gross_salary)

    # Calculate Net Salary
    net_salary = calculate_net_salary(gross_salary, tax)

    # Display Employee Salary Details
    print("\n========== EMPLOYEE SALARY DETAILS ==========")
    print("Employee Name      :", employee_name)
    print("Employee ID        :", employee_id)
    print("Designation        :", designation)
    print("---------------------------------------------")
    print("Basic Salary       : Tk.", round(basic_salary, 2))
    print("House Rent (40%)   : Tk.", round(house_rent, 2))
    print("Medical Allowance  : Tk.", round(medical_allowance, 2))
    print("---------------------------------------------")
    print("Gross Salary       : Tk.", round(gross_salary, 2))
    print("Tax                : Tk.", round(tax, 2))
    print("---------------------------------------------")
    print("Net Salary         : Tk.", round(net_salary, 2))
    print("=============================================")

    # Store Employee Record in List
    employee_record = {
        "name": employee_name,
        "id": employee_id,
        "designation": designation,
        "gross_salary": gross_salary,
        "tax": tax,
        "net_salary": net_salary
    }

    salary_records.append(employee_record)

    print("\nSuccess: Employee salary record added successfully!")


# Function 7: View All Salary Records
def view_all_records():

    print("\n========== ALL EMPLOYEE SALARY RECORDS ==========")

    if len(salary_records) == 0:
        print("No employee salary records found!")

    else:

        for index, record in enumerate(salary_records, start=1):

            print(f"\n========== EMPLOYEE {index} ==========")
            print("Employee Name :", record["name"])
            print("Employee ID   :", record["id"])
            print("Designation   :", record["designation"])
            print("Gross Salary  : Tk.", round(record["gross_salary"], 2))
            print("Tax           : Tk.", round(record["tax"], 2))
            print("Net Salary    : Tk.", round(record["net_salary"], 2))
            print("---------------------------------------------")

    # Display Total Number of Records
    print("\nTotal Salary Records Saved:", len(salary_records))


# Main Function: Menu-Driven Interface
def main():

    while True:

        print("\n=============================================")
        print("          EMPLOYEE SALARY CALCULATOR")
        print("=============================================")
        print("1. Add Employee Salary")
        print("2. View All Records")
        print("3. Exit")
        print("=============================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_employee_salary()

        elif choice == "2":
            view_all_records()

        elif choice == "3":
            print("\nThank you for using Employee Salary Calculator!")
            print("Program exited successfully.")
            break

        else:
            print("\nInvalid Choice! Please select 1, 2, or 3.")


# Global List to Store Salary Records
salary_records = []


# Program Execution
if __name__ == "__main__":
    main()
