import re


def categorize_value(value):
    if re.match(r'^\w+@\w+\.\w+$', value):
        return "email"
    if re.match(r'^\+7\d{10}$', value):
        return "phone"
    if re.match(r'^@[\w\d_]+$', value):
        return "username"
    return "unknown"
