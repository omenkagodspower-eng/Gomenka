import json
import uuid
from pathlib import Path

FILE_PATH = Path("tickets.json")


def load_tickets():
    """Load existing tickets or return an empty list."""
    if not FILE_PATH.exists():
        return []

    with FILE_PATH.open("r", encoding="utf-8") as file:
        tickets = json.load(file)

    if not isinstance(tickets, list):
        raise ValueError("The tickets file must contain a JSON list.")

    return tickets


def create_ticket(title, description):
    """Validate input and create a new ticket."""
    if not title.strip():
        raise ValueError("Title cannot be empty.")

    if not description.strip():
        raise ValueError("Description cannot be empty.")

    return {
        "id": str(uuid.uuid4()),
        "title": title.strip(),
        "description": description.strip()
    }


def save_tickets(tickets):
    """Save all tickets to the JSON file."""
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)


def main():
    print("=== CampusFlow Ticket Creator ===")

    try:
        tickets = load_tickets()

        title = input("Enter ticket title: ")
        description = input("Describe the problem: ")

        ticket = create_ticket(title, description)

        tickets.append(ticket)
        save_tickets(tickets)

        print("\nTicket created successfully!")
        print(f"Ticket ID: {ticket['id']}")

    except ValueError as error:
        print(f"Invalid input or ticket data: {error}")

    except json.JSONDecodeError:
        print("Error: tickets.json contains invalid JSON.")

    except OSError as error:
        print(f"File error: {error}")

    except (EOFError, KeyboardInterrupt):
        print("\nOperation cancelled.")


if __name__ == "__main__":
    main()