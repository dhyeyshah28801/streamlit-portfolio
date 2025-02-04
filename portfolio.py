import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Dhyey Shah - Portfolio", layout="wide")
    
    with st.sidebar:
        selected_page = option_menu(
            "Navigation", 
            ["Home", "Projects", "Experience", "Skills", "Contact"],
            icons=["house", "code", "briefcase", "tools", "envelope"],
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
        "Contact": contact
    }
    
    pages[selected_page]()

def home():
    st.title("👋 Welcome to My Portfolio")
    # st.image("profile.jpg", width=250)
    st.write("Hi, I'm Dhyey Shah, a software developer passionate about cloud computing, web development, and scalable infrastructure.")
    st.markdown("---")
    st.write("Explore my projects, experience, and skills through this interactive portfolio.")

def projects():
    st.title("🚀 Projects")
    st.write("### NS2SQL - Natural Speech to SQL")
    st.write("Developed an AI-powered speech-to-SQL model improving query generation using database-specific context injection.")
    
    st.write("### College Parking System")
    st.write("A Python Django API leveraging OpenCV to detect and report available parking spots in real time.")
    
    st.write("### Asset Manager")
    st.write("A web app for tracking company assets, developed with AngularJS, Node.js, and MySQL.")
    
    st.write("### API Gateway Integration with DynamoDB")
    st.write("A serverless API Gateway-DynamoDB plugin using AWS CloudFormation, eliminating the need for Lambda functions.")

def experience():
    st.title("💼 Experience")
    st.write("### Integration Developer - Distinction Dev (March 2024 - August 2024)")
    st.write("- Developed infrastructure tools and CI/CD pipelines for a UK-based credit card provider.")
    st.write("- Integrated third-party APIs using the Adapter design pattern in TypeScript with Inversify for IoC.")
    st.write("- Created serverless solutions with AWS-SDK for managing Lambda functions and real-time event fan-out systems.")
    
    st.write("### Software Developer - Distinction Dev (May 2023 - March 2024)")
    st.write("- Built event-driven microservices on AWS for a large home improvement retailer in the UK.")
    st.write("- Optimized SQL queries with Sequelize ORM, improving query execution speed by 60%.")
    st.write("- Designed scalable frontend solutions with Vue.js and integrated Auth0 authentication.")
    
    st.write("### Flutter Intern - Urbanweb Solutions (Dec 2022 - May 2023)")
    st.write("- Developed a supply chain management mobile app for a steel manufacturer using Flutter and PHP.")
    
    st.write("### Software Developer Intern - Cygnet Infotech (May 2022)")
    st.write("- Created a company asset management system using AngularJS and Node.js, implementing JWT authentication.")

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

def contact():
    st.title("📬 Get in Touch")
    st.write("Let's connect and collaborate!")
    st.markdown("📧 Email: dhyeyshahr@gmail.com")
    st.markdown("📍 Dallas, TX, USA")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/dhyeyshah28801)")
    st.markdown("📂 [GitHub](https://github.com/dhyeyshah28801)")
    
if __name__ == "__main__":
    main()
