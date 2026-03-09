# palindrome_args.py
import sys

# Check if a string is provided
if len(sys.argv) != 2:
    print("Usage: python palindrome_args.py <text>")
    sys.exit(1)

text = sys.argv[1]
cleaned_text = text.replace(" ", "").lower()  # ignore spaces and case

if cleaned_text == cleaned_text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
