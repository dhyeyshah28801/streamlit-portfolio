import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Dhyey Shah - Portfolio", layout="wide")
    
    # Inject custom CSS for overall style
    st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #E0E0E0;
        font-family: 'Helvetica Neue', sans-serif;
    }
    a {
        color: #03DAC6;
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.sidebar:
        selected_page = option_menu(
            "Navigation", 
            ["Home", "Projects", "Experience", "Skills", "Education", "Contact"],
            icons=["house", "code", "briefcase", "tools", "book", "envelope"],
            menu_icon="cast", 
            default_index=0,
            styles={
                "container": {"padding": "5px", "background": "linear-gradient(135deg, #141E30, #243B55)", "border-radius": "10px"},
                "icon": {"color": "#03DAC6", "font-size": "20px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px", "color": "white"},
                "nav-link-selected": {"background-color": "#03DAC6", "color": "#141E30", "border-radius": "5px"},
            }
        )
    
    pages = {
        "Home": home,
        "Projects": projects,
        "Experience": experience,
        "Skills": skills,
        "Education": education,
        "Contact": contact
    }
    
    pages[selected_page]()

def home():
    st.title("👋 Welcome to My Portfolio")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("profile.jpg", width=250,use_container_width=True)
        with open("./Dhyey_Shah_AWS_SWE_PLTFRM_ENG_2YR.pdf", "rb") as file:
                st.download_button(
                    label="Download Resume",
                    data=file,
                    file_name="./Dhyey_Shah_AWS_SWE_PLTFRM_ENG_2YR.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
    
    with col2:
        st.markdown(f"""
            <div style='background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px;'>
                <h3 style='color: #03DAC6;'>Hi, I'm Dhyey Shah!</h3>
                <p>A software developer passionate about cloud computing, web development, and scalable infrastructure.</p>
                <p>Explore my projects, experience, and skills through this interactive portfolio.</p>
                
            </div>
        """, unsafe_allow_html=True)


def projects():
    st.title("🚀 Projects")
    project_list = [
        ("NS2SQL - Natural Speech to SQL", "Developed an AI-powered speech-to-SQL model improving query generation using database-specific context injection. Combined techniques of text correction and database schema awareness to enhance query accuracy."),
        ("College Parking System", "A Python Django API leveraging OpenCV to detect and report available parking spots in real time. Uses Flask for API handling and integrates real-time image processing for parking availability updates."),
        ("Asset Manager", "A web app for tracking company assets, developed with AngularJS, Node.js, and MySQL. Implements JWT-based authentication, session management, and an intuitive admin panel for asset tracking."),
        ("API Gateway Integration with DynamoDB", "A serverless API Gateway-DynamoDB plugin using AWS CloudFormation, eliminating the need for Lambda functions. Enables direct API Gateway to DynamoDB communication for improved efficiency."),
        ("Steelo", "A supply chain management app for a steel manufacturer, developed using Flutter and PHP for inventory and order tracking. Automates order placement, route determination, and retail selling with real-time inventory updates.")
    ]
    
    for title, description in project_list:
        st.markdown(f"""
            <div style='background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 6px rgba(0,0,0,0.3); transition: transform 0.2s;'>
                <h4 style='color: #03DAC6;'>{title}</h4>
                <p>{description}</p>
            </div>
        """, unsafe_allow_html=True)

def experience():
    st.title("💼 Experience")
    experience_list = [
        ("Integration Developer - Distinction Dev (March 2024 - August 2024)", [
            "Developed infrastructure tools and CI/CD pipelines for a UK-based credit card provider.",
            "Integrated third-party APIs such as Salesforce, Mambu, and GoCardless using the Adapter design pattern in TypeScript with Inversify for IoC.",
            "Created serverless solutions with AWS-SDK for managing Lambda functions and real-time event fan-out systems.",
            "Built and documented adapters, development guides, and POCs for solution architects."
        ]),
        ("Software Developer - Distinction Dev (May 2023 - March 2024)", [
            "Built event-driven microservices on AWS for a large home improvement retailer in the UK.",
            "Optimized SQL queries with Sequelize ORM, reducing query execution time by 60%.",
            "Designed scalable frontend solutions with Vue.js and integrated Auth0 authentication for secure access.",
            "Developed and deployed full-stack applications consisting of Node.js REST APIs on AWS Cloud Infrastructure using Serverless Framework and CloudFormation."
        ]),
        ("Flutter Intern - Urbanweb Solutions (Dec 2022 - May 2023)", [
            "Developed a supply chain management mobile app for a steel manufacturer using Flutter and PHP.",
            "Led a team of interns, conducted client demos, and refined application workflows through user feedback."
        ]),
        ("Software Developer Intern - Cygnet Infotech (May 2022)", [
            "Created a company asset management system using AngularJS and Node.js.",
            "Implemented JWT authentication and session management for secure user access."
        ])
    ]
    
    for title, details in experience_list:
        st.markdown(f"""
            <div style='background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 6px rgba(0,0,0,0.3); transition: transform 0.2s;'>
                <h4 style='color: #03DAC6;'>{title}</h4>
                <ul>
                    {''.join(f'<li>{detail}</li>' for detail in details)}
                </ul>
            </div>
        """, unsafe_allow_html=True)

def skills():
    st.title("🛠 Skills")

    # Define skills and corresponding proficiency levels
    skills_data = {
        "Programming Languages": {"Python": 90, "Java": 80, "TypeScript": 75, "Node.js": 70},
        "Frontend Technologies": {"React": 85, "Angular": 70, "Vue.js": 65},
        "Backend & Databases": {"Express.js": 80, "Flask": 75, "MySQL": 85, "PostgreSQL": 80},
        "Cloud & DevOps": {"AWS": 80, "Serverless Framework": 75, "Datadog": 70},
        "Tools & Frameworks": {"Jira": 80, "Figma": 70}
    }

    # Custom CSS for progress bars
    st.markdown("""
        <style>
            .progress-bar {
                background-color: #f0f2f6;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            .progress {
                background-color: #03DAC6;
                height: 20px;
                border-radius: 5px;
            }
            .skill-label {
                font-weight: bold;
                margin-bottom: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Display skills with progress bars
    for category, skills in skills_data.items():
        st.subheader(category)
        for skill, proficiency in skills.items():
            st.markdown(f"""
                <div class="skill-label">{skill}</div>
                <div class="progress-bar">
                    <div class="progress" style="width: {proficiency}%;"></div>
                </div>
            """, unsafe_allow_html=True)
def education():
    st.title("📚 Education")
    education_list = [
        ("Master of Science in Computer Science", "University of Texas at Dallas, Expected Graduation: August 2026"),
        ("Bachelor of Engineering in Computer Engineering", "Gujarat Technological University, CGPA: 9.5")
    ]
    
    for degree, details in education_list:
        st.markdown(f"""
            <div style='background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0px 4px 6px rgba(0,0,0,0.3); transition: transform 0.2s;'>
                <h4 style='color: #03DAC6;'>{degree}</h4>
                <p>{details}</p>
            </div>
        """, unsafe_allow_html=True)

def contact():
    st.title("📬 Get in Touch")
    st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px;'>
            <h4 style='color: #03DAC6;'>Let's Connect!</h4>
            <p>📧 Email: dhyeyshahr@gmail.com</p>
            <p>📍 Dallas, TX, USA</p>
            <p>🔗 <a href='https://www.linkedin.com/in/dhyeyshah28801' style='color: #03DAC6;'>LinkedIn</a></p>
            <p>📂 <a href='https://github.com/dhyeyshah28801' style='color: #03DAC6;'>GitHub</a></p>
        </div>
    """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
