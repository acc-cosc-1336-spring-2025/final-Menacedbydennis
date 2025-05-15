from x import create_multiplication_table, display_multiplication_table

def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        again = input("Would you like to see the table again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

# === RUN MAIN ===
if __name__ == "__main__":
    main()
    