from companies import get_stock_list,display_stock_list

def main():


    stocks = get_stock_list()  # Step 2: Get list of stock objects

    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_stock_list(stocks)  # Step 3 Option 1
        elif choice == "2":
            print("Exiting program.")
            break  # Step 3 Option 2
        else:
            print("Invalid option. Please choose 1 or 2.")


# === RUN PROGRAM ===
if __name__ == "__main__":
    main()