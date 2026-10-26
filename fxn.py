def login_system():
    """Handles user authentication with 3 attempts"""
    # Database of valid users (in production, use a real database with hashed passwords)
    users = {
        "admin": "securepassword123",
        "john": "johnsPassword!",
        "emma": "emma@2024"
    }
    
    max_attempts = 3
    attempts = 0
    
    print("\nLogin System")
    print("============")
    
    while attempts < max_attempts:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        # Check credentials
        if username in users and users[username] == password:
            print(f"\nAccess granted! Welcome, {username}!")
            return True  # Successful login
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"\nInvalid credentials. {remaining_attempts} attempts remaining.")
    
    print("\nMaximum login attempts reached. Access denied.")
    return False  # Failed login

def view_course_offerings():
    """Displays all available courses"""
    courses = [
        "Introduction to Python Programming",
        "Data Structures and Algorithms",
        "Web Development with Django",
        "Machine Learning Fundamentals",
        "Database Systems",
        "Computer Networks",
        "Software Engineering Principles",
        "Artificial Intelligence",
        "Cybersecurity Basics",
        "Mobile App Development with Flutter"
    ]
    
    print("\nAvailable Courses:")
    print("=================")
    for idx, course in enumerate(courses, 1):
        print(f"{idx}. {course}")
    return courses

def select_courses(course_list):
    """Handles course selection with validation"""
    selected = []
    print("\nCourse Selection")
    print("==============")
    
    while True:
        try:
            choice = input("Enter course number (0 to finish): ")
            if choice == '0':
                break
                
            choice = int(choice)
            if 1 <= choice <= len(course_list):
                selected_course = course_list[choice-1]
                if selected_course not in selected:
                    selected.append(selected_course)
                    print(f"Added: {selected_course}")
                else:
                    print("Course already selected")
            else:
                print("Invalid course number")
        except ValueError:
            print("Please enter a number")
    
    return selected

def calculate_fees(selected_courses):
    """Calculates total fees based on selected courses"""
    # Course fee structure (in a real system, this would come from a database)
    fee_structure = {
        "Introduction to Python Programming": 100,
        "Data Structures and Algorithms": 150,
        "Web Development with Django": 200,
        "Machine Learning Fundamentals": 250,
        "Database Systems": 175,
        "Computer Networks": 180,
        "Software Engineering Principles": 160,
        "Artificial Intelligence": 300,
        "Cybersecurity Basics": 220,
        "Mobile App Development with Flutter": 240
    }
    
    total = sum(fee_structure[course] for course in selected_courses)
    return total

def process_payment(amount):
    """Simulates payment processing"""
    print(f"\nPayment Processing")
    print("=================")
    print(f"Total amount due: ${amount}")
    
    while True:
        try:
            payment = float(input("Enter payment amount: $"))
            if payment >= amount:
                print(f"Payment successful! Change: ${payment-amount:.2f}")
                return True
            else:
                print("Insufficient payment")
        except ValueError:
            print("Invalid amount")

def confirm_registration(selected_courses):
    """Displays registration confirmation"""
    print("\nRegistration Confirmation")
    print("========================")
    print("You have successfully registered for:")
    for course in selected_courses:
        print(f"- {course}")
    print("\nThank you for your registration!")

# Main program flow
if __name__ == "__main__":
    # Lecture Explanation:
    # 1. First authenticate the user
    login_successful = login_system()
    
    if login_successful:
        # 2. Show available courses
        courses = view_course_offerings()
        
        # 3. Let user select courses
        selected = select_courses(courses)
        
        if selected:
            # 4. Calculate fees
            total_fee = calculate_fees(selected)
            
            # 5. Process payment
            payment_success = process_payment(total_fee)
            
            if payment_success:
                # 6. Confirm registration
                confirm_registration(selected)
            else:
                print("Registration cancelled due to payment issues")
        else:
            print("No courses selected. Registration cancelled.")