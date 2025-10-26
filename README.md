# Python Practice Tracker

A **Streamlit-based web app** to help you log, organize, and review your Python coding practice problems.  
Built for learners who want to stay consistent, track progress, and avoid forgetting old concepts.

---

##  Overview

The **Python Practice Tracker** lets you save every coding question you solve — along with your logic, what you learned, and even your code.  
It provides an interactive dashboard where you can:
- Add new practice entries
- Filter and review past problems
- Randomly pick older questions for spaced repetition
- Visualize your practice stats by topic

Everything is stored locally in a simple JSON file (`practice_log.json`) — no database setup needed.

---

##  Features

###  Add New Practice Entries
- Record each question with:
  - **Title**
  - **Topic** (loops, strings, lists, etc.)
  - **Logic** or approach
  - **What you learned or found difficult**
  - Optional **code snippet**
- Automatically saves with date and time.

###  View Entries
- See all your past entries in an expandable list.
- Filter by **topic** for quick access.
- View your stored code right in the browser.

###  Review Random Question
- Pick a random past question for quick recall.
- Reinforces learning through spaced repetition.

###  Stats & Topics Dashboard
- Bar chart showing how many problems you’ve solved per topic.
- Displays total entries and last update time.

---

## Why Use It

- Keeps your Python learning organized in one place.  
- Builds long-term memory through active recall and spaced repetition.  
- Helps you identify strong and weak topics.  
- Visualizes your progress for motivation.  

---

## Tech Stack

- **Language:** Python 3  
- **Frontend/UI:** [Streamlit](https://streamlit.io)  
- **Data Storage:** Local JSON file  
- **Libraries Used:** `streamlit`, `json`, `datetime`, `random`

---

##  Getting Started

1. Clone the Repository
git clone https://github.com/umamak064/python-coding-tracker.git
cd python-coding-tracker

2. Install Dependencies
pip install streamlit

3. Run the App
streamlit run practice_tracker_app.py



## Author

Umama Khan
📧 Email: umamasaeed.214@gmail.com
