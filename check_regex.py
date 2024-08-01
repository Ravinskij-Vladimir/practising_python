import re

def main():
    phoneNumRegex  =re.compile(r'\d{3}-\d{3}-\d{4}')
    match_object = phoneNumRegex.search("My phone number: 415-555-4242.")
    print("Found phone number: " + match_object.group())

if __name__ == "__main__":
    main()