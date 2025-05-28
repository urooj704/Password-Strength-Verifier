import streamlit as st
import re

st.set_page_config(page_title="Password Strength Verifier", page_icon="🔒")

st.markdown("""
    <style>
        .main-title {
            font-size: 2.5em;
            font-weight: 700;
            color: #ff3374;
            text-align: center;
            margin-bottom: 0.5em;
        }

        .subtitle {
            text-align: center;
            color: #5d6d7e;
            font-size: 1.4em;
            margin-bottom: 1em;
        }

        .stTextInput > div > input {
            background-color: #85929e;
            border: 1px solid #fff000;
            padding: 0.6em;
            border-radius: 8px;
        }

        .stTextInput label {
            font-weight: bold;
            color: #85929e ;
        }

        .stMarkdown {
            font-size: 4.05em;
        }

        .stAlert {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="main-title">🔐 Password Strength Verifier</div>', unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
    <p>Welcome to the ultimate Password Strength Verifier! 👋🏻<br>
    Use this simple tool to determine how strong and safe your password is.<br>
    We’ll give you helpful tips to create a <strong>Strong Password</strong> 🔒</p>
</div>
""", unsafe_allow_html=True)


password = st.text_input("Enter your password: ", type="password")

feedback = []

score = 0

if password:
    if len(password) > 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password): 
        score += 1
    else:
        feedback.append("❌Password should contain both lowercase and uppercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one number.")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character(!@#$%^&*).")
    
    if score == 4:
        feedback.append("✅Password is strong and secure!🎉")
    elif score == 3:
        feedback.append("🟡Password is moderately strong. Consider adding more complexity.")
    else:
        feedback.append("❌Password is weak. Please consider making it stronger.")
        
    if feedback:
        st.markdown("### Improvement Suggestions:")
        for tip in feedback:
            st.markdown(tip)
            
else:
    st.info("Please enter your password to get started.")