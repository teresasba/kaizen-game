
import streamlit as st
import pandas as pd
from datetime import datetime

def waste_hunter_game():
    st.set_page_config(page_title="Waste Hunter – Kaizen Lean Game", layout="centered")
    st.title("♻️ Waste Hunter – The Kaizen Game")

    st.header("🎯 Your Mission:")
    st.markdown("""
Identify the 8 types of waste hidden in business processes.
Classify each activity as:
- Value-Added (VA)
- Business Value-Added (BVA)
- Non-Value-Added (NVA)
Suggest one Kaizen improvement for each activity.
    """)

    player_name = st.text_input("👤 Enter your name or team:", key="player_name")

    with st.expander("📘 Glossary – Click to expand"):
        st.markdown("""
        ### 🔄 Activity Types
        - **Value-Added (VA):** Directly benefits the customer.
        - **Business Value-Added (BVA):** Necessary for regulatory or business needs.
        - **Non-Value-Added (NVA):** Pure waste that should be eliminated.

        ### 🗑️ The 8 Wastes (TIMWOODS)
        - **Transport:** Unnecessary movement of materials or data (e.g., sending unnecessary emails, moving papers between offices).
        - **Inventory:** Excess work-in-process or backlog (e.g., customer requests sitting unprocessed).
        - **Motion:** Unnecessary movements of people (e.g., searching for information across systems).
        - **Waiting:** Delays between steps (e.g., waiting for approval or feedback).
        - **Overproduction:** Making more than required (e.g., producing unused reports).
        - **Overprocessing:** Doing more work than necessary (e.g., duplicating data entries).
        - **Defects:** Errors causing rework (e.g., wrong customer information leading to complaints).
        - **Skills (Unused Talent):** Not fully utilizing people's capabilities (e.g., senior staff doing basic data entry).

        ### Remember:
        - Transport = Moving THINGS (data, materials)
        - Motion = Moving PEOPLE (walking, clicking, searching)
        """)

    process_steps = {
        "Manually emailing monthly reports": {"correct_type": "NVA", "waste": "Overprocessing"},
        "Waiting for manager approval on requests": {"correct_type": "BVA", "waste": "Waiting"},
        "Entering client data into 3 systems": {"correct_type": "NVA", "waste": "Motion"},
        "Archiving contracts physically": {"correct_type": "NVA", "waste": "Transport"},
        "Double-checking NAV calculations": {"correct_type": "BVA", "waste": "Overprocessing"},
        "Calling client for final approval": {"correct_type": "VA", "waste": None}
    }

    show_solutions = st.checkbox("🔍 Show Correct Answers & Suggestions")
    total_score = 0
    results = []

    for step, details in process_steps.items():
        st.markdown(f"### 🔹 Step: {step}")
        activity_type = st.radio("Classify this activity:", ["VA", "BVA", "NVA"], key=f"{step}_type")
        selected_waste = st.selectbox(
            "Select any waste present (optional):",
            ["None", "Transport", "Inventory", "Motion", "Waiting", "Overproduction", "Overprocessing", "Defects", "Skills (Unused Talent)"],
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
            st.info(f"✅ Correct: {details['correct_type']} | 🗑 Waste: {details['waste'] or 'None'} | 💡 Suggested Kaizen: Automate or standardize this step.")

        results.append({
            "Player": player_name,
            "Step": step,
            "Chosen Type": activity_type,
            "Correct Type": details["correct_type"],
            "Chosen Waste": selected_waste,
            "Correct Waste": details["waste"] or "None",
            "Your Kaizen": kaizen_action,
            "Score": score
        })

    st.markdown("---")
    st.subheader("🏁 Final Score")
    st.markdown(f"### 🎯 Your total score is: **{total_score} / {len(process_steps) * 7}**")

    if player_name.strip():
        df = pd.DataFrame(results)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"wastehunter_results_{player_name}_{timestamp}.csv"
        st.success("📥 Your results were saved!")
        st.download_button("⬇ Download your results", data=df.to_csv(index=False), file_name=filename, mime="text/csv")

waste_hunter_game()
