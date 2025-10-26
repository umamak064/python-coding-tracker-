import streamlit as st
import json
import random
from datetime import datetime

DATA_FILE = "practice_log.json"


# ---------- Utility Functions ----------
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------- App UI ----------
st.set_page_config(page_title="Python Practice Tracker", page_icon="🐍", layout="centered")
st.title("Python Practice Tracker")
st.caption("Keep track of your Python practice progress with ease!")


menu = st.sidebar.radio("📘 Menu", ["Add New Entry", "View Entries", "Review Random", "Stats & Topics"])


# ---------- Add New Entry ----------
if menu == "Add New Entry":
    st.header("📝 Add a New Practice Entry")

    title = st.text_input("Question Title")
    topic = st.text_input("Topic (e.g., loops, strings, list)")
    logic = st.text_area("Briefly explain your logic")
    learned = st.text_area("What did you learn or find hard?")
    code = st.text_area("Paste your final code (optional)")

    if st.button(" Save Entry"):
        if not title or not topic or not logic:
            st.warning("Please fill at least the Title, Topic, and Logic fields.")
        else:
            entry = {
                "title": title,
                "topic": topic,
                "logic": logic,
                "learned": learned,
                "code": code,
                "date": datetime.now().strftime("%Y-%m-%d"),
            }

            data = load_data()
            data.append(entry)
            save_data(data)
            st.success(" Entry saved successfully!")


# ---------- View Entries ----------
elif menu == "View Entries":
    st.header("📚 All Practice Entries")

    data = load_data()
    if not data:
        st.info("No entries found. Add some from the sidebar!")
    else:
        topics = sorted(set(entry["topic"] for entry in data))
        selected_topic = st.selectbox("Filter by Topic", ["All"] + topics)

        for i, entry in enumerate(data, start=1):
            if selected_topic == "All" or entry["topic"] == selected_topic:
                with st.expander(f"{i}. {entry['title']} ({entry['topic']}) - {entry['date']}"):
                    st.markdown(f"**Logic:** {entry['logic']}")
                    st.markdown(f"**Learned:** {entry['learned']}")
                    if entry["code"]:
                        st.code(entry["code"], language="python")


# ---------- Review Random ----------
elif menu == "Review Random":
    st.header("🎯 Review Random Old Question")

    data = load_data()
    if not data:
        st.info("No entries available yet.")
    else:
        if st.button("🔀 Pick a Random Question"):
            entry = random.choice(data)
            st.subheader(f"🧩 {entry['title']} ({entry['topic']})")
            st.caption(f"Solved on: {entry['date']}")
            st.markdown(f"**Logic (try to recall before reading!):** {entry['logic']}")
            st.markdown(f"**What you learned:** {entry['learned']}")
            if entry["code"]:
                st.code(entry["code"], language="python")


# ---------- Stats & Topics ----------
elif menu == "Stats & Topics":
    st.header("📊 Practice Summary")

    data = load_data()
    if not data:
        st.info("No data yet. Add entries to see your progress!")
    else:
        # Explicitly define topics as a dict to satisfy type checker
        topics: dict[str, int] = {}

        for entry in data:
            topic_name = entry.get("topic", "Unknown")
            topics[topic_name] = topics.get(topic_name, 0) + 1

        st.write("###  Problems per Topic")
        st.bar_chart(topics)

        st.write("###  Total Entries:", len(data))
        st.write("Last updated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
