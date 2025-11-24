import streamlit as st

st.set_page_config(page_title="Calculator App", page_icon="🧮")

st.title("🧮 Simple Calculator App")

st.write("Enter two numbers and choose an operation.")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

# Calculate
result = None

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
        else:
            result = num1 / num2

# Display result
if result is not None:
    st.success(f"### Result: {result}")
