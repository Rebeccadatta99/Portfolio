import streamlit as st
from PIL import Image
import pandas as pd
import io

# Page configuration
st.set_page_config(
    page_title="Your Name - Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1E90FF;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666666;
        margin-top: 0px;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #333333;
        border-bottom: 2px solid #1E90FF;
        padding-bottom: 10px;
        margin-top: 30px;
    }
    .skill-box {
        background-color: #F0F8FF;
        padding: 10px;
        border-radius: 5px;
        margin: 5px;
        display: inline-block;
    }
    .icon-link {
        margin-right: 20px;
        text-decoration: none;
    }
    .highlight {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with profile photo and contact info
with st.sidebar:
    # Create a placeholder image instead of loading from file
    st.markdown("### Profile Photo")
    #st.info("Replace this with your photo using `st.image(Image.open('your_photo.jpg'), width=250)`")

    st.markdown("## Contact Information")
    st.write("📧 your.email@example.com")
    st.write("📱 +1 (123) 456-7890")
    st.write("📍 City, Country")

    st.markdown("## Social Links")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourusername)")
    with col2:
        st.markdown(
            "[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)")
    with col3:
        st.markdown(
            "[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/yourusername)")

    st.markdown(
        "[![Portfolio](https://img.shields.io/badge/Portfolio-1DA1F2?style=for-the-badge&logo=web&logoColor=white)](https://yourportfolio.com)")

    # Create a dummy resume placeholder for download
    dummy_resume = io.BytesIO(b"This is a placeholder for your resume. Replace with your actual resume content.")

    #st.download_button(
        #label="Download Resume",
        #data=dummy_resume,
        #file_name="YourName_Resume.pdf",
        #mime="application/pdf"
    #)

# Main content
st.markdown('<p class="main-header">Your Name</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Professional Title | Industry</p>', unsafe_allow_html=True)

# Summary/About Me
st.markdown('<p class="section-header">About Me</p>', unsafe_allow_html=True)
st.markdown("""
<div class="highlight">
I am a passionate [your profession] with X years of experience specializing in [your specialization]. 
My background includes [brief overview of background]. I am particularly interested in [your interests] 
and am constantly seeking opportunities to [your goals]. My approach combines [your strengths] with 
[your unique perspective] to deliver [your value proposition].
</div>
""", unsafe_allow_html=True)

# Education
st.markdown('<p class="section-header">Education</p>', unsafe_allow_html=True)

education_data = [
    {"Degree": "Master of Science", "Field": "Computer Science", "Institution": "University Name",
     "Location": "City, Country", "Year": "20XX-20XX"},
    {"Degree": "Bachelor of Technology", "Field": "Information Technology", "Institution": "University Name",
     "Location": "City, Country", "Year": "20XX-20XX"}
]

for edu in education_data:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**{edu['Degree']} in {edu['Field']}**")
        st.write(f"{edu['Institution']}, {edu['Location']}")
    with col2:
        st.write(f"**{edu['Year']}**")
    st.markdown("---")

# Experience
st.markdown('<p class="section-header">Professional Experience</p>', unsafe_allow_html=True)

experience_data = [
    {
        "Title": "Senior Developer",
        "Company": "Company Name",
        "Duration": "Month 20XX - Present",
        "Description": [
            "Led development of [specific project], resulting in [specific outcome]",
            "Implemented [technology/process] that improved [metrics] by XX%",
            "Collaborated with cross-functional teams to deliver [specific results]"
        ]
    },
    {
        "Title": "Software Developer",
        "Company": "Previous Company",
        "Duration": "Month 20XX - Month 20XX",
        "Description": [
            "Developed and maintained [specific applications/systems]",
            "Improved [specific aspect] by implementing [specific solution]",
            "Participated in [specific initiatives] that enhanced [specific metrics]"
        ]
    }
]

for exp in experience_data:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**{exp['Title']} | {exp['Company']}**")
    with col2:
        st.write(f"**{exp['Duration']}**")

    for bullet in exp['Description']:
        st.write(f"• {bullet}")
    st.markdown("---")

# Skills
st.markdown('<p class="section-header">Skills</p>', unsafe_allow_html=True)

# Create tabs for different skill categories
skill_tabs = st.tabs(["Technical", "Languages", "Tools", "Soft Skills"])

with skill_tabs[0]:
    tech_skills = ["Python", "JavaScript", "React", "Node.js", "SQL", "Data Analysis", "Machine Learning", "AWS",
                   "Docker"]
    st.markdown('<div>' + ''.join([f'<span class="skill-box">{skill}</span>' for skill in tech_skills]) + '</div>',
                unsafe_allow_html=True)

with skill_tabs[1]:
    lang_skills = ["English (Native)", "Spanish (Fluent)", "French (Intermediate)"]
    st.markdown('<div>' + ''.join([f'<span class="skill-box">{skill}</span>' for skill in lang_skills]) + '</div>',
                unsafe_allow_html=True)

with skill_tabs[2]:
    tool_skills = ["Git", "JIRA", "Figma", "Adobe Creative Suite", "Microsoft Office", "Tableau", "Power BI"]
    st.markdown('<div>' + ''.join([f'<span class="skill-box">{skill}</span>' for skill in tool_skills]) + '</div>',
                unsafe_allow_html=True)

with skill_tabs[3]:
    soft_skills = ["Project Management", "Team Leadership", "Communication", "Problem Solving", "Critical Thinking",
                   "Agile Methodology"]
    st.markdown('<div>' + ''.join([f'<span class="skill-box">{skill}</span>' for skill in soft_skills]) + '</div>',
                unsafe_allow_html=True)

# Projects
st.markdown('<p class="section-header">Projects</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.expander("Project 1: Name of Project"):
        st.markdown("**Description:** Brief description of the project and your role.")
        st.markdown("**Technologies:** List of technologies used")
        st.markdown("**Key Achievements:**")
        st.markdown("• Achievement 1")
        st.markdown("• Achievement 2")
        st.markdown("**Links:** [GitHub](https://github.com/yourusername/project) | [Live Demo](https://demo-link.com)")

with col2:
    with st.expander("Project 2: Name of Project"):
        st.markdown("**Description:** Brief description of the project and your role.")
        st.markdown("**Technologies:** List of technologies used")
        st.markdown("**Key Achievements:**")
        st.markdown("• Achievement 1")
        st.markdown("• Achievement 2")
        st.markdown("**Links:** [GitHub](https://github.com/yourusername/project) | [Live Demo](https://demo-link.com)")

col3, col4 = st.columns(2)

with col3:
    with st.expander("Project 3: Name of Project"):
        st.markdown("**Description:** Brief description of the project and your role.")
        st.markdown("**Technologies:** List of technologies used")
        st.markdown("**Key Achievements:**")
        st.markdown("• Achievement 1")
        st.markdown("• Achievement 2")
        st.markdown("**Links:** [GitHub](https://github.com/yourusername/project) | [Live Demo](https://demo-link.com)")

with col4:
    with st.expander("Project 4: Name of Project"):
        st.markdown("**Description:** Brief description of the project and your role.")
        st.markdown("**Technologies:** List of technologies used")
        st.markdown("**Key Achievements:**")
        st.markdown("• Achievement 1")
        st.markdown("• Achievement 2")
        st.markdown("**Links:** [GitHub](https://github.com/yourusername/project) | [Live Demo](https://demo-link.com)")

# Certificates & Achievements
st.markdown('<p class="section-header">Certificates & Achievements</p>', unsafe_allow_html=True)

cert_tabs = st.tabs(["Certificates", "Achievements"])

with cert_tabs[0]:
    certs_data = [
        {"Name": "Certificate Name 1", "Issuer": "Issuing Organization", "Date": "Month Year",
         "Link": "https://certificate-link.com"},
        {"Name": "Certificate Name 2", "Issuer": "Issuing Organization", "Date": "Month Year",
         "Link": "https://certificate-link.com"},
        {"Name": "Certificate Name 3", "Issuer": "Issuing Organization", "Date": "Month Year",
         "Link": "https://certificate-link.com"}
    ]

    for cert in certs_data:
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.write(f"**{cert['Name']}**")
        with col2:
            st.write(cert['Issuer'])
        with col3:
            st.write(cert['Date'])
        st.markdown(f"[View Certificate]({cert['Link']})")
        st.markdown("---")

with cert_tabs[1]:
    achievements = [
        "Recognition award for [specific accomplishment] at [company/event]",
        "Published article on [specific topic] in [publication/platform]",
        "Speaker at [specific conference/event] on [specific topic]",
        "Winner of [specific award/competition]"
    ]

    for achievement in achievements:
        st.markdown(f"• {achievement}")

# Hobbies & Interests
st.markdown('<p class="section-header">Hobbies & Interests</p>', unsafe_allow_html=True)

hobby_cols = st.columns(3)
hobbies = [
    {"name": "Photography", "icon": "📷", "description": "Street photography and portraits"},
    {"name": "Hiking", "icon": "🥾", "description": "Explored over 20 trails in national parks"},
    {"name": "Reading", "icon": "📚", "description": "Science fiction and psychology books"},
    {"name": "Cooking", "icon": "🍳", "description": "Specializing in international cuisines"},
    {"name": "Chess", "icon": "♟️", "description": "Competitive player with ELO rating of 1800"},
    {"name": "Music", "icon": "🎸", "description": "Play guitar and compose original songs"}
]

for i, hobby in enumerate(hobbies):
    with hobby_cols[i % 3]:
        st.markdown(f"**{hobby['icon']} {hobby['name']}**")
        st.write(hobby['description'])

# Contact Form
st.markdown('<p class="section-header">Get In Touch</p>', unsafe_allow_html=True)
contact_form = st.form("contact_form")
name = contact_form.text_input("Name")
email = contact_form.text_input("Email")
message = contact_form.text_area("Message")
submit = contact_form.form_submit_button("Send Message")

if submit:
    st.success("Thanks for reaching out! I'll get back to you soon.")
    # In a real application, you would add code to handle form submission, like sending an email

# Footer
st.markdown("---")
st.markdown("© 2025 Your Name - All Rights Reserved")