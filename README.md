# 📚 Just SAT — Student Progress Dashboard

An interactive web dashboard built for **Just SAT**, an online SAT preparation center. The app allows teachers to monitor student performance, track deadlines, and visualize individual progress — all in one place.

Built with **Python** and **Streamlit**.

---

## Pages

### 🏠 Home
The main overview of all students, built around three Key Performance Indicator (KPI) cards, a detailed data table, and a course popularity chart.

**KPI Cards**

There are three metric cards displayed at the top of the page, each filterable by month:

- 🥇 **Top Student** — Highlights the best-performing student based on the selected month. Displays the student's name, their average grade via a Streamlit metric widget, and a line chart of all their individual unit test grades.

- 📊 **Average Grade** — Shows the average grade across all students, the percentage of students with an *On Track* status, and an area chart of the grades of all students for a cohort-wide view.

- 🔴 **Students at Risk** — Displays the total number of at-risk students, the percentage they represent out of the full cohort, and a line chart of the average grades of all at-risk students.

**Student Data Table**

Below the KPI cards, a full interactive data table is displayed using Streamlit's `st.dataframe`. Each row represents one student and includes:
- Name
- Course
- Progress (rendered as a progress bar)
- All unit test grades (rendered as an inline line chart)
- Missed deadlines
- Average grade
- Status

**Course Popularity Chart**

At the bottom of the page, an interactive Plotly pie chart shows the distribution of students across courses — English only, Math only, and English & Math — giving a quick visual breakdown of course popularity across the cohort.

### 👩‍🎓 Student Profile
Search for any student by name to view their individual profile. Includes:
- Key info: course, unit test grades, status, missed deadlines
- Grade metric card showing growth from Month 1 → Month 3
- Line chart of grades over time
- Donut chart showing course completion percentage
- Downloadable PDF report with the student's key stats and charts

### ℹ️ About Us
An HTML/CSS-styled page with information about the Just SAT center, the teacher, and how to get in touch via Telegram.

---

## Progress Bar

The progress bar displays the percentage of units completed based on the student's current course. There are two courses with three possible positions:

| Position | Total Units |
|----------|-------------|
| English only | 11 units |
| Math only | 11 units |
| English & Math | 22 units |

Students enrolled in both English and Math have their progress calculated out of 22 units.

---

## Tech Stack

| Library | Purpose |
|---------|---------|
| `streamlit` | Web app framework |
| `pandas` | Data loading and processing |
| `numpy` | Status and progress calculations |
| `plotly` | Interactive charts in the web app |
| `matplotlib` | Chart image generation for PDF export |
| `fpdf2` | PDF report generation |

### Why both Plotly and Matplotlib?

Initially only Plotly was used for all charts. When exporting chart images for PDF reports, the `kaleido` engine (Plotly's image exporter) caused persistent bugs. To resolve this, **Matplotlib** was adopted specifically for PDF chart generation, while **Plotly** was kept for the web app due to its superior visual quality and interactivity.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/monbbdzy/EdTech-Dashboard.git
cd EdTech-Dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## Project Structure

```
EdTech-Dashboard/
├── app.py                  ← app entry point
├── data_processor.py       ← all data processing logic
├── pages/
│   ├── home.py             ← home page
│   ├── section1.py         ← student profile page
│   └── about.py            ← about us page
├── month1.csv              ← student data (Month 1)
├── month3.csv              ← student data (Month 3)
├── DejaVuSans.ttf          ← unicode font for PDF
├── DejaVuSans-Bold.ttf     ← unicode bold font for PDF
├── logo.png                ← school logo
├── requirements.txt
└── README.md
```

---

## What Could Be Improved

- **Better course name parsing** — currently the app expects exact strings like `"English&Math"`. Future versions could handle variations such as `"English and Math"`, `"math"`, `"english & math"`, etc.
- **Student avatars** — adding profile pictures or auto-generated avatars for better visual identification across the dashboard.
- **PDF design** — the current PDF report covers all key information but is minimal in design. It could be significantly improved by restructuring the layout using HTML/CSS-based rendering.

---

## Author

**Nigina Rashidova**  
SAT Instructor & Developer  
[Just SAT Telegram Channel](YOUR_TELEGRAM_LINK_HERE)
