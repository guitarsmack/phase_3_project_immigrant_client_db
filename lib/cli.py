# lib/cli.py

from helpers import (
    exit_program,
    get_clients,
    get_client_by_id,
    delete_client_by_id,
    get_clients_by_origin,
    get_clients_by_language,
    create_client,
    create_country,
    delete_country_by_id,
    get_countries,
    get_country_by_id,
    get_countries_by_language
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_client()
        elif choice == "2":
            delete_client_by_id()
        elif choice == "3":
            get_clients()
        elif choice == "4":
            get_client_by_id()
        elif choice == "5":
            get_clients_by_origin()
        elif choice == "6":
            get_clients_by_language()
        elif choice == "7":
            create_country()
        elif choice == "8":
            delete_country_by_id()
        elif choice == "9":
            get_countries()
        elif choice == "10":
            get_country_by_id()
        elif choice == "11":
            get_countries_by_language()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create new client")
    print("2. Delete client by ID")
    print("3. List all clients")
    print("4. Get client by ID")
    print("5. Get all clients from country name")
    print("6. Get clients who share a language")
    print("7. Add new country")
    print("8. Delete country by ID")
    print("9. List all countries")
    print("10. Get country by ID")
    print("11. Get countries that speak certain language")


if __name__ == "__main__":
    main()
