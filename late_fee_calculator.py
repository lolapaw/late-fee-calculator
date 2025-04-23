from datetime import datetime

def calculate_late_fee(amount, due_date_str, today_str, monthly_rate=0.02):
    # Convert string dates to datetime objects using DD-MM-YYYY format
    due_date = datetime.strptime(due_date_str, '%d-%m-%Y')
    today = datetime.strptime(today_str, '%d-%m-%Y')

    # Calculate days overdue
    days_overdue = (today - due_date).days

    if days_overdue <= 0:
        print("Invoice is not overdue.")
        return 0.0

    # Daily interest rate (assuming 30 days/month)
    daily_rate = monthly_rate / 30
    late_fee = amount * daily_rate * days_overdue

    print(f"Amount: ${amount:.2f}")
    print(f"Days overdue: {days_overdue}")
    print(f"Late fee: ${late_fee:.2f}")
    print(f"Total due: ${amount + late_fee:.2f}")

    return late_fee

# EXAMPLE USAGE
if __name__ == "__main__":
    invoice_amount = 5411.70
    due_date = "25-03-2024"  # Format: DD-MM-YYYY
    today = "23-04-2024"     # Format: DD-MM-YYYY

    calculate_late_fee(invoice_amount, due_date, today)

