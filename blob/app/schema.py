schema = {
    "bank_statement": {
        "account_number": "string",
        "date": "string",
        "transactions": [
            {"date": "string", "description": "string", "amount": "string"}
        ],
        "total_balance": "string"
    },
    "bank_check": {
        "check_number": "string",
        "account_number": "string",
        "amount": "string",
        "date": "string"
    }
}
