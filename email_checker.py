import re

import sys
 
def check_email(email: str) -> dict:

    """

    Validates an email address and returns detailed results.

    Returns a dict with:

        - valid (bool): Whether the email is valid

        - reason (str): Reason if invalid, or "Valid email" if valid

    """

    result = {"email": email, "valid": False, "reason": ""}
 
    # 1. Must not be empty

    if not email or not email.strip():

        result["reason"] = "Email is empty"

        return result
 
    email = email.strip()
 
    # 2. Must have exactly one '@'

    if email.count("@") != 1:

        result["reason"] = "Must contain exactly one '@' symbol"

        return result
 
    local, domain = email.split("@")
 
    # 3. Local part checks

    if not local:

        result["reason"] = "Local part (before '@') is empty"

        return result

    if len(local) > 64:

        result["reason"] = "Local part exceeds 64 characters"

        return result

    if not re.match(r'^[a-zA-Z0-9._%+\-]+$', local):

        result["reason"] = "Local part contains invalid characters"

        return result

    if local.startswith(".") or local.endswith("."):

        result["reason"] = "Local part cannot start or end with a dot"

        return result

    if ".." in local:

        result["reason"] = "Local part cannot contain consecutive dots"

        return result
 
    # 4. Domain checks

    if not domain:

        result["reason"] = "Domain (after '@') is empty"

        return result

    if len(domain) > 253:

        result["reason"] = "Domain exceeds 253 characters"

        return result

    if not re.match(r'^[a-zA-Z0-9.\-]+$', domain):

        result["reason"] = "Domain contains invalid characters"

        return result

    if domain.startswith("-") or domain.endswith("-"):

        result["reason"] = "Domain cannot start or end with a hyphen"

        return result

    if domain.startswith(".") or domain.endswith("."):

        result["reason"] = "Domain cannot start or end with a dot"

        return result

    if ".." in domain:

        result["reason"] = "Domain cannot contain consecutive dots"

        return result
 
    # 5. TLD checks

    if "." not in domain:

        result["reason"] = "Domain must contain at least one dot (missing TLD)"

        return result

    tld = domain.rsplit(".", 1)[1]

    if len(tld) < 2:

        result["reason"] = "TLD must be at least 2 characters"

        return result

    if not re.match(r'^[a-zA-Z]+$', tld):

        result["reason"] = "TLD must contain only letters"

        return result
 
    # 6. Overall length

    if len(email) > 320:

        result["reason"] = "Email address exceeds maximum length of 320 characters"

        return result
 
    result["valid"] = True

    result["reason"] = "Valid email address"

    return result
 
 
def main():
 
    # If arguments provided, use those instead

    emails_to_check = sys.argv[1:]
 
    print("=" * 55)

    print(f"{'EMAIL VALIDATION RESULTS':^55}")

    print("=" * 55)
 
    valid_count = 0

    for email in emails_to_check:

        result = check_email(email)

        status = "✓ VALID" if result["valid"] else "✗ INVALID"

        display = repr(email) if not email.strip() else email[:40]

        print(f"\n  Email  : {display}")

        print(f"  Status : {status}")

        if not result["valid"]:

            print(f"  Reason : {result['reason']}")

        if result["valid"]:

            valid_count += 1
 
    print("\n" + "=" * 55)

    print(f"  Checked: {len(emails_to_check)} | Valid: {valid_count} | Invalid: {len(emails_to_check) - valid_count}")

    print("=" * 55)
 
 
if __name__ == "__main__":

    main()
 