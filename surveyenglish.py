import streamlit as st
import pandas as pd
import os

# Set the survey title
st.title("Survey: Opinions on Using AI Systems for Learning Programming Languages")

# Survey introduction
st.write("Thank you for participating in this survey, which aims to understand the perspectives of students and teachers on using AI systems to learn programming languages. Please answer the following questions based on your actual experience.")

# CSV file path
csv_file = "responses.csv"

# Function to save data to CSV
def save_to_csv(data):
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    else:
        df = pd.DataFrame([data])
    df.to_csv(csv_file, index=False)

# Initialize the response dictionary
responses = {}

# Question 1: Are you a student or a teacher?
role = st.selectbox("1. What is your role?", ["Please select", "Student", "Teacher"])

if role != "Please select":
    responses["Role"] = role
    
    # If the user selects "Student"
    if role == "Student":
        st.write("### Questions for Students")

        # Student Question 1
        q1 = st.selectbox("1.1. Is learning a programming language required in your field of study?", ["Please select", "Mandatory", "Elective", "Not required"])
        if q1 != "Please select":
            responses["Is programming required in your field?"] = q1

            # Student Question 2
            q2 = st.selectbox("1.2. How would you rate your proficiency in programming?", ["Please select", "No experience", "Beginner (basic syntax knowledge)", "Intermediate (able to complete simple projects independently)", "Advanced (familiar with multiple languages, can solve complex problems)", "Expert (deep understanding of algorithms and system design)"])
            if q2 != "Please select":
                responses["Programming proficiency"] = q2

                # Student Question 3
                q3 = st.multiselect("1.3. How do you primarily learn programming languages?", ["Classroom learning", "Self-study through tutorials/books", "Online courses", "Discussions with peers or friends", "AI tools or software"], [])
                if q3:
                    responses["Methods for learning programming"] = ', '.join(q3)

                    # Student Question 4
                    q4 = st.selectbox("1.4. Have you ever used AI tools (e.g., ChatGPT, Copilot) to assist in learning programming languages?", ["Please select", "Yes", "No"])
                    if q4 != "Please select":
                        responses["Used AI for learning programming"] = q4

                        # If the student has used AI
                        if q4 == "Yes":
                            q5 = st.select_slider("1.4.1. How much has the AI tool helped you in the following aspects of learning programming? (1 = Not helpful, 5 = Very helpful)", options=[1, 2, 3, 4, 5])
                            responses["Helpfulness of AI (1-5)"] = q5
                        else:
                            q6 = st.selectbox("1.4.2. If you have never used AI tools, would you consider trying them in the future?", ["Please select", "Definitely", "Maybe", "Not sure", "Unlikely", "Never"])
                            if q6 != "Please select":
                                responses["Willingness to try AI in the future"] = q6

                        # Student Question 5
                        q7 = st.selectbox("1.5. Have you used AI tools to solve any challenges encountered while learning programming?", ["Please select", "Frequently", "Occasionally", "Rarely", "Never"])
                        if q7 != "Please select":
                            responses["Used AI for programming challenges"] = q7

                            # Student Question 6
                            q8 = st.selectbox("1.6. What is your current year of study?", ["Please select", "First year", "Second year", "Third year", "Fourth year", "Graduate student"])
                            if q8 != "Please select":
                                responses["Current year of study"] = q8

                                # Student Question 7
                                q9 = st.selectbox("1.7. How long have you been learning programming languages?", ["Please select", "Less than 6 months", "6-12 months", "1-2 years", "2-4 years", "More than 4 years"])
                                if q9 != "Please select":
                                    responses["Duration of learning programming"] = q9

    # If the user selects "Teacher"
    elif role == "Teacher":
        st.write("### Questions for Teachers")

        # Teacher Question 1
        q1 = st.selectbox("2.1. Compared to the past, how do you think students' ability and efficiency in learning programming languages have changed?", ["Please select", "Significantly improved", "Somewhat improved", "Stayed the same", "Somewhat declined", "Significantly declined"])
        if q1 != "Please select":
            responses["Change in students' learning ability"] = q1

            # Teacher Question 2
            q2 = st.selectbox("2.2. Have you ever used AI tools (e.g., ChatGPT, Copilot) to help solve programming challenges in your research?", ["Please select", "Frequently", "Occasionally", "Rarely", "Never"])
            if q2 != "Please select":
                responses["Used AI for research challenges"] = q2

                # Teacher Question 3
                q3 = st.selectbox("2.3. Do you believe that AI systems can effectively help students learn and master programming languages in the long term?", ["Please select", "Strongly believe", "Somewhat believe", "Not sure", "Somewhat doubt", "Strongly doubt"])
                if q3 != "Please select":
                    responses["Belief in AI's long-term effectiveness"] = q3

# Submit button
if st.button("Submit") and responses:
    save_to_csv(responses)
    st.success("Thank you for your participation! Your response has been submitted.")

# Prompt user to enter a password to view data
st.write("### Enter password to view data")
password = st.text_input("Please enter the password", type="password")

# Check password and display data
if password == "Aa110426!":
    st.success("Correct password, displaying data")
    if os.path.exists(csv_file):
        st.write("### All submitted responses:")
        df = pd.read_csv(csv_file)
        st.dataframe(df)
else:
    if password != "":
        st.error("Incorrect password, please try again")
