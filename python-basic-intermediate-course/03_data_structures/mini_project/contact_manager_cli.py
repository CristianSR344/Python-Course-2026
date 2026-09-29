"""In-memory Contact Manager CLI: add, list, search, and delete contacts."""


def add_contact(contacts: list[dict[str, str]]) -> None:
    name = input("Name: ").strip()
    email = input("Email: ").strip().lower()
    if name and email:
        contacts.append({"name": name, "email": email})
        print("Contact added.")
    else:
        print("Name and email are required.")


def list_contacts(contacts: list[dict[str, str]]) -> None:
    if not contacts:
        print("No contacts.")
    for number, contact in enumerate(contacts, 1):
        print(f"{number}. {contact['name']} <{contact['email']}>")


def search_contacts(contacts: list[dict[str, str]]) -> None:
    query = input("Search: ").strip().lower()
    matches = [c for c in contacts if query in c["name"].lower()
               or query in c["email"]]
    list_contacts(matches)


def delete_contact(contacts: list[dict[str, str]]) -> None:
    email = input("Email to delete: ").strip().lower()
    original_count = len(contacts)
    contacts[:] = [contact for contact in contacts if contact["email"] != email]
    print("Deleted." if len(contacts) < original_count else "Contact not found.")


def main() -> None:
    contacts: list[dict[str, str]] = []
    actions = {"1": add_contact, "2": list_contacts,
               "3": search_contacts, "4": delete_contact}
    while True:
        choice = input("\n1 Add | 2 List | 3 Search | 4 Delete | 5 Quit: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(contacts)
        else:
            print("Choose 1–5.")


if __name__ == "__main__":
    main()

