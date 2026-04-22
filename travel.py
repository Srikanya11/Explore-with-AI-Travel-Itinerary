import streamlit as st
import google.generativeai as genai

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Travel Itinerary Generator",
    layout="centered"
)

# ---------------- GOOGLE GEMINI API ----------------
genai.configure(api_key="AIzaSyAzgS4GcBh2Lu_DoNqXw0D98eoT-TxnaSA")
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- CUSTOM CSS (FIXED WHITE TEXT) ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: #FFFFFF;
}

h1, h2, h3, h4, h5, h6, p, span, label, div {
    color: #FFFFFF !important;
    opacity: 1 !important;
}

input, textarea {
    background-color: #1E1E1E !important;
    color: #FFFFFF !important;
}

button {
    background-color: transparent !important;
    border: 1px solid #FF4B4B !important;
    color: #FF4B4B !important;
}

.output-box {
    border: 1px solid #FF4B4B;
    padding: 20px;
    border-radius: 10px;
    background-color: #0E1117;
    color: #FFFFFF;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>Travel Itinerary Generator</h1>", unsafe_allow_html=True)

# ---------------- INPUTS ----------------
destination = st.text_input("Enter your desired destination:")
days = st.number_input("Enter the number of days:", min_value=1, step=1)
nights = st.number_input("Enter the number of nights:", min_value=0, step=1)

# ---------------- BUTTON ----------------
if st.button("Generate Itinerary"):
    if destination.strip() == "":
        st.error("Please enter a destination")
    else:
        with st.spinner("Generating itinerary..."):

            prompt = f"""
Create a detailed travel itinerary.

Destination: {destination}
Days: {days}
Nights: {nights}

FORMAT:
- Title
- Short introduction
- Day-wise itinerary (Morning, Afternoon, Evening)
- Important Notes section

Use clear markdown headings.
"""

            response = model.generate_content(prompt)

            st.markdown("### Generated Itinerary")
            st.markdown(
                f"<div class='output-box'>{response.text.replace(chr(10), '<br>')}</div>",
                unsafe_allow_html=True
            )
