import streamlit as st

from currentAccount import CurrentAccount

st.set_page_config(page_title = "current account", layout = "centered")
if "current" not in st.session_state:
    st.session_state.current = CurrentAccount(200000)
limit = 1000

with st.form("CURRENT_FORM"):
    st.subheader("WE GOT YOU COVERED")
    st.title("Current Account")
    amount = st.number_input("Enter Amount In Naira")
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")
    if submit and operations == "Withdraw":
        if amount > st.session_state.current.balance:
            st.error("❌ Insufficient funds")
        elif amount > limit:
            st.warning("⚠️ You can only withdraw N1000 or less at a time")
        else:
            amount <= st.session_state.current.balance
            st.session_state.current.balance -= amount
            st.success(f"✅ Successfully withdrew ₦{amount}")

    elif submit and operations == "Deposit":
        st.success(f"✅ Successfully Deposited ₦{amount}")
        with st.spinner("Processing..."):
            st.session_state.current.deposit(amount)
    st.write(f"### Updated Balance: ₦{st.session_state.current.balance}")



