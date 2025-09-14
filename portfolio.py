import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Portfolio - Girish Pardeshi", page_icon="📊", layout="wide")

# ---- HELPER FUNCTIONS ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- LOAD CSS ----
local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/dca6e95f-a693-4c1e-9576-9b66b6281a5e/gCyER1y3dR.json")
img_firstbi = Image.open("images/firstbi.png")
img_tableu = Image.open("images/tableu.png")
img_secondbi = Image.open("images/secondbi.png")
img_smpa = Image.open("images/SMPA.png")

# ---- NAVIGATION ----
tabs = st.tabs(["🏠 Home", "💡 Skills", "📂 Projects", "🎓 Education", "📞 Contact"])

# ---- HOME TAB ----
with tabs[0]:
    # Hero Section
    st.markdown("""
        <div style="text-align:center; padding:40px 0;">
            <h1 style="font-size:60px; margin-bottom:0;">👋 Hi, I'm <span style='color:#4CAF50'>Girish Pardeshi</span></h1>
            <h3 style="margin-top:10px;">Turning Data into Decisions | Aspiring Data Analyst</h3>
        </div>
    """, unsafe_allow_html=True)

    # Intro and CTA
    st.write(
        "I'm passionate about using **Python, SQL,Machine Learning, Power BI, and Tableau** to solve business problems and build impactful dashboards. With a strong academic record and hands-on projects, I aim to transform raw data into actionable insights."
    )

    colA, colB, colC = st.columns(3)
    with colA:
        st.metric("Dashboards", "5+")
    with colB:
        st.metric("Projects", "8+")
    with colC:
        st.metric("Virtual Internships", "2")

    st.markdown("""
    <div style="text-align:center; padding:20px;">
        <a href="https://github.com/GirishRPardeshi"><button style="padding:10px 20px; margin:10px; background:#4CAF50; color:white; border:none; border-radius:8px; font-size:16px; cursor:pointer;">📂 View My Projects</button></a>
        <a href="#contact"><button style="padding:10px 20px; margin:10px; background:#2196F3; color:white; border:none; border-radius:8px; font-size:16px; cursor:pointer;">📄 Download Resume</button></a>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        left_column, right_column = st.columns([2, 1])
        with left_column:
            st.header("What I Do")
            st.write(
                """
                • Building interactive dashboards and analytical applications from scratch.  
                • Experienced in Python, SQL, Power BI, Tableau, and Machine Learning.  
                • Strong academic background with distinction in B.Sc. CS and MCA (in progress).  
                • Skilled in transforming datasets into actionable insights and forecasts.  

                👉 Reach out on [LinkedIn](https://linkedin.com/in/girish-pardeshi-gp7871/)
                """
            )
        with right_column:
            st_lottie(lottie_coding, height=250, key="coding")

# ---- SKILLS TAB ----
with tabs[1]:
    with st.container():
        st.header("Hard Skills & Soft Skills")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔧 Hard Skills")
            st.write("""
            • Python (Pandas, NumPy, Matplotlib, Scikit-learn)  
            • R, SQL, C++  
            • Databases: MySQL, RDBMS concepts  
            • Power BI, Tableau, Streamlit  
            • Machine Learning (regression, classification, preprocessing)  
            • Azure fundamentals, Docker basics  
            • Excel (pivot tables, advanced functions)
            """)

        with col2:
            st.subheader("🤝 Soft Skills")
            st.write("""
            • Effective Presentation  
            • Decision Making  
            • Communication (English, Hindi, Marathi)  
            • Creativity & Critical Thinking  
            • Teamwork & Collaboration  
            • Multi-tasking
            """)

# ---- PROJECTS TAB ----
with tabs[2]:
    st.header("My Projects")

    project_data = [
        {
            "title": "📈 Stock Market Performance Analyzer (Streamlit)",
            "img": img_smpa,
            "desc": "Built a web app analyzing U.S. & Indian stock performance with EDA, volatility patterns, and trend forecasting.",
            "link": "",
        },
        {
            "title": "🏬 Walmart Sales Dashboard (Power BI)",
            "img": img_secondbi,
            "desc": "Interactive dashboard with KPIs, slicers, and advanced charts, reducing manual reporting time.",
            "link": "",
        },
        {
            "title": "📊 Amazon Sales Dashboard (Tableau)",
            "img": img_tableu,
            "desc": "Designed Tableau dashboard with interactive time-series analysis, boosting user engagement by 90%.",
            "link": "https://public.tableau.com/app/profile/girish.pardeshi/viz/E-CommerceSalesDashboard_17022238961680/Dashboard1",
        },
        {
            "title": "🛒 Ecommerce Sales Dashboard (Power BI)",
            "img": img_firstbi,
            "desc": "Developed intuitive sales dashboard with drill-downs and filters for deeper insights.",
            "link": "",
        },
    ]

    for proj in project_data:
        with st.container():
            img_col, text_col = st.columns([1, 2])
            with img_col:
                st.image(proj["img"])
            with text_col:
                st.subheader(proj["title"])
                st.write(proj["desc"])
                if proj["link"]:
                    st.markdown(f"[🔗 View Project]({proj['link']})")

# ---- EDUCATION TAB ----
with tabs[3]:
    st.header("Education")
    st.markdown(
        """
        🎓 **Bachelor of Science in Computer Science** – Moolji Jaitha College, Jalgaon (2021-2024)  
        CGPA: 9.07/10

        🎓 **Master of Computer Applications (MCA)** – NMU Jalgaon (2024-2026, in progress)  
        Current CGPA: 8.58/10
        """
    )

# ---- CONTACT TAB ----
with tabs[4]:
    st.header("Get In Touch With Me")
    st.write("Fill the form below or connect on LinkedIn/GitHub.")

    contact_form = """
    <form action="https://formsubmit.co/girishpardeshi7871@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
        st.markdown("""
        📧 [Email](mailto:girishpardeshi7871@gmail.com)  
        🔗 [LinkedIn](https://linkedin.com/in/girish-pardeshi-gp7871/)  
        💻 [GitHub](https://github.com/GirishRPardeshi)
        """)
    with right_col:
        st.empty()

    st.download_button(
        label="📄 Download My Resume",
        data=open("Girish_Resume_RBIS.pdf", "rb").read(),
        file_name="Girish_Pardeshi_Resume.pdf",
        mime="application/pdf",
    )