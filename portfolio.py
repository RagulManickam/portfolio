import streamlit as st
from PIL import Image
import base64

# Set page title and icon
st.set_page_config(page_title="Ragul Manickam | Portfolio", page_icon="🌟", layout="wide")

# Function to add animated background
def add_animated_bg():
    animated_bg = """
    <style>
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #fbc2eb);
        background-size: 400% 400%;
        animation: gradientAnimation 10s ease infinite;
    }
    </style>
    """
    st.markdown(animated_bg, unsafe_allow_html=True)

# Apply the animated background
add_animated_bg()

# Sidebar Navigation
st.sidebar.title("🔹 Navigation")
nav_selection = st.sidebar.radio("Go to", ["Home", "Skills", "Projects", "Contact"])

# Home Section
if nav_selection == "Home":
    st.title("🚀 Welcome to My Portfolio")
    st.subheader("Hi, I'm K E Ragul Manickam!")
    st.write("A passionate **Data Scientist** & **AI Enthusiast** with expertise in Python, Machine Learning, and Data Visualization.")
    
    # Contact Info
    st.write("💎 Email: [ragulmanickam123@gmail.com](mailto:ragulmanickam123@gmail.com)")
    st.write("🔗 LinkedIn: [linkedin.com/in/ragul-manickam18](https://www.linkedin.com/in/ragul-manickam18)")
    st.write("💻 GitHub: [github.com/RagulManickam](https://github.com/RagulManickam)")
    
    st.markdown("---")

# Skills Section
elif nav_selection == "Skills":
    st.title("🛠 Technical Skills")

    skill_levels = {
        "Python (Pandas, NumPy, Scikit-Learn)": 90,
        "SQL (Joins, Window Functions)": 85,
        "Data Visualization (Tableau, Power BI, Matplotlib)": 80,
        "Machine Learning & AI": 75,
        "AWS (S3, EC2)": 65,
        "Data Preprocessing & EDA": 85
    }

    for skill, level in skill_levels.items():
        st.subheader(skill)
        st.progress(level / 100)  # Progress bar for skill levels

    st.markdown("---")

# Projects Section
elif nav_selection == "Projects":
    st.title("📌 Featured Projects")

    projects = [
        {
            "title": "Zomato Recommendation System",
            "desc": "Built an ML-based restaurant recommendation system using AWS & Streamlit.",
            "skills": "AWS, Machine Learning, Streamlit, Data Visualization"
        },
        {
            "title": "Industrial Copper Modeling",
            "desc": "Developed a predictive model for sales trends and lead classification.",
            "skills": "Data Pre-processing, EDA, Streamlit"
        },
        {
            "title": "Airbnb Analysis",
            "desc": "Analyzed Airbnb pricing and demand trends using MongoDB and Streamlit.",
            "skills": "Python, Data Visualization, EDA, MongoDB, Streamlit"
        }
    ]

    for project in projects:
        st.subheader(f"📌 {project['title']}")
        st.write(f"**Description:** {project['desc']}")
        st.write(f"**Skills Used:** {project['skills']}")
        st.markdown("---")

# Contact Section
elif nav_selection == "Contact":
    st.title("📬 Get in Touch")

    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

    if submit:
        if name and email and message:
            st.success("✅ Thank you! I'll get back to you soon.")
        else:
            st.error("❌ Please fill out all fields.")
