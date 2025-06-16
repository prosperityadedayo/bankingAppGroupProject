import streamlit as st
from PIL import Image
import pandas as pd
from savingsAccount import SavingsAccount
from currentAccount import CurrentAccount

st.set_page_config(page_title = "Bank App", layout = "centered")

username = "Username"
profile_pic_path = "passportPhotograph.png"  

if "savings" not in st.session_state:
    st.session_state.savings = SavingsAccount(200000)

if "current" not in st.session_state:
    st.session_state.current = CurrentAccount(200000)

if "transactions" not in st.session_state:
   st.session_state.transactions = []



savings_balance = st.session_state.savings.balance
current_balance = st.session_state.current.balance
total_balance = savings_balance + current_balance

if "transactions" not in st.session_state:
    st.session_state.transactions = [] 


st.sidebar.header("Accounts Overview")
st.sidebar.subheader("Savings Account")
st.sidebar.write(f"Balance: ₦{savings_balance:,.2f}")

st.sidebar.subheader("Current Account")
st.sidebar.write(f"Balance: ₦{current_balance:,.2f}")
col1, col2 = st.columns([4, 1])

with col1:
    st.subheader("Total Available Balance")
    st.write(f"**₦{total_balance:,.2f}**")

    st.subheader("Transaction History")
    transactions_df = pd.DataFrame(st.session_state.transactions)
    if not transactions_df.empty:
        st.dataframe(transactions_df[::-1], use_container_width=True)
    else:
        st.info("No transactions yet.")
with col2:
    st.write(username)
    st.write("Welcome back")

    try:
        profile_image = Image.open(profile_pic_path)
        st.image(profile_image, width=75)
    except:
        st.write("Profile picture")
        