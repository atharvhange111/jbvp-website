import streamlit as st

# Configure the page
st.set_page_config(page_title="JBVP Group of Institutions", layout="wide")

# Custom CSS for modern styling, smooth scrolling, and visual presentation
st.markdown("""
<style>
    html {
        scroll-behavior: smooth;
    }
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #4B5563;
        font-size: 1.2rem;
        margin-bottom: 40px;
    }
    .section-card {
        background-color: #F3F4F6;
        padding: 30px;
        border-radius: 15px;
        border-left: 8px solid #1E3A8A;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .section-title {
        color: #1E3A8A;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .section-text {
        color: #374151;
        font-size: 1.1rem;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# Hero / Header Section
st.markdown('<h1 class="main-title">Jay Bhavanigad Vikas Pratishthan (JBVP)</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Vidya Niketan Group of Institutions — Lakhewadi, Pune</p>', unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1200&q=80", width=1200)

st.markdown("--- ")

# Quick Navigation Sidebar
st.sidebar.title("Campus Navigation")
st.sidebar.markdown("[🏠 Home](#jay-bhavanigad-vikas-pratishthan-jbvp)")
st.sidebar.markdown("[ℹ️ About Us](#about-us)")
st.sidebar.markdown("[🎓 Vidya Niketan Engineering College](#vidya-niketan-engineering-college)")
st.sidebar.markdown("[💊 Pharmacy College](#pharmacy-college)")
st.sidebar.markdown("[🏫 CBSE School (Nursery - 12th)](#cbse-school-nursery-to-12th)")
st.sidebar.markdown("[📖 SSC School](#ssc-school)")
st.sidebar.markdown("[📞 Contact Us](#contact-us)")

# Section: About Us
st.markdown('<div id="about-us"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-card" style="border-left-color: #4F46E5;">
    <div class="section-title">ℹ️ About Jay Bhavanigad Vikas Pratishthan (JBVP)</div>
    <div class="section-text">
        <b>Jay Bhavanigad Vikas Pratishthan (JBVP)</b> is a registered socio-educational trust founded with a core vision to democratize access to high-quality professional and technical education in rural and semi-urban landscapes.
        <br><br>
        Our flagship institutions are situated in the scenic and culturally rich region of Lakhewadi (Indapur, Pune), close to the historic and peaceful confluence of the Neera and Bheema rivers.
        <ul>
            <li><b>Our Vision:</b> To empower rural youth with technical proficiency, strong ethical values, and leadership traits to excel in global careers.</li>
            <li><b>Key Pillars:</b> Modern state-of-the-art infrastructure, a committed and highly-experienced faculty team, active industry collaborations, and extensive community support systems.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Section 1: Engineering College (Updated with User Info)
st.markdown('<div id="vidya-niketan-engineering-college"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-card">
    <div class="section-title">🚀 Vidya Niketan Institute of Engineering & Technology (VNIET)</div>
    <div class="section-text">
        Approved by AICTE (New Delhi), ISO 9001:2015 certified, recognized by the Government of Maharashtra, DTE Mumbai, and MSBTE. Affiliated to <b>Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere</b>.
        <br><br>
        Our beautiful 15-acre campus in Lakhewadi is located near the peaceful confluence of the Neera and Bheema rivers, offering top-tier technical education in semi-rural areas.
        <ul>
            <li><b>B.E. Courses Offered:</b> Computer Engineering, Civil Engineering, Mechanical Engineering, Electrical Engineering.</li>
            <li><b>Facilities:</b> Modern analytical and computer laboratories, digital classrooms, seminar halls, library, hostels, sports amenities, and campus-wide Wi-Fi.</li>
            <li><b>Key Features:</b> Scholarship schemes, dedicated placement assistance, and intensive industrial training.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Section 2: Pharmacy College
st.markdown('<div id="pharmacy-college"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-card" style="border-left-color: #059669;">
    <div class="section-title">💊 Vidya Niketan College of Pharmacy</div>
    <div class="section-text">
        Dedicated to creating next-generation healthcare professionals and researchers.
        <ul>
            <li><b>Courses Offered:</b> B.Pharm & D.Pharm.</li>
            <li><b>Features:</b> Fully-equipped chemistry labs, advanced pharmacology systems, and a dedicated medicinal botanical garden.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Section 3: CBSE School
st.markdown('<div id="cbse-school-nursery-to-12th"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-card" style="border-left-color: #D97706;">
    <div class="section-title">🏫 Vidya Niketan Public CBSE School (Nursery to 12th)</div>
    <div class="section-text">
        A progressive environment supporting standard Central Board of Secondary Education (CBSE) guidelines.
        <ul>
            <li><b>Nursery - 5th Grade:</b> Interactive play-based and inquiry-based learning.</li>
            <li><b>6th - 10th Grade:</b> Comprehensive focus on foundational sciences, mathematics, and life skills.</li>
            <li><b>11th & 12th Grade (Science & Commerce):</b> Tailored mentoring for boards and competitive engineering/medical entrance tests.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Section 4: SSC School
st.markdown('<div id="ssc-school"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-card" style="border-left-color: #DC2626;">
    <div class="section-title">📖 Vidya Niketan SSC School</div>
    <div class="section-text">
        State Board (SSC) affiliated curriculum delivering solid scholastic accomplishments paired with athletic growth and traditional cultural exposure.
        <ul>
            <li><b>Core Strengths:</b> High board-passing rates, expert state-board educators, and extensive vocational project activities.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer & Contact Section
st.markdown('<div id="contact-us"></div>', unsafe_allow_html=True)
st.markdown("--- ")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #4B5563;">
    <h3>📍 Contact Admissions & Administration</h3>
    <p><b>Address:</b> Vidya Niketan Institute of Engineering and Technology, Lakhewadi (A/P), Tal. Indapur, Dist. Pune, Maharashtra – 413103</p>
    <p>📧 <a href="mailto:jbvp.engineering@gmail.com">jbvp.engineering@gmail.com</a> | 🌐 <a href="http://vniet.edu.in" target="blank">vniet.edu.in</a></p>
    <p>📞 Phone: +91 72182 47777, +91 98901 37827</p>
    <p style="font-size: 0.9rem; margin-top: 15px;">© 2024 Jay Bhavanigad Vikas Pratishthan. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
