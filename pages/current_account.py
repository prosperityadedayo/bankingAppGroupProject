import streamlit as st

from currentAccount import CurrentAccount

st.set_page_config(page_title = "current account", layout = "centered")
current = CurrentAccount(100000)

with st.form("CURRENT_FORM"):
    st.subheader("WE GOT YOU COVERED")
    st.title("Current Account")
    amount = st.number_input("Enter Amount")
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")
    if submit and operations == "Withdraw":
        with st.spinner("Processing..."):
            current.withdraw(amount)

    elif submit and operations == "Deposit":
        with st.spinner("Processing..."):
            current.deposit(amount)
print(current.balance)




