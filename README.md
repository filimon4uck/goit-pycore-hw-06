# Address Book Management System

## Overview

This project is a system for managing an address book. It includes functionality to add, search, edit, and delete contacts and their phone numbers. The system is designed with a modular approach, with each class handling a specific part of the functionality.

## Entities

### Field
- Base class for record fields.

### Name
- Class for storing a contact's name.
- **Required field.**

### Phone
- Class for storing a phone number.
- **Format validation**: must be 10 digits.

### Record
- Class for storing contact information, including name and a list of phone numbers.

### AddressBook
- Class for storing and managing records.

## Functionality

### AddressBook
- **Add records**: `add_record(record)`
- **Search records by name**: `find(name)`
- **Delete records by name**: `delete(name)`

### Record
- **Add phones**: `add_phone(phone)`
- **Remove phones**: `remove_phone(phone)`
- **Edit phones**: `edit_phone(old_phone, new_phone)`
- **Find phone**: `find_phone(phone)`

## File Structure

- `address_book.py`: Contains the `AddressBook` class.
- `record.py`: Contains the `Record` class.
- `field.py`: Base class for all fields.
- `name.py`: Contains the `Name` class.
- `phone.py`: Contains the `Phone` class.
- `main.py`: Example usage of the address book system.

## Example Usage

```python
from record import Record
from address_book import AddressBook

book = AddressBook()

# Create a record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Add John's record to the address book
book.add_record(john_record)

# Print the address book
print(book)

# Create and add a new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Print all records in the book
print("All records:")
print(book)

# Find and edit a phone number for John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

# Find a specific phone number in John's record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Output: 5555555555

# Delete Jane's record
book.delete("Jane")
print(book)
