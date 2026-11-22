
# Function 1: Calculate Units Consumed
def calculate_units(previous_reading, current_reading):
    units = current_reading - previous_reading
    return units


# Function 2: Calculate Energy Charge
def calculate_energy_charge(units):

    if units <= 100:
        energy_charge = units * 5

    elif units <= 200:
        energy_charge = (100 * 5) + ((units - 100) * 7)

    else:
        energy_charge = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return energy_charge


# Function 3: Calculate VAT
def calculate_vat(energy_charge):
    vat = energy_charge * 5 / 100
    return vat


# Function 4: Calculate Total Bill
def calculate_total_bill(energy_charge, vat):
    total_bill = energy_charge + vat
    return total_bill


# Function 5: Add Customer Bill
def add_customer_bill():

    print("\n========== ADD CUSTOMER BILL ==========")

    # Customer Information
    customer_name = input("Enter Customer Name: ").strip()
    meter_number = input("Enter Meter Number: ").strip()

    # Validate Customer Information
    if not customer_name or not meter_number:
        print("\nError: Customer Name and Meter Number cannot be empty!")
        return

    # Input and Validate Previous Reading
    try:
        previous_reading = float(input("Enter Previous Reading: "))

        if previous_reading <= 0:
            print("\nError: Previous Reading must be a positive number!")
            return

        # Input and Validate Current Reading
        current_reading = float(input("Enter Current Reading: "))

        if current_reading <= 0:
            print("\nError: Current Reading must be a positive number!")
            return

        if current_reading <= previous_reading:
            print("\nError: Current Reading must be greater than Previous Reading!")
            return

    except ValueError:
        print("\nError: Please enter valid numeric readings!")
        return

    # Calculate Units
    units = calculate_units(previous_reading, current_reading)

    # Calculate Energy Charge
    energy_charge = calculate_energy_charge(units)

    # Calculate VAT
    vat = calculate_vat(energy_charge)

    # Calculate Total Bill
    total_bill = calculate_total_bill(energy_charge, vat)

    # Display Customer Bill
    print("\n========== ELECTRICITY BILL ==========")
    print("Customer Name    :", customer_name)
    print("Meter Number     :", meter_number)
    print("Previous Reading :", previous_reading)
    print("Current Reading  :", current_reading)
    print("Units Consumed   :", units)
    print("Energy Charge    : Tk.", round(energy_charge, 2))
    print("VAT (5%)         : Tk.", round(vat, 2))
    print("--------------------------------------")
    print("Total Bill       : Tk.", round(total_bill, 2))
    print("======================================")

    # Save Bill to Text File
    try:
        with open("bills.txt", "a", encoding="utf-8") as file:

            file.write("========== ELECTRICITY BILL ==========\n")
            file.write(f"Customer Name  : {customer_name}\n")
            file.write(f"Meter Number   : {meter_number}\n")
            file.write(f"Units Consumed : {units}\n")
            file.write(f"Total Bill     : Tk. {total_bill:.2f}\n")
            file.write("--------------------------------------\n")

        print("\nSuccess: Customer bill saved successfully!")

    except OSError:
        print("\nError: Unable to save the bill to the file!")


# Function 6: View All Saved Bills
def view_all_bills():

    print("\n========== ALL SAVED BILLS ==========")

    try:
        with open("bills.txt", "r", encoding="utf-8") as file:

            bills = file.read()

            if bills.strip():
                print(bills)
            else:
                print("No bills found in the file.")

    except FileNotFoundError:
        print("No saved bills found! Please add a customer bill first.")

    except OSError:
        print("Error: Unable to read the bills file!")


# Main Function: Menu-Driven Interface
def main():

    while True:

        print("\n======================================")
        print("       ELECTRICITY BILL CALCULATOR")
        print("======================================")
        print("1. Add Customer Bill")
        print("2. View All Bills")
        print("3. Exit")
        print("======================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_customer_bill()

        elif choice == "2":
            view_all_bills()

        elif choice == "3":
            print("\nThank you for using Electricity Bill Calculator!")
            print("Program exited successfully.")
            break

        else:
            print("\nInvalid Choice! Please select 1, 2, or 3.")


# Program Execution
if __name__ == "__main__":
    main()
