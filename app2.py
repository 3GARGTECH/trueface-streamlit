import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="TrueFace Quiz", layout="centered")

st.title("🛡️ TrueFace – Fake or Real?")
st.write("Can you spot what’s fake and what’s real? Let’s test your digital instincts!")

quiz_data = [
    {"image": "images/img1.jpg", "answer": "Fake"},
    {"image": "images/img2.jpg", "answer": "Real"},
    {"image": "images/img3.jpg", "answer": "Fake"},
    {"image": "images/img4.jpg", "answer": "Real"},
    {"image": "images/img5.jpg", "answer": "Fake"}
]

user_answers = []
score = 0

for idx, q in enumerate(quiz_data):
    st.image(q["image"], caption=f"Question {idx + 1}", use_column_width=True)
    choice = st.radio(f"Is this image Fake or Real? (Q{idx + 1})", ["Fake", "Real"], key=idx)
    user_answers.append(choice)

if st.button("Submit Quiz"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="TrueFace Quiz Report", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    for idx, (q, ua) in enumerate(zip(quiz_data, user_answers)):
        correct = q["answer"]
        result = "✅ Correct" if ua == correct else "❌ Wrong"
        if ua == correct:
            score += 1
        pdf.cell(200, 10, txt=f"Q{idx + 1}: Your answer: {ua} | Correct: {correct} → {result}", ln=True)

    pdf.cell(200, 10, txt=f"Final Score: {score}/5", ln=True)
    pdf.output("/mnt/data/trueface_quiz_report.pdf")

    st.success(f"Your Score: {score}/5")
    st.download_button("Download PDF Report", data=open("/mnt/data/trueface_quiz_report.pdf", "rb"), file_name="TrueFace_Quiz_Report.pdf")
