
import streamlit as st

def lean_kaizen_game():
    st.set_page_config(page_title="Waste Hunter – Kaizen Game", layout="centered")
    st.title("💡 Waste Hunter – The Kaizen Game")
    st.subheader("🎯 Classify process steps, detect waste, and apply Kaizen solutions")

    with st.expander("📘 Glossary – Click to learn before you play"):
        st.markdown("""
        ### 🔄 Activity Types
        - **Value-Added (VA):** Activities that directly contribute to what the customer is paying for.
        - **Business Value-Added (BVA):** Activities required for business/legal reasons but don't add customer value (e.g., compliance checks).
        - **Non-Value-Added (NVA):** Pure waste. These steps should be minimized or eliminated.

        ### 🗑️ The 8 Wastes (TIMWOODS)
        - **Transport:** Unnecessary movement of items or information.
        - **Inventory:** Excess materials, info, or WIP.
        - **Motion:** Excess movement by people.
        - **Waiting:** Idle time for people, info, or items.
        - **Overproduction:** Producing too much or too early.
        - **Overprocessing:** Doing more than necessary.
        - **Defects:** Errors or rework.
        - **Skills (Unused Talent):** Not using people's full potential.
        """)

    process_steps = {
        "Send monthly report by email manually": {
            "correct_type": "NVA", "waste": "Overprocessing",
            "solution": "Automate report distribution via integrated BI tool."
        },
        "Validate compliance rules manually": {
            "correct_type": "BVA", "waste": "Waiting",
            "solution": "Implement rule engine for automated validation."
        },
        "Re-enter client data in 3 systems": {
            "correct_type": "NVA", "waste": "Motion",
            "solution": "Adopt single-entry interface across systems."
        },
        "Print and archive client contracts": {
            "correct_type": "NVA", "waste": "Inventory",
            "solution": "Digitize storage with e-signature and secure cloud archive."
        },
        "Review NAV calculation": {
            "correct_type": "BVA", "waste": "Overprocessing",
            "solution": "Validate NAV with automated cross-check logic."
        },
        "Client approval call": {
            "correct_type": "VA", "waste": None,
            "solution": "Keep as is – value-added direct contact."
        }
    }

    total_score = 0
    show_solutions = st.checkbox("🔍 Show Correct Answers & Solutions")

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
            st.markdown(f"""
**✅ Correct Classification**: {details['correct_type']}
**🗑 Actual Waste**: {details['waste'] or "None"}
**💡 Suggested Kaizen**: {details['solution']}
""")

    st.markdown("---")
    st.markdown(f"### 🧮 Final Score: **{total_score} points** out of {len(process_steps) * 7}")

lean_kaizen_game()
