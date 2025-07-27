
import streamlit as st
from fpdf import FPDF
import base64
import io

quiz_data = [
    {"image": "https://i.imgur.com/QrKpWjS.png", "answer": "Fake"},
    {"image": "https://i.imgur.com/RV4xN6M.png", "answer": "Real"},
    {"image": "https://i.imgur.com/IyU1uIR.png", "answer": "Fake"},
    {"image": "https://i.imgur.com/UPL6xC3.png", "answer": "Real"},
    {"image": "https://i.imgur.com/mbVQxqA.png", "answer": "Fake"},
]

if "score" not in st.session_state:
    st.session_state.score = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

st.title("🧠 TrueFace: Detect the Fake")

if st.session_state.current_question < len(quiz_data):
    q = quiz_data[st.session_state.current_question]
    st.image(q["image"], use_column_width=True)
    st.write("Is this image Fake or Real?")
    col1, col2 = st.columns(2)
    if col1.button("Fake"):
        st.session_state.answers.append(("Fake", q["answer"]))
        if q["answer"] == "Fake":
            st.session_state.score += 1
        st.session_state.current_question += 1
    if col2.button("Real"):
        st.session_state.answers.append(("Real", q["answer"]))
        if q["answer"] == "Real":
            st.session_state.score += 1
        st.session_state.current_question += 1
else:
    st.success(f"Quiz complete! Your score: {st.session_state.score}/{len(quiz_data)}")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="TrueFace Quiz Results", ln=True, align="C")
    pdf.ln(10)
    for i, (user_ans, correct_ans) in enumerate(st.session_state.answers, 1):
        result = "✅" if user_ans == correct_ans else "❌"
        pdf.cell(200, 10, txt=f"Q{i}: You answered {user_ans} - Correct: {correct_ans} {result}", ln=True)

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    b64_pdf = base64.b64encode(pdf_output.read()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="TrueFace_Results.pdf">📄 Download your results as PDF</a>'
    st.markdown(href, unsafe_allow_html=True)

    if st.button("🔁 Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = []
