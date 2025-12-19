📞 Python CLI Contact Manager

A robust, command-line interface (CLI) tool designed to manage personal contacts efficiently. This project demonstrates core Python concepts including file handling (I/O), JSON serialization, input validation, and algorithm logic for searching and duplicate prevention.
🚀 Features

    Persistent Storage: All data is saved locally in contacts.json, ensuring data remains available after the program closes.

    Smart Validation:

        Prevents non-numeric input for mobile numbers.

        Auto-converts names to lowercase for consistent searching.

    Duplicate Protection: logic prevents adding the same phone number twice.

    Search Functionality: Find contacts by name keywords (substring matching).

    Error Handling: Gracefully handles missing database files and invalid user inputs.



Follow the on-screen menu:
Plaintext

    === CONTACT MANAGER ===
    1. Add Contact
    2. View All Contacts
    3. Delete Contact
    4. Search
    5. Exit

         

🧠 Code Logic

    Data Structure: Contacts are stored as a list of dictionaries to allow easy key-value retrieval.

    JSON Handling: The load_contact() function includes try-except blocks to handle FileNotFoundError, automatically creating a new list if no database exists.

    Search Algorithm: Uses linear search to iterate through the list and match substrings, allowing partial name searches (e.g., searching "ro" finds "Robert").

🔮 Future Roadmap

    [ ] Add "Edit Contact" functionality.

    [ ] Implement email address fields.

    
