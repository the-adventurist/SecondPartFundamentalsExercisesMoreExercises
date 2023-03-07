import re

emails_string = input()
pattern = r'(?<!\S)[a-z0-9][a-z0-9_\-\.]*@[a-z-]+\.[a-z-]+\.?[a-z]+'

correct_emails = re.findall(pattern, emails_string)

for email in correct_emails:
    print(email)
