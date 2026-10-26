# Validate the number of affected users
def validate_affected_users(affected_users):
    if type(affected_users) is not int or affected_users <=0:
        raise ValueError("Affected users must be a positive integer")
    return affected_users
print(validate_affected_users(8))

# validate a ticket category
VALID_CATEGORIES = ("Network", "Hardware", "Software", "others")

def validate_category(category):
    if category not in VALID_CATEGORIES:
        raise ValueError("Invalid Ticket category")
    return category
print(validate_category("Network"))


def check_duplicate_ids(tickets):
    seen_ids = set()
    for ticket in tickets:
        ticket_id = ticket.get("id")
        
        # Look closely at the underscore here: ticket_id
        if ticket_id in seen_ids:
            raise ValueError(f"Duplicate Ticket ID {ticket_id}")
            
        seen_ids.add(ticket_id)
    return True

# Line 1: Define the list first so Python knows what 'tickets' is
tickets = [ 
    {"id": 1, "title": "Wi-fi Problem"},
    {"id": 1, "title": "Printer Problem"}
    ]
try:
    check_duplicate_ids(tickets)
except ValueError as error:
    print(error)
    
    
# find largest numbers
def find_largest(numbers):
    if not numbers:
        return none
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num 
    return largest
print(find_largest([3, 41, 56, 21, 76, 9]))
