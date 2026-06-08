#Name : section2.py 
#Author: Nigina Rashidova
#Description: About us page
#Date started: 08/06/2026

#__Imports__ 
import streamlit as st
import data_processor

#Get the number of students studying currently
student_data = data_processor.load_file("month3.csv")
llen = len(student_data)

st.set_page_config(page_title="Just SAT", layout="wide")

# __Using CSS for designing the about page____
st.markdown("""
<style>
    .hero-title { 
        font-size: 3rem;
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.7;
        margin-bottom: 2rem;
    }
    .stat-card {
        background: var(--secondary-background-color);
        border: 1px solid #e0e4ff;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: var(--primary-color);
    }
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.6;
        margin-top: 4px;
    }
    .section-tag {
        background: var(--secondary-background-color);
        color: var(--primary-color);
        padding: 4px 14px;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 0.8rem;
    }
    .feature-card {
        background: var(--background-color);
        border: 1px solid #e8eaf0;
        border-radius: 16px;
        padding: 1.4rem;
        height: 100%;
    }
    .feature-icon {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }
    .feature-title {
        font-weight: 700;
        font-size: 1rem;
        margin-bottom: 0.3rem;
    }
    .feature-desc {
        font-size: 0.9rem;
        opacity: 0.65;
        line-height: 1.5;
    }
    .teacher-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128,128,128,0.2);
    border-radius: 20px;
    padding: 2rem;
    }
    .score-badge {
    background: var(--primary-color);
    color: white;
    padding: 6px 16px;
    border-radius: 100px;
    font-size: 0.85rem;
    font-weight: 600;
    display: inline-block;
    margin-top: 0.5rem;
    }
    .tg-button {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #229ED9;
        color: white !important;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        text-decoration: none !important;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

#____Title and description____
st.image("logo.png", width=64)
st.markdown('<div class="hero-title">Just SAT 📑</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">The biggest online SAT school — built around <em>you</em>.</div>', unsafe_allow_html=True)

#__Button for telegram link___
st.markdown(
    '<a class="tg-button" href="https://t.me/jast_sat" target="_blank">:material/send: Join our Telegram channel</a>',
    unsafe_allow_html=True
)
st.divider()

# ____Stats key performance indicators____
st.markdown('<div class="section-tag">By the numbers</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    #number of active students
    st.markdown(f"""<div class="stat-card"><div class="stat-number">{llen}</div><div class="stat-label">Active students</div></div>""", unsafe_allow_html=True)
with c2:
    #SAT score of the teacher
    st.markdown("""<div class="stat-card"><div class="stat-number">1530</div><div class="stat-label">Teacher's SAT score</div></div>""", unsafe_allow_html=True)
with c3:
    #teaching experience of teacher
    st.markdown("""<div class="stat-card"><div class="stat-number">2 yrs</div><div class="stat-label">Teaching experience</div></div>""", unsafe_allow_html=True)
with c4:
    #how students improved their score
    st.markdown("""<div class="stat-card"><div class="stat-number">95%</div><div class="stat-label">Students improved score</div></div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# __Our approach section___
st.markdown('<div class="section-tag">Our approach</div>', unsafe_allow_html=True)
st.markdown("### Every student gets a personalized path")
st.markdown("We don't believe in one-size-fits-all SAT prep. Each student learns differently, moves at their own pace, and has unique strengths and gaps. That's why everything at Just SAT is built around the individual.")

#three containers with more information about approach of the center
f1, f2, f3 = st.columns(3)
with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Diagnostic-first learning</div>
        <div class="feature-desc">We start by identifying exactly where you are — your strengths, weak spots, and scoring potential — so every lesson counts.</div>
    </div>""", unsafe_allow_html=True)
with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Real-time progress tracking</div>
        <div class="feature-desc">You always know where you stand. Track your scores, completed modules, and deadlines — all in one dashboard.</div>
    </div>""", unsafe_allow_html=True)
with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💬</div>
        <div class="feature-title">Direct access to your teacher</div>
        <div class="feature-desc">No faceless platform. You study with Nigina directly — ask questions, get feedback, and feel supported throughout your journey.</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ____Teacher card___
st.markdown('<div class="section-tag">Meet your teacher</div>', unsafe_allow_html=True)

col_teacher, col_gap, col_quote = st.columns([0.45, 0.05, 0.5])

#More info about teacher in a seperate container
with col_teacher:
    st.markdown("""
    <div class="teacher-card">
        <div style="font-size:1.4rem; font-weight:800; margin-bottom:4px;">Nigina Rashidova</div>
        <div style="opacity:0.8; font-size:0.95rem; color:var(--text-color)">SAT Instructor & Founder of Just SAT</div>
        <div class="score-badge">🏆 SAT Score: 1530</div>
        <div style="margin-top:1.2rem; opacity:0.9; font-size:0.95rem; line-height:1.6;">
            2+ years of hands-on teaching experience, helping students across all levels crack the SAT with confidence.
        </div>
    </div>
    """, unsafe_allow_html=True)

#Words of the teacher in a seperate container
with col_quote:
    st.markdown("#### My teaching philosophy")
    st.markdown("""
    > *"The SAT is learnable. Every student I've worked with has improved — because we figure out the pattern, not just the content. I treat each student as an individual, not a number."*
    
    Nigina scored **1530 on the SAT** and has spent 2 years turning that experience into a structured, warm, and results-driven teaching approach. Whether you're starting from 900 or aiming for 1500+, Just SAT meets you where you are.
    """)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# _Ending section___
col_cta, _ = st.columns([0.6, 0.4])
with col_cta:
    st.markdown("### Ready to start your SAT journey?")
    #another telegram channel link button
    st.markdown("Join our Telegram channel for free resources, updates, and to get in touch with Nigina directly.")
    st.markdown(
        '<a class="tg-button" href="https://t.me/jast_sat" target="_blank">✈️ Join us on Telegram</a>',
        unsafe_allow_html=True
    )