import streamlit as st
from langchain.llms import OpenAI

st.title("🦜🔗 Langchain Quickstart App")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)






"""
"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import hashlib
import google.generativeai as genai

genai.configure(api_key= API)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 1024,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

uploaded_files = []
def upload_if_needed(pathname: str) -> list[str]:
  path = Path(pathname)
  hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
  try:
    existing_file = genai.get_file(name=hash_id)
    return [existing_file.uri]
  except:
    pass
  uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
  return [uploaded_files[-1].uri]

def extract_pdf_pages(pathname: str) -> list[str]:
  parts = [f"--- START OF PDF ${pathname} ---"]
  # Add logic to read the PDF and return a list of pages here.
  pages = []
  for index, page in enumerate(pages):
    parts.append(f"--- PAGE {index} ---")
    parts.append(page)
  return parts

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document0.pdf")
  },
  {
    "role": "model",
    "parts": ["**What is a Secured Credit Card?**\n\nA Secured Credit Card is a credit card that is issued against a Fixed Deposit (FD). When you create an FD of at least Rs 5,000 in the app, your credit card limit will be equal to the FD amount.\n\n**Will it have zero forex markup?**\n\nYes, it does, and it will be accepted on all Visa accepted POS, ATMs, etc.\n\n**How do I get the Credit Card?**\n\nLog into the app, create the FD, and order the card. You will receive the card at your communication address within 7-15 working days. You can start using the card on Ecom apps and websites immediately after ordering.\n\n**What is the maximum limit on this Credit Card?**\n\nIt is recommended to not create an FD of more than Rs 1 lakh.\n\n**Can I use the Credit Card to withdraw cash?**\n\nYes, you can. International ATM withdrawal charges are Rs 299 + taxes.\n\n**How can I withdraw my FDs?**\n\nYou cannot withdraw your FD within 3 months of creating it.\n\n**Will my card be active if I withdraw my FD?**\n\nNo, your card will be blocked if you withdraw your FD, and it cannot be re-issued.\n\n**What is the interest rate on my Fixed Deposit?**\n\nThe FD interest rate is 6.75% per year.\n\n**How can I increase my Credit Card limit?**\n\nYou can create more new FDs to increase your Credit Card limit, which will then be equal to the total amount in your fixed deposits.\n\n**Where will the FD interest amount be credited after maturity?**\n\nUpon maturity, the interest gets credited to your Niyo SBM savings account, and the principal amount gets reinvested automatically for the same tenure. Your credit limit remains the same upon maturity since the FD gets auto-renewed.\n\n**How do I add money to the FD?**\n\nYou can add money to the FD from your Niyo Global Savings account.\n\n**Can I withdraw the FD before maturity?**\n\nYes, you can withdraw the FD before maturity, but:\n\n1. You cannot withdraw the FD within 3 months of creating it.\n2. The FD can only be withdrawn fully (all FDs will get withdrawn) and not partially.\n3. The FD withdrawal balance will come to your Niyo Global (SBM) savings account after deducting any credit card outstanding (if you have any credit card bill due, then the amount will get deducted from FD, and you will get the balance). The FD withdrawal process may take up to 5-7 working days.\n4. Early withdrawal leads to a penalty (loss of 1% interest on your FD) by the bank.\n\n**I'm not able to find the Secured Credit Card option in my Niyo Global app. What should I do?**\n\nThe secured credit card option is available in the latest version of the app. Please update your app to see the option on the homepage."]
  },
  {
    "role": "user",
    "parts": ["hello what is niyo globAL"]
  },
  {
    "role": "model",
    "parts": ["Niyo Global is a fintech company that offers a range of banking and financial services, including:\n\n* **Niyo Global by SBM:** A digital savings account with zero forex markup on international spends, free international ATM withdrawals, and other benefits.\n* **Niyo Global Card:** A multi-currency travel card that allows you to load and spend money in multiple currencies, with no hidden fees or charges.\n* **Niyo Money:** An international remittance service that allows you to send money to over 100 countries at competitive rates.\n\nNiyo Global is designed to make it easier and more affordable for Indians to manage their finances globally. The company's mission is to provide a seamless and convenient banking experience for everyone, regardless of where they live or travel.\n\nNiyo Global is a joint venture between SBM Bank (India) and Niyo Solutions. SBM Bank (India) is a leading private sector bank in India, while Niyo Solutions is a fintech company that specializes in providing digital banking solutions.\n\nNiyo Global is headquartered in Mumbai, India, and has offices in Bangalore, Delhi, and Hyderabad. The company also has a presence in Singapore and the United Kingdom.\n\nNiyo Global is a safe and secure company to use. The company is regulated by the Reserve Bank of India (RBI) and follows all applicable laws and regulations. Niyo Global also uses the latest security technologies to protect customer data and transactions."]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
for uploaded_file in uploaded_files:
  genai.delete_file(name=uploaded_file.name)
"""

