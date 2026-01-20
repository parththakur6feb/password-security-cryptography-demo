# password-security-cryptography-demo
Foundational Python project demonstrating password validation, MOD-26 cipher, and SHA-256 hashing for learning cryptography and security concepts.

🔐 Password Security & Hashing Demo (Python)
📌 Overview

This project demonstrates fundamental password security concepts used in authentication systems, including strong password validation and cryptographic hashing using SHA-256.

The purpose of this project is learning and conceptual clarity, focusing on how passwords should be validated and handled securely, not stored in plain text.

🧠 Features
1️⃣ Strong Password Validation

The program enforces commonly used security constraints:

Password length between 8 and 20 characters

Must contain:

At least one uppercase letter

At least one lowercase letter

At least one digit

At least one special character

If any requirement is missing, the program clearly reports it and prompts the user again.

2️⃣ SHA-256 Password Hashing

After successful validation, the password is processed using the SHA-256 cryptographic hash function.

Key properties demonstrated:

One-way hashing (irreversible)

Fixed-length output (256-bit)

Deterministic behavior

Avalanche effect (small input change → large hash change)

Passwords are never stored or handled in plaintext after hashing.

🔍 Why Hashing Instead of Encryption?
Hashing	Encryption
One-way process	Reversible process
Used for password storage	Used for data transmission
No secret key required	Requires a secret key

This project correctly uses hashing, not encryption, for password handling.

⚠️ Security Disclaimer

This project uses SHA-256 for educational purposes only.

In real-world applications:

Passwords should be hashed using bcrypt, Argon2, or PBKDF2

A unique salt must be added to each password

Additional protections such as rate-limiting and timing-safe comparisons are required

🛠 Technologies Used

Python 3

hashlib (Python standard library)

📂 Project Structure
password-security-demo/
│
├── main.py    # Password validation and control flow
└── README.md

🎯 Learning Outcomes

Implementing strong password validation logic

Understanding why passwords must be hashed

Difference between hashing and encryption

Importance of encoding before hashing

Foundational concepts in authentication security

🚀 Possible Extensions

Add salted hashing

Implement a login verification system

Replace SHA-256 with bcrypt or Argon2

Convert the script into a CLI authentication tool

👤 Author

Parth Thakur
B.Tech CSE
Interest areas: Cybersecurity, Cryptography, Backend Systems

✅ Honest Note

This project is intended as a foundational learning exercise and not a production-ready security system.
