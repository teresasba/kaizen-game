
import streamlit as st
import pandas as pd
from datetime import datetime

def lean_kaizen_game():
    st.set_page_config(page_title="Waste Hunter – Kaizen Game", layout="centered")
    st.title("💡 Waste Hunter – The Kaizen Game")
    st.subheader("🎯 Classify process steps, detect waste, and apply Kaizen solutions")

    player_name = st.text_input("👤 Enter your name or team:", key="player_name")

    with st.expander("📘 Glossary – Click to learn before you play"):
        st.markdown(""" 
        ### 🔄 Activity Types
        - **Value-Added (VA):** Directly benefits the customer.
        - **Business Value-Added (BVA):** Necessary for legal or operational needs.
        - **Non-Value-Added (NVA):** Pure waste, should be reduced or removed.

        ### 🗑️ The 8 Wastes (TIMWOODS)
        - **Transport, Inventory, Motion, Waiting, Overproduction, Overprocessing, Defects, Skills (unused talent)**
        """)

    process_steps = {
        "Send monthly report by email manually": {
            "correct_type": "NVA", "waste": "Overprocessing",
            "solution": "Automate report distribution via BI tool."
        },
        "Validate compliance rules manually": {
            "correct_type": "BVA", "waste": "Waiting",
            "solution": "Automate validation with a rule engine."
        },
        "Re-enter client data in 3 systems": {
            "correct_type": "NVA", "waste": "Motion",
            "solution": "Use single data entry with integration."
        },
        "Print and archive client contracts": {
            "correct_type": "NVA", "waste": "Inventory",
            "solution": "Implement digital signature & cloud storage."
        },
        "Review NAV calculation": {
            "correct_type": "BVA", "waste": "Overprocessing",
            "solution": "Automate cross-checks and reduce rework."
        },
        "Client approval call": {
            "correct_type": "VA", "waste": None,
            "solution": "Keep – adds value through personal contact."
        }
    }

    show_solutions = st.checkbox("🔍 Show Correct Answers & Solutions")
    total_score = 0
    results = []

    for step, details in process_steps.items():
        st.markdown(f"### 🔹 Step: {step}")
        activity_type = st.radio("Classify this activity:", ["VA", "BVA", "NVA"], key=f"{step}_type")
        selected_waste = st.selectbox(
            "Select any waste present (optional):",
            ["None", "Defect", "Overproduction", "Waiting", "Non-utilized talent",
             "Transport", "Inventory", "Motion", "Overprocessing"],
            key=f"{step}_waste"
        )
        kaizen_action = st.text_input("💡 Suggest a Kaizen improvement:", key=f"{step}_kaizen")

        score = 0
        if activity_type == details["correct_type"]:
            score += 2
        if selected_waste != "None" and selected_waste == details["waste"]:
            score += 2
        if kaizen_action.strip():
            score += 3

        total_score += score
        st.markdown(f"✅ Points for this step: **{score}**")

        if show_solutions:
            st.info(f"✅ Correct: {details['correct_type']} | 🗑 Waste: {details['waste'] or 'None'} | 💡 Kaizen: {details['solution']}")

        results.append({
            "Player": player_name,
            "Step": step,
            "Chosen Type": activity_type,
            "Correct Type": details["correct_type"],
            "Chosen Waste": selected_waste,
            "Correct Waste": details["waste"] or "None",
            "Your Kaizen": kaizen_action,
            "Suggested Kaizen": details["solution"],
            "Score": score
        })

    st.markdown("---")
    st.markdown(f"### 🧮 Final Score: **{total_score} / {len(process_steps) * 7}**")

    if player_name.strip():
        df = pd.DataFrame(results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"kaizen_results_{player_name}_{timestamp}.csv"
        df.to_csv(filename, index=False)
        st.success("📥 Your results were saved!")
        st.download_button("⬇ Download your results", data=df.to_csv(index=False), file_name=filename, mime="text/csv")

lean_kaizen_game()
