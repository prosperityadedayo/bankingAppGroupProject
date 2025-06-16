import streamlit as st
from savingsAccount import SavingsAccount

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
            amount <= st.session_state.savings.balance
            st.session_state.savings.balance -= amount
            st.success(f"✅ Successfully Withdrew ₦{amount}")

    elif submit and operations == "Deposit":
        st.success(f"✅ Successfully Deposited ₦{amount}")
        with st.spinner("Processing..."):
            st.session_state.savings.deposit(amount)
    st.write(f"###  Updated Balance: ₦{st.session_state.savings.balance}")
