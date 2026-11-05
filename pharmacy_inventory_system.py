# Smart Pharmacy Inventory & Sales Management System

# Business rules and thresholds
LOW_STOCK_THRESHOLD = 10

print("\n==== Smart Pharmacy Inventory & Sales Management System ====")

# Step 1: Ask how many medicines to process
medicine_count_text = input("\nEnter the number of medicines: ").strip()

# Step 2: Validate the count before the loop
if not medicine_count_text.isdecimal() or int(medicine_count_text) < 1:
    print(
        "Invalid Input! Number of medicines must be a whole number "
        "of at least 1."
    )
else:
    total_medicines = int(medicine_count_text)

    # Step 3: Initialize variables
    total_revenue = 0
    restock_count = 0
    processed_count = 0

    # Step 4: Process each medicine using for loop
    for i in range(total_medicines):

        print("\n---- Medicine", i + 1, "----")

        # Step 5: Collect medicine information as text
        medicine_name = input("Enter medicine name: ").strip()
        stock_text = input("Enter available stock: ").strip()
        price_text = input("Enter price per unit (Rs.): ").strip()
        quantity_text = input("Enter quantity sold: ").strip()

        # Step 6: Validate numeric text before conversion
        is_stock_number = stock_text.isdecimal()
        if stock_text.startswith("-"):
            is_stock_number = stock_text[1:].isdecimal()

        is_price_number = price_text.replace(".", "", 1).isdecimal()
        if price_text.startswith("-"):
            is_price_number = price_text[1:].replace(".", "", 1).isdecimal()

        is_quantity_number = quantity_text.isdecimal()
        if quantity_text.startswith("-"):
            is_quantity_number = quantity_text[1:].isdecimal()

        # Step 7: Check input validity
        if medicine_name == "":
            print("\nInvalid Input! Medicine name cannot be empty.")

        elif not is_stock_number:
            print("\nInvalid Input! Available stock must be a whole number.")

        elif not is_price_number:
            print("\nInvalid Input! Price per unit must be a number.")

        elif not is_quantity_number:
            print("\nInvalid Input! Quantity sold must be a whole number.")

        else:
            stock = int(stock_text)
            price = float(price_text)
            quantity_sold = int(quantity_text)

            if stock < 0 or price < 0 or quantity_sold < 0:
                print("\nInvalid Input! Values cannot be negative.")

            # Step 8: Check stock availability
            elif quantity_sold > stock:
                print("\nInsufficient stock!")
                print("Available stock:", stock)
                print("Requested quantity:", quantity_sold)
                print("Sale could not be processed.")

            else:
                # Step 9: Calculate sales amount
                sales_amount = quantity_sold * price

                # Step 10: Calculate remaining stock
                remaining_stock = stock - quantity_sold

                # Step 11: Update total revenue (accumulator)
                total_revenue = total_revenue + sales_amount

                # Step 12: Count successful sales (counter)
                processed_count = processed_count + 1

                # Step 13: Display medicine details
                print("\nMedicine Name:", medicine_name)
                print(f"Sales Amount: Rs. {sales_amount:.2f}")
                print("Remaining Stock:", remaining_stock)

                # Step 14: Check low stock
                if remaining_stock < LOW_STOCK_THRESHOLD:
                    print("\nWarning: Low Stock! Restocking Required.")

                    # Counter
                    restock_count = restock_count + 1

                else:
                    print("\nStock Status: Sufficient")

    # Step 15: Display final pharmacy report
    print("\n=== Daily Pharmacy Sales Report ===")
    print("\nTotal Medicines Entered:", total_medicines)
    print("Medicines Successfully Processed:", processed_count)
    print(f"Total Pharmacy Revenue: Rs. {total_revenue:.2f}")
    print("Medicines Requiring Restocking:", restock_count)
    print("==================================")
