import re

def main():
    phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    match_object = phoneNumRegex.search("My phone number: 415-555-4242.")
    print("Found phone number:", match_object.group)
    print("Region code:", match_object.group(1))
    print("Number:", match_object.group(2))
    print("All in all:", match_object.groups())

if __name__ == "__main__":
    main()