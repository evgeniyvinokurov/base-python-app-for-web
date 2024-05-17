import random
import os

import re
 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
def checkemail(email):
    return re.fullmatch(regex, email)

def validateform(u):
    resp = {}

    resp["status"] = "ok"
    resp["key"] = "Success"

    if not u["phone"].isdigit():
        resp["status"] = "error"
        resp["key"] = "Only numbers in phone number, please!"
    
    val = all(x.isalpha() or x.isspace() or x == "," or x == "." for x in u["comment"])

    if not val or len(u["comment"]) < 10:
        resp["status"] = "error"
        resp["key"] = "Only letters, spaces and [.,] in comment, minimum 10 chars, please!"

    if not u["name"].isalpha():
        resp["status"] = "error"
        resp["key"] = "Only texts in name, please!"

    if not checkemail(u["email"]):
        resp["status"] = "error"
        resp["key"] = "Only good emails, please!"

    return resp