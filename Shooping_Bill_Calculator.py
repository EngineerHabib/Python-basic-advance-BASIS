
import math
from pathlib import Path

# Store all bills in the same folder as this Python file
BILL_FILE = Path(__file__).with_name("bills.txt")


# Calculate individual product price
def calculate_product_price(quantity, unit_price):
    return quantity * unit_price


# Calculate total amount of all products
def calculate_total_amount(products):
    total = 0

    for product in products:
        total += product["price"]

    return total


# Calculate discount based on total amount
def calculate_discount(total_amount):
    if total_amount >= 5000:
        return total_amount * 0.10
    elif total_amount >= 2000:
        return total_amount * 0.05
    else:
        return 0


# Calculate net payable amount
def calculate_net_payable(total_amount, discount):
    return total_amount - discount


# Add a new customer bill
def add_customer_bill():

    print("\n========== Add Customer Bill ==========")

    customer_name = input("Enter Customer Name: ").strip()

    if not customer_name:
        print("Error: Customer name cannot be empty.")
        return

    products = []

    while True:

        print("\n--- Enter Product Information ---")

        product_name = input("Enter Product Name: ").strip()

        if not product_name:
            print("Error: Product name cannot be empty.")
            continue

        # Validate quantity
        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Error: Quantity must be a positive number.")
                continue

        except ValueError:
            print("Error: Quantity must be a valid whole number.")
            continue

        # Validate unit price
        try:
            unit_price = float(input("Enter Unit Price: "))

            if not math.isfinite(unit_price) or unit_price <= 0:
                print("Error: Unit Price must be a positive number.")
                continue

        except ValueError:
            print("Error: Please enter a valid Unit Price.")
            continue

        product_price = calculate_product_price(
            quantity, unit_price
        )

        products.append({
            "name": product_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "price": product_price
        })

        print(f"Product added successfully!")
        print(f"Product Price: Tk. {product_price:.2f}")

        # Ask whether to add another product
        choice = input(
            "\nDo you want to add another product? (y/n): "
        ).strip().lower()

        if choice == "n":
            break
        elif choice != "y":
            print("Invalid choice. Finishing product entry.")
            break

    if not products:
        print("No products added. Bill was not saved.")
        return

    # Perform calculations
    total_amount = calculate_total_amount(products)

    discount = calculate_discount(total_amount)

    net_payable = calculate_net_payable(
        total_amount, discount
    )

    # Display bill
    print("\n========== Customer Bill ==========")
    print(f"Customer Name: {customer_name}")
    print("-" * 50)

    for product in products:
        print(
            f"{product['name']} | "
            f"Quantity: {product['quantity']} | "
            f"Unit Price: Tk. {product['unit_price']:.2f} | "
            f"Price: Tk. {product['price']:.2f}"
        )

    print("-" * 50)
    print(f"Total Amount       : Tk. {total_amount:.2f}")
    print(f"Discount           : Tk. {discount:.2f}")
    print(f"Net Payable Amount : Tk. {net_payable:.2f}")
    print("=" * 50)

    # Save bill to text file
    try:
        with open(BILL_FILE, "a", encoding="utf-8") as file:

            file.write("\n========== CUSTOMER BILL ==========\n")
            file.write(f"Customer Name: {customer_name}\n")

            for product in products:
                file.write(
                    f"Product: {product['name']} | "
                    f"Quantity: {product['quantity']} | "
                    f"Unit Price: Tk. {product['unit_price']:.2f} | "
                    f"Price: Tk. {product['price']:.2f}\n"
                )

            file.write(f"Total Amount: Tk. {total_amount:.2f}\n")
            file.write(f"Discount: Tk. {discount:.2f}\n")
            file.write(f"Net Payable: Tk. {net_payable:.2f}\n")
            file.write("=" * 50 + "\n")

        print("\nBill saved successfully!")

    except OSError:
        print("Error: Unable to save the bill.")


# Display all saved bills
def view_all_bills():

    print("\n========== All Saved Bills ==========")

    try:
        with open(BILL_FILE, "r", encoding="utf-8") as file:
            bills = file.read()

            if not bills.strip():
                print("No bills found.")
            else:
                print(bills)

    except FileNotFoundError:
        print("No bill file found. Please add a customer bill first.")

    except OSError:
        print("Error: Unable to read the bill file.")


# Main menu
def main():

    while True:

        print("\n========== Shopping Bill Calculator ==========")
        print("1. Add Customer Bill")
        print("2. View All Bills")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_customer_bill()

        elif choice == "2":
            view_all_bills()

        elif choice == "3":
            print("\nThank you for using Shopping Bill Calculator!")
            print("Program exited successfully.")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


# Program execution starts here
if __name__ == "__main__":
    main()
