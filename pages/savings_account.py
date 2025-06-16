import streamlit as st
from savingsAccount import SavingsAccount
from datetime import datetime

st.set_page_config(page_title = "SavingsAcct", layout = "centered")
if "savings" not in st.session_state:
    st.session_state.savings = SavingsAccount(200000)

limit = 1000

with st.form("savings_form"):
    st.subheader("WE GOT YOU COVERED")
    st.title("Savings Account")
    amount = st.number_input("Enter Amount In Naira")
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

    if submit and operations == "Withdraw":
        if amount > st.session_state.savings.balance:
            st.error("❌ Insufficient funds")
        elif amount > limit:
            st.warning("⚠️ You can only withdraw ₦1000 or less at a time")
        else:
            st.session_state.savings.balance -= amount
            st.session_state.transactions.append({
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Account": "Savings",
                "Type": "Withdraw",
                "Amount": -amount
            })
            st.success(f"✅ Successfully Withdrew ₦{amount:,}")

    elif submit and operations == "Deposit":
        st.session_state.savings.deposit(amount)
        st.session_state.transactions.append({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Account": "Savings",
            "Type": "Deposit",
            "Amount": amount
        })
        st.success(f"✅ Successfully Deposited ₦{amount:,}")
            
    st.write(f"###  Updated Balance: ₦{st.session_state.savings.balance}")
