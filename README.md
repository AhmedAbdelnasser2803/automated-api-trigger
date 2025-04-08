# Automated API Trigger CLI

A Python-based command-line tool for triggering service-related API actions such as **suspend**, **resume**, or **check-status** based on customer input.

---

## Features

- Supports both manual input and file-based input.
- Works with services such as `internet`, `voice`, `tv`, and `vpn`.
- Simple command-line interface using `argparse`.

---

## Requirements

- Python 3.x
- All dependencies listed in `requirements.txt`

---

## How to Use

### Manual Mode
To trigger an API request using manual input:

```bash
python client.py --mode manual --service internet --customer-id exampleNumber --action suspend
```
## File Mode

To trigger an API request using data from a JSON file, you can provide the file path and action as follows:
```bash
python client.py --mode file --file request_data.json --action resume
```
---
## Project Structure

automated-api-trigger/
├── client.py          # Main script for triggering API requests
├── request_sender.py  # Handles the API request sending logic
├── requirements.txt   # Lists required dependencies
├── request_data.json  # (Optional) Example JSON file for file mode
└── README.md          # Project documentation
---
## Author
Ahmed Abdelnasser – Software QC Engineer with a Computer Science background, exploring automation and Python scripting
