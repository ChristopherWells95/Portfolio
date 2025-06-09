class Email:
    # Class variable to store all email objects
    inbox = []

    def __init__(self, email_address, subject_line, email_content):
        # Initialize an Email object with sender address, subject, and content.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

        # Track whether the email has been read
        self.has_been_read = False
        # Add email to the class-level inbox  
        Email.inbox.append(self)  

    def mark_as_read(self):
        # Mark email as read if "true".
        self.has_been_read = True


def populate_inbox():
    # Populate inbox with sample emails.
    Email("user1@example.com", "Meeting Update", "The meeting is at 4 PM.")
    Email("friend@email.com", "Catch Up!", "Let's grab coffee this weekend.")
    Email("work@company.com", "Project Deadline", "The project deadline is next Monday.")


def list_emails():
    # List all emails in the inbox along with their read/unread status.
    if not Email.inbox:  # Check if inbox is empty
        print("\nInbox is empty.")
        return
    
    print("\nInbox Emails:")
    for index, email in enumerate(Email.inbox):
        # Determine read status
        status = "read" if email.has_been_read else "unread"  
        # Display email index and subject
        print(f"{index + 1}. {email.subject_line} [{status}]")  


def read_email(index):
    # Display the content of a selected email and mark it as read.
    # Ensure valid index
    if 0 <= index < len(Email.inbox):  
        email = Email.inbox[index]
        print("\n--- Email ---")
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}\n")
        # Mark email as read after displaying
        email.mark_as_read()  
        
    else:
        # Error message for invalid selection
        print("Invalid email index.")  


def view_unread_emails():
    """Display a list of unread emails."""
    unread_emails = [(i, email) for i, email in enumerate(Email.inbox) if not email.has_been_read]

    if not unread_emails:  
        # Check if there are any unread emails
        print("\nNo unread emails.")
        return

    print("\nUnread Emails:")
    for index, (i, email) in enumerate(unread_emails):
        # Display unread email details
        print(f"{i + 1}. {email.subject_line} (From: {email.email_address})")  


# Populate the inbox with sample emails
populate_inbox()

# Main menu loop
while True:
    try:
        # Display menu options and get user input
        user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. List all emails
    4. Quit application

Enter selection: '''))

        if user_choice == 1:
            # List emails and prompt user to choose an email to read
            list_emails()
            try:
                email_index = int(input("\nEnter the email number to read: ")) - 1
                read_email(email_index)
            except ValueError:
                # Handle non-integer input
                print("Invalid input. Please enter a number.")  

        elif user_choice == 2:
            # View unread emails
            view_unread_emails()

        elif user_choice == 3:
            # List all emails
            list_emails()

        elif user_choice == 4:
            # Exit the program
            print("Exiting program. Goodbye!")
            break  # Break out of loop to terminate program

        else:
            # Handle invalid menu selection
            print("Oops - incorrect input. Please enter a valid option.")  

    except ValueError:
        # Handle non-numeric menu input
        print("Invalid input. Please enter a number.")  
        
