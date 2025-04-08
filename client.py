import argparse
import requests
import json
import os
from request_sender import send_api_request

def parse_args():
    parser = argparse.ArgumentParser(
        description="""Automated API Trigger Tool

    Examples:

  🔹 Manual mode:
      python client.py --mode manual --service internet --customer-id 123 --action suspend

  🔹 File mode:
      python client.py --mode file --file input_data.json --action resume
    """,
    formatter_class=argparse.RawTextHelpFormatter


    )
    parser.add_argument("--mode", choices=["manual", "file"], required=True, help="Input mode (manual or file)")
    parser.add_argument("--file", help="Path to JSON file (if using file mode)")
    parser.add_argument("--service", choices=["internet", "voice", "tv", "vpn"], help="Service name (manual mode)")
    parser.add_argument("--customer-id", type=int, help="Customer ID (manual mode)")
    parser.add_argument("--action", choices=["suspend", "resume", "check-status"], required=True, help="Action to perform")
    return parser.parse_args()

def build_data(args):
    if args.mode == "file":
        if args.file and os.path.exists(args.file):
            with open(args.file, "r") as f:
                return json.load(f)
        else:
            print("File not found.")
            exit(1)
    elif args.mode == "manual":
        if args.service and args.customer_id:
            return {
                "service": args.service,
                "customerId": str(args.customer_id)
            }
        else:
            print("Manual mode requires --service and --customer-id.")
            exit(1)

if __name__ == "__main__":
    args = parse_args()
    data = build_data(args)
    data["action"] = args.action

    response = send_api_request(data)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
