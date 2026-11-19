# FileHashVerification-Checker
This program was originally made in 2024 while I was on my apprenticeship. Made some improvements after finishing my military obligations

Wolfy - File Hash Checker & Verifier 🔐

A Python-based command-line application designed to calculate file hashes and verify file integrity using cryptographic hashing algorithms.

The application allows users to generate file hashes, compare files against trusted hash values, and save hash records for future reference.

🚀 Features
1. File Hash Checker
Calculates file hashes using four different algorithms:
SHA-256
MD5
SHA-384
SHA-512
Accepts file names and file paths.
Reads files in 4096-byte chunks to handle larger files efficiently.
Optionally saves generated hash records to a local text file.
2. File Hash Verification
Compares a file's calculated hash against a reference hash provided by the user.
Supports SHA-256, MD5, SHA-384, and SHA-512.
Identifies whether the calculated hash matches the reference value.
Provides feedback when a hash mismatch is detected.
3. Hash Record Management
Allows users to save generated hash information.
Automatically creates a DataHash directory.
Records the following information:
File name/path
Hashing algorithm
Generated hash
Date and time of calculation

🛠️ Technologies Used
Python 3
hashlib – Cryptographic hash generation.
os – File and directory operations.
datetime – Date and time recording.
time – Timing and interface delays.

All libraries used are included in Python's standard library.

📋 Requirements
Python 3.x
Windows terminal (the current interface uses the cls command).

No external Python packages are required.

📖 How It Works

When launched, the application presents two main options:

Option 1 – File Hash Verification

Select a hashing algorithm.
Enter the trusted reference hash.
Provide the path to the file you want to verify.
The application calculates the file's hash.
The calculated hash is compared against the reference hash.
The application reports whether the hashes match.

Option 2 – File Hash Checker

Select a hashing algorithm.
Enter the file path.
The application calculates and displays the file's hash.
Choose whether to save the generated hash information.
Similar to GET-FILEHASH in Powershell.

📂 Output Structure

When hash records are saved, the application generates the following directory structure:

text
Project/
│
├── main.py
│
└── DataHash/
    └── Data.txt

🎯 Purpose & Learning Objectives

This project was developed to explore practical applications of Python in cybersecurity and file integrity verification.

It demonstrates knowledge and practical experience with:

Cryptographic hashing algorithms.
File integrity verification.
Binary file handling.
File and directory management.
Python functions and control flow.
Basic command-line interface development.
Handling and storing file verification records.
⚠️ Security Notes
SHA-256, SHA-384, and SHA-512 are recommended for modern file integrity verification.
MD5 is included for compatibility and educational purposes but is considered cryptographically broken.
A matching hash confirms that the file matches the supplied reference hash. It does not independently establish that the reference hash is trustworthy.
A hash mismatch indicates that the file differs from the reference and should be investigated.


🔮 Future Improvements

Potential improvements for future versions:

Add a graphical user interface (GUI).
Support drag-and-drop file selection.
Improve input validation and exception handling.
Add automatic hash comparison and reporting.
Support additional hashing algorithms.
Improve cross-platform compatibility.

Developed by Wolfy

Built with Python 🐍 | Cybersecurity | File Integrity Verification
