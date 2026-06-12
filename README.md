# 📧 Email Validator

A lightweight, dependency-free Python utility for validating email addresses against RFC-standard rules — with clear, human-readable error messages.

---

## ✨ Features

- ✅ No external libraries required — pure Python (`re`, `sys`)
- ✅ Validates against RFC 5321 / 5322 rules
- ✅ Returns detailed reasons for invalid emails
- ✅ Supports command-line arguments input
- ✅ Batch-test multiple emails at once
- ✅ Clean, importable `check_email()` function for use in your own projects

---

## 📋 Validation Rules

| Rule | Details |
|------|---------|
| `@` symbol | Must contain exactly one `@` |
| Local part | Max 64 chars, valid characters only (`a-z`, `0-9`, `._%+-`) |
| Local part dots | Cannot start, end, or contain consecutive dots |
| Domain | Max 253 chars, valid characters only (`a-z`, `0-9`, `.-`) |
| Domain hyphens | Cannot start or end with a hyphen |
| Domain dots | Cannot start, end, or contain consecutive dots |
| TLD | Minimum 2 characters, letters only |
| Total length | Must not exceed 320 characters |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- No `pip` installs needed

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/email-validator.git

# Navigate into the project folder
cd email-validator
```

---

## 💻 Usage

### 1. Run the built-in test suite

Running the script with no arguments automatically tests 21 built-in email cases:

```bash
python3 email_checker.py
```

**Output:**

```
=======================================================
              EMAIL VALIDATION RESULTS
=======================================================
  Email  : user@example.com
  Status : ✓ VALID

  Email  : double@@at.com
  Status : ✗ INVALID
  Reason : Must contain exactly one '@' symbol

  ...
=======================================================
  Checked: 21 | Valid: 6 | Invalid: 15
=======================================================
```

---

### 2. Validate your own email(s) via command line

Pass one or more email addresses directly as arguments:

```bash
python3 email_checker.py you@example.com
```

```bash
python3 email_checker.py alice@gmail.com bad@.com test@domain.123
```

---


### 3. Import into your own Python project

The `check_email()` function is fully importable:

```python
from email_checker import check_email

result = check_email("user@example.com")
print(result)
# {'email': 'user@example.com', 'valid': True, 'reason': 'Valid email address'}

result = check_email("bad@@email.com")
print(result["valid"])   # False
print(result["reason"])  # Must contain exactly one '@' symbol
```

### Return value structure

```python
{
    "email":  str,   # The original email passed in
    "valid":  bool,  # True if valid, False otherwise
    "reason": str    # "Valid email address" or a specific error message
}
```

---

## 🧪 Test Cases

| Email | Status | Reason |
|-------|--------|--------|
| `user@example.com` | ✅ Valid | — |
| `firstname.lastname@company.org` | ✅ Valid | — |
| `user+tag@subdomain.example.co.uk` | ✅ Valid | — |
| `USER@DOMAIN.COM` | ✅ Valid | — |
| `user@domain-with-hyphen.com` | ✅ Valid | — |
| `missingatsign.com` | ❌ Invalid | Must contain exactly one `@` symbol |
| `double@@at.com` | ❌ Invalid | Must contain exactly one `@` symbol |
| `@nodomain.com` | ❌ Invalid | Local part (before `@`) is empty |
| `.user@domain.com` | ❌ Invalid | Local part cannot start or end with a dot |
| `user..double@domain.com` | ❌ Invalid | Local part cannot contain consecutive dots |
| `user@domain..com` | ❌ Invalid | Domain cannot contain consecutive dots |
| `user@-invalid.com` | ❌ Invalid | Domain cannot start or end with a hyphen |
| `user@domain.c` | ❌ Invalid | TLD must be at least 2 characters |
| `user@domain.123` | ❌ Invalid | TLD must contain only letters |

---

## 📁 Project Structure

```
email-validator/
│
├── email_checker.py   # Main script with check_email() function
└── README.md          # Project documentation
```

---

## 🛣️ Roadmap

- [ ] Add DNS/MX record lookup to verify domain existence
- [ ] Add disposable email domain detection
- [ ] Build a simple CLI with `argparse` (flags, quiet mode, JSON output)
- [ ] Export results to CSV

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — feel free to use, modify, and distribute it.

---

## 👤 Author

**Your Name**  
GitHub: [@Selvakumar-sk](https://github.com/Selvakumar-sk)

---

<p align="center">Made with ❤️ and Python</p>
