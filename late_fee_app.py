import streamlit as st
from datetime import datetime

def calculate_late_fee(amount, due_date_str, today_str, monthly_rate=0.02):
    try:
        due_date = datetime.strptime(due_date_str, '%d-%m-%Y')
        today = datetime.strptime(today_str, '%d-%m-%Y')
    except ValueError:
        st.error("⚠️ Please use the correct date format: DD-MM-YYYY.")
        return None

    days_overdue = (today - due_date).days

    if days_overdue <= 0:
        st.info("✅ The invoice is not overdue.")
        return 0.0

    daily_rate = monthly_rate / 30
    late_fee = amount * daily_rate * days_overdue
    return late_fee

# --- Streamlit UI ---
st.title("💸 Late Fee Calculator")
st.markdown("Enter the invoice amount and dates to calculate overdue charges.")

invoice_amount = st.number_input("Invoice Amount ($)", min_value=0.01, step=0.01)
due_date = st.text_input("Due Date (DD-MM-YYYY)", value="25-03-2024")
today_date = st.text_input("Today's Date (DD-MM-YYYY)", value=datetime.now().strftime('%d-%m-%Y'))

if st.button("Calculate Late Fee"):
    late_fee = calculate_late_fee(invoice_amount, due_date, today_date)
    if late_fee is not None:
        st.success(f"Late Fee: **${late_fee:.2f}**")
        st.write(f"**Total Due:** ${invoice_amount + late_fee:.2f}")
