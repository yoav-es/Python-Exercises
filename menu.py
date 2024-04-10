import re

def get_input(prompt):
    return input(prompt)

def validate_email(user_input):
    email_regex_short = r'\b[A-Za-z0-9.-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_regex_long  = r'\b[A-Za-z0-9]+[A-Za-z0-9.-]*@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\.[A-Z|a-z]{2,}\b'
    return re.match(email_regex_short, user_input) is not None or return re.match(email_regex_long, user_input) is not None

def validate_input(user_input, ptype):
    # Add your validation logic here
    if ptype == 'Name':
        if not user_input.isalpha():
            return False
    elif ptype == 'Email':
        if validate_email(user_input) == False:
            return False
        return True
    elif ptype == 'Age':
        if not user_input.isdigit():
            return False
        
    return True if user_input else False

def main():
    inputs = ['Email', 'Name', 'Age']
    user_data = {}
    for i in inputs:
        while True:
            user_input = get_input(f"Enter your {i}: ")
            if validate_input(user_input,i):
                user_data[i] = user_input
                break
            else:
                print(f"Invalid {i}. Please try again.")
    print("User data:", user_data)

if __name__ == "__main__":
    main()