
import streamlit as st

def lean_kaizen_game():
    st.set_page_config(page_title="Waste Hunter – Kaizen Game", layout="centered")
    st.title("💡 Waste Hunter – The Kaizen Game")
    st.subheader("🎯 Classify process steps, detect waste, and apply Kaizen solutions")

    process_steps = {
        "Send monthly report by email manually": {"correct_type": "NVA", "waste": "Overprocessing"},
        "Validate compliance rules manually": {"correct_type": "BVA", "waste": "Waiting"},
        "Re-enter client data in 3 systems": {"correct_type": "NVA", "waste": "Motion"},
        "Print and archive client contracts": {"correct_type": "NVA", "waste": "Inventory"},
        "Review NAV calculation": {"correct_type": "BVA", "waste": "Overprocessing"},
        "Client approval call": {"correct_type": "VA", "waste": None}
    }

    total_score = 0

    for step, details in process_steps.items():
        st.markdown(f"### 🔹 Step: {step}")

        activity_type = st.radio(f"Classify this activity:", ["VA", "BVA", "NVA"], key=f"{step}_type")
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

    st.markdown("---")
    st.markdown(f"### 🧮 Final Score: **{total_score} points** out of {len(process_steps) * 7}")

lean_kaizen_game()
