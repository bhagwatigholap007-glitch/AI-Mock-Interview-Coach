import streamlit as st

st.set_page_config(
    page_title="AI Mock Interview Coach",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Mock Interview Coach")
st.write("Practice interview questions and improve your answers!")

name = st.text_input("Enter your name")
role = st.selectbox(
    "Choose your interview role",
    ["Python Developer", "Data Scientist", "AI Engineer"]
)

questions = {
    "Python Developer": [
        "Tell me about yourself.",
        "What is Python?",
        "What is the difference between a list and a tuple?"
    ],
    "Data Scientist": [
        "Tell me about yourself.",
        "What is data science?",
        "What is the difference between supervised and unsupervised learning?"
    ],
    "AI Engineer": [
        "Tell me about yourself.",
        "What is artificial intelligence?",
        "What is the difference between AI and machine learning?"
    ]
}

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if name:
    st.subheader(f"Welcome, {name}!")

question_list = questions[role]
index = st.session_state.question_index

st.progress((index + 1) / len(question_list))
st.subheader(f"Question {index + 1} of {len(question_list)}")
st.write(question_list[index])

answer = st.text_area(
    "Type your answer here:",
    key=f"answer_{index}",
    height=150
)

if st.button("Submit Answer"):
    if answer.strip():
        st.session_state.answers.append(answer)
        st.success("Answer submitted!")

        words = len(answer.split())

        st.write(f"**Your answer length:** {words} words")

        if words < 20:
            st.info("Try adding more detail and a practical example.")
        else:
            st.info(
                "Good start! Review your answer for clarity, "
                "relevance, and examples."
            )
    else:
        st.warning("Please type your answer first.")

if index < len(question_list) - 1:
    if st.button("Next Question"):
        st.session_state.question_index += 1
        st.rerun()
else:
    st.success("You have reached the end of this practice session!")

if st.button("Restart Interview"):
    st.session_state.question_index = 0
    st.session_state.answers = []
    st.rerun()

st.caption(
    "Note: This starter version gives basic feedback. "
    "It does not yet use a real AI model."
)