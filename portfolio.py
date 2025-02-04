import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Dhyey Shah - Portfolio", layout="wide")
    
    with st.sidebar:
        selected_page = option_menu(
            "Navigation", 
            ["Home", "Projects", "Experience", "Skills", "Education", "Contact"],
            icons=["house", "code", "briefcase", "tools", "book", "envelope"],
            menu_icon="cast", 
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "black"},
                "icon": {"color": "#4CAF50", "font-size": "20px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                "nav-link-selected": {"background-color": "#4CAF51", "color": "white"},
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
        st.image("profile.jpg", width=250)
    
    with col2:
        st.write("Hi, I'm Dhyey Shah, a software developer passionate about cloud computing, web development, and scalable infrastructure.")
        st.markdown("---")
        st.write("Explore my projects, experience, and skills through this interactive portfolio.")

def projects():
    st.title("🚀 Projects")
    st.write("### NS2SQL - Natural Speech to SQL")
    st.write("Developed an AI-powered speech-to-SQL model improving query generation using database-specific context injection. Combined techniques of text correction and database schema awareness to enhance query accuracy.")
    
    st.write("### College Parking System")
    st.write("A Python Django API leveraging OpenCV to detect and report available parking spots in real time. Uses Flask for API handling and integrates real-time image processing for parking availability updates.")
    
    st.write("### Asset Manager")
    st.write("A web app for tracking company assets, developed with AngularJS, Node.js, and MySQL. Implements JWT-based authentication, session management, and an intuitive admin panel for asset tracking.")
    
    st.write("### API Gateway Integration with DynamoDB")
    st.write("A serverless API Gateway-DynamoDB plugin using AWS CloudFormation, eliminating the need for Lambda functions. Enables direct API Gateway to DynamoDB communication for improved efficiency.")
    
    st.write("### Steelo")
    st.write("A supply chain management app for a steel manufacturer, developed using Flutter and PHP for inventory and order tracking. Automates order placement, route determination, and retail selling with real-time inventory updates.")

def experience():
    st.title("💼 Experience")
    st.write("### Integration Developer - Distinction Dev (March 2024 - August 2024)")
    st.write("- Developed infrastructure tools and CI/CD pipelines for a UK-based credit card provider.")
    st.write("- Integrated third-party APIs such as Salesforce, Mambu, and GoCardless using the Adapter design pattern in TypeScript with Inversify for IoC.")
    st.write("- Created serverless solutions with AWS-SDK for managing Lambda functions and real-time event fan-out systems.")
    st.write("- Built and documented adapters, development guides, and POCs for solution architects.")
    
    st.write("### Software Developer - Distinction Dev (May 2023 - March 2024)")
    st.write("- Built event-driven microservices on AWS for a large home improvement retailer in the UK.")
    st.write("- Optimized SQL queries with Sequelize ORM, reducing query execution time by 60%.")
    st.write("- Designed scalable frontend solutions with Vue.js and integrated Auth0 authentication for secure access.")
    st.write("- Developed and deployed full-stack applications consisting of Node.js REST APIs on AWS Cloud Infrastructure using Serverless Framework and CloudFormation.")
    
    st.write("### Flutter Intern - Urbanweb Solutions (Dec 2022 - May 2023)")
    st.write("- Developed a supply chain management mobile app for a steel manufacturer using Flutter and PHP.")
    st.write("- Led a team of interns, conducted client demos, and refined application workflows through user feedback.")
    
    st.write("### Software Developer Intern - Cygnet Infotech (May 2022)")
    st.write("- Created a company asset management system using AngularJS and Node.js.")
    st.write("- Implemented JWT authentication and session management for secure user access.")

def skills():
    st.title("🛠️ Skills")
    skill_categories = {
        "Programming Languages": ["Python", "JavaScript", "TypeScript", "Java", "C/C++"],
        "Frameworks & Libraries": ["React.js", "Vue.js", "Node.js", "AngularJS", "Flask"],
        "Cloud & DevOps": ["AWS", "Microsoft Azure", "Google Cloud", "Terraform", "Docker"],
        "Databases": ["SQL (MySQL, PostgreSQL)", "NoSQL (MongoDB, DynamoDB)"],
        "Tools": ["Datadog", "Figma", "JIRA", "Git", "CI/CD (GitHub Actions)"]
    }
    for category, skills in skill_categories.items():
        st.write(f"**{category}**: {', '.join(skills)}")

def education():
    st.title("📚 Education")
    st.write("### University of Texas - Dallas (August 2024 - May 2026)")
    st.write("Master's in Computer Science (GPA: 3.78)")
    st.write("Relevant Coursework: Algorithms, Big Data, Software Evolution, Database Design, Web Development, Machine Learning")
    
    st.write("### Gujarat Technological University (June 2019 - June 2023)")
    st.write("Bachelor's in Computer Engineering (GPA: 9.5)")
    st.write("Relevant Coursework: Algorithms, Data Structures, DBMS, Web Programming, Mobile Development (Android Java), Computer Vision")

def contact():
    st.title("📬 Get in Touch")
    st.write("Let's connect and collaborate!")
    st.markdown("📧 Email: dhyeyshahr@gmail.com")
    st.markdown("📍 Dallas, TX, USA")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/dhyeyshah28801)")
    st.markdown("📂 [GitHub](https://github.com/dhyeyshah28801)")
    
if __name__ == "__main__":
    main()
