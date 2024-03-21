import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageEnhance

# Page configuration
st.set_page_config(
    page_title="Limgrave Middle School Band",
    page_icon="🎵",
    layout="wide"
)

# Define background color and text color
background_color = "#f3f3f3"
text_color = "#000000"

# Style the app with the chosen colors
st.markdown(
    f"""
    <style>
        body {{
            background-color: {background_color};
            color: {text_color};
            font-family: 'Arial', sans-serif;
        }}
        .streamlit-table {{
            color: {text_color};
        }}
        .section {{
            border: 1px solid #ddd;
            border-radius: 10px;
            overflow: hidden;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            background-color: #fff;
        }}
        .section-title {{
            font-size: 24px;
            color: #333;
            margin-bottom: 15px;
        }}
        .subheader {{
            font-size: 18px;
            color: #555;
            margin-top: 15px;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            color: #777;
            font-size: 14px;
        }}
        .image-container {{
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }}
        img {{
            max-width: 100%;
            border-radius: 8px;
        }}
        .navbar {{
            display: flex;
            justify-content: space-around;
            background-color: #333;
            padding: 10px;
        }}
        .navbar a {{
            color: white;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
        }}
        .navbar a:hover {{
            color: #ffcc00;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Function to set background color for individual sections
def set_section_background_color(section_color):
    st.markdown(
        f"""
        <style>
            .section {{
                background-color: {section_color};
                text-align: center;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to enhance image contrast and add text

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["Home", "Staff", "Private Lessons", "Teaching Schedule", "Future Members", "Band Calendar", "Resources"])

if page == "Home":
    # Home Page
    image_path = "band_logo.png"
    text = "Limgrave Middle School Band"
        
    # Add text to the image
    

    

    # Centering the title using CSS style
    st.markdown(
        "<h1 style='text-align: center;'>Limgrave Middle School Band</h1>", 
        unsafe_allow_html=True
    )
    st.image("band_logo.png", use_column_width=True)

    # Excellence, Inspiration, and Experience Section
    set_section_background_color("#b3ffb3")

    st.markdown("<p style='text-align: center; font-size: 40px;'>About Us</p>", unsafe_allow_html=True)

    # Add the additional information
    st.markdown("<p style='text-align: center; font-size: 24px;'>Our middle school band program has a rich history of nurturing young musicians and providing them with a comprehensive music education. We are committed to fostering a love for music and helping students develop their skills to their fullest potential.</p>", unsafe_allow_html=True)
    # Columns for Excellence, Inspiration, and Experience
    col1, col2, col3 = st.columns(3)

    # Excellence
    with col1:
        st.subheader("Excellence")
        st.write("Limgrave Middle School Band strives to be excellent in every way. This includes helping develop and build character with all of our students.")

    # Inspiration
    with col2:
        st.subheader("Inspiration")
        st.write("We hope to tell a story through our music and marching routines. May it inspire those who witness it and encourage our children who dream of being part of our band one day.")

    # Experience
    with col3:
        st.subheader("Experience")
        st.write("Our ultimate goal is to help prepare our students as they get ready for the challenges of college and other obstacles that they face with becoming an adult.")

    
    
    
    # Add separation lines and centered music quote
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 24px;'>Music is the divine way to tell beautiful, poetic things to the heart.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 24px;'> - Pablo Casals</p>", unsafe_allow_html=True)
    st.markdown("---")


# Staff Page
# Staff Page
elif page == "Staff":
    st.title("Meet the Directors of the Limgrave Middle School Band")
    
    # Sebastian - Band Director
    set_section_background_color("#b3ffb3")
    st.markdown("<p style='color: #333; font-size: 24px;'>Limgrave Middle School Band</p>", unsafe_allow_html=True)

    st.image("Sebastian.png", width=400)
    st.markdown("<p style='color: #003366; font-size: 40px; font-weight: bold;'>Sebastian Ortega, Head Director:</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Sebastian Ortega was born in Mexico but spent his formative years in El Paso, Texas. He developed a passion for music early on, which led him to pursue a Bachelor's degree in Music Education at the University of North Texas. After completing his studies, Sebastian returned to his hometown of El Paso, where he found his calling as a music educator at Limgrave Middle School.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>At Limgrave, Sebastian teaches a variety of music ensembles, including the Symphonic Band, Jazz Band, and Beginning Band. His dedication to music education extends beyond the classroom as he strives to inspire and mentor young musicians, nurturing their talents and instilling in them a love for music that will last a lifetime. Sebastian's commitment to his students and his craft makes him an invaluable member of the Limgrave Middle School community.</p>", unsafe_allow_html=True)
    
    

    # Line before Michael Moore's image
    st.markdown("---")

    # Michael Moore - Band Director
    set_section_background_color("#b3ffb3")
    st.image("michael_moore.jpg", width=400)
    st.markdown("<p style='color: #003366; font-size: 40px; font-weight: bold;'>Daniel Camilo Fuentes, Assistant Director:</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Daniel Fuentes, a native of El Paso, Texas, has always had a passion for music. After graduating from the University of Texas at El Paso with a Bachelor's degree in Music Education, Daniel embarked on a fulfilling career as a music educator.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Currently, Daniel is a dedicated member of the faculty at Limgrave Middle School, where he channels his expertise and enthusiasm into teaching the Concert Band and Beginning Band. His commitment to nurturing young musicians and fostering a love for music is evident in his dynamic and engaging teaching style.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>Outside of the classroom, Daniel continues to be an active member of the local music community, participating in various musical endeavors and performances. His passion for music and dedication to his students make him a valued asset to the Limgrave Middle School community.</p>", unsafe_allow_html=True)


# Private Lessons Page
elif page == "Private Lessons":
    st.title("Enhance your musical skills with private lessons!")
    
    set_section_background_color("#b3ffb3")
    st.markdown("<p style='color: #333; font-size: 24px;'>Limgrave Middle School Band</p>", unsafe_allow_html=True)
    # Information about private lessons
    set_section_background_color("#b3ffb3")
    st.markdown("<p style='font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 20px;'>Private lessons provide personalized instruction tailored to individual student needs. Our instructors are experienced professionals who are dedicated to helping students reach their musical goals. Lessons cover technique, repertoire, and musicianship, providing a well-rounded musical education.</p>", unsafe_allow_html=True)
    #st.write("Private lessons provide personalized instruction tailored to individual student needs. Our instructors are experienced professionals who are dedicated to helping students reach their musical goals. Lessons cover technique, repertoire, and musicianship, providing a well-rounded musical education.")

    st.markdown("---")

    # Benefits of private lessons
    st.subheader("Benefits of Private Lessons")
    col1, col2 = st.columns([2, 1])  # Adjust the width of the columns as needed
    with col1:
        st.write("- Customized instruction to suit your individual learning style and goals.")
        st.write("- Flexible scheduling options to accommodate your busy lifestyle.")
        st.write("- Personalized feedback and guidance from experienced instructors.")
        st.write("- Opportunities for performance and participation in recitals and competitions.")
        st.write("- Access to a supportive and encouraging learning environment.")
        
    with col2:
        st.image("music_pages.jpg", width = 300)  # Add your image here

    st.markdown("---")

    # Enrollment Process
    st.subheader("Enrollment Process")
    st.write("To enroll in private lessons, please email our staff with the following information:")
    st.write("- Your child’s name")
    st.write("- Instrument of interest")
    st.write("- Phone number")
    st.write("Our team will assist you with scheduling and answer any questions you may have.")

    st.markdown("---")

    # Contact Information
    st.subheader("Contact Information")
    st.write("Email: info@limegravemsband.com")
    st.write("Phone: 915-491-1276")


elif page == "Teaching Schedule":
    st.title("Course Schedule")
    set_section_background_color("#b3ffb3")
    st.markdown("<p style='color: #333; font-size: 24px;'>Limgrave Middle School Band</p>", unsafe_allow_html=True)
    
    # Set background color for the section
    set_section_background_color("#b3ffb3")

    # Define teaching schedule data
    schedule_data = [
        {"Class Name": "Symphonic Band", "Period": "1st", "Time": "8:49-9:32"},
        {"Class Name": "Concert Band", "Period": "2nd", "Time": "9:36-10:19"},
        {"Class Name": "Jazz Band", "Period": "6th", "Time": "1:18-2:01"},
        {"Class Name": "Beginning Band", "Period": "8th", "Time": "2:52-3:35"}
    ]

    class_descriptions = {
        "Symphonic Band": "An advanced ensemble performing a diverse repertoire of challenging music, showcasing the highest level of instrumental proficiency.",
        "Concert Band": "An intermediate-level ensemble featuring a wide range of musical styles, providing a platform for developing instrumental skills and ensemble performance techniques.",
        "Jazz Band": "A dynamic ensemble specializing in jazz, blues, and swing music, emphasizing improvisation and ensemble interaction.",
        "Beginning Band": "An introductory ensemble for students new to playing musical instruments, focusing on building fundamental skills and fostering a passion for music."
    }

    # Display teaching schedule with improved styling
    
    
    st.markdown("#### Below is the teaching schedule for Limgrave Middle School Band:")
    #st.image("course_schedule_image.jpg", width = 500)

    

    st.markdown("---")
    st.write("")

    # Display teaching schedule as a formatted table with periods and lines
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.write("### Period")
    with col2:
        st.write("### Class Name")
    with col3:
        st.write("### Time")
    with col4:
        st.write("### Description")

    for i, entry in enumerate(schedule_data):
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            st.write(entry["Period"])
        with col2:
            st.write(entry["Class Name"])
        with col3:
            st.write(entry["Time"])
        with col4:
            st.write(class_descriptions[entry["Class Name"]])
        
        # Add horizontal line between entries
        if i < len(schedule_data) - 1:
            st.markdown("---")
    st.markdown("_____")
    
    
    
    

    col1, col2, col3 = st.columns([.1, 1, .1])  # Adjust the width of the columns as needed
    with col1:
        st.write("")
    with col2:
        st.image("course_schedule_image.jpg", width = 1000)  # Add your image here
    with col3:
        st.write("")
    




# Future Members Page
elif page == "Future Members":
    st.title("Future Members")

    set_section_background_color("#b3ffb3")
    st.markdown("<p style='color: #333; font-size: 24px;'>Limgrave Middle School Band</p>", unsafe_allow_html=True)
    # Set background color for the section
    set_section_background_color("#b3ffb3")
    st.markdown("-----")

    # Display information for potential future members
    st.markdown("### Are you currently in elementary school and interested in joining our band program?")
    st.markdown("### Here's what you need to know:")
    st.markdown("#")
    st.markdown("#")
    

    st.markdown("### Instrument Sign-up Process:")
    st.write("#####   - Attend the parent meeting on **February 21, 2024** at **7:00 PM**.")
    st.write("#####   - Ensure your child selects band as one of their two electives.")

    st.markdown("#")
    st.markdown("#")

    st.markdown("### Recruitment Events/Instrument Fittings:")
    st.write("####   Band Fair:")
    st.write("#####      - **Date:** February 24, 2024")
    st.write("#####      - **Time:** 10:00 AM - 6:00 PM")

    st.markdown("-----")


    # Highschool Band Image
    st.title("Highschool Band")
    st.image("highschool_band.jpg", width=800)  # Replace "highschool_band_image.jpg" with your image path

    # Display information for potential future members
    st.markdown("### Interested in joining the Limgrave High School  Band? ")
    st.markdown("### Here's what you need to know:")

    st.markdown("#")
    

    st.write("#####   - Attend the parent meeting on July 1st at 7pm in the LHS Band Hall.")
    st.write("#####   - Make sure to pick band as your elective when registering for classes. ")
    st.write("#####   - Attend the LHS Band Camp from July 15-19 from 12-4pm")
    

    st.markdown("-----")




# Band Calendar Page
elif page == "Band Calendar":
    st.title("Upcoming Events")
    set_section_background_color("#b3ffb3")
    st.markdown("<p style='color: #333; font-size: 24px;'>Limgrave Middle School Band</p>", unsafe_allow_html=True)
    # Set background color for the section
    set_section_background_color("#b3ffb3")

    # Define band calendar events
    band_calendar_events = [
        {"Event": "Winter Concert", "Date": "December 15th, 2023", "Time": "7:00 PM", "Location": "Gymnasium"},
        {"Event": "6th Grade Parent Meeting", "Date": "February 21st, 2024", "Time": "7:00 PM", "Location": "Band Hall"},
        {"Event": "Instrument Selection", "Date": "February 24th, 2024", "Time": "10:00 AM - 6:00 PM", "Location": "Gymnasium"},
        {"Event": "Spring Concert", "Date": "April 19th, 2024", "Time": "7:00 PM", "Location": "Gymnasium"},
        {"Event": "Register for fall semester classes", "Date": "May 1st, 2024", "Time": "N/A", "Location": "Online"},
        {"Event": "Schedules finalize", "Date": "June 3rd, 2024", "Time": "N/A", "Location": "N/A"}
    ]

    # Display band calendar events in a table with formatting

    st.markdown("---")
    st.write("")  # Add some space between the title and the table

    # Define table headers
    st.markdown("<div style='display: flex; padding: 8px; background-color: #333; color: white;'>"
                "<div style='flex: 3; text-align: center;'>Event</div>"
                "<div style='flex: 2; text-align: center;'>Date</div>"
                "<div style='flex: 2; text-align: center;'>Time</div>"
                "<div style='flex: 3; text-align: center;'>Location</div>"
                "</div>", unsafe_allow_html=True)

    # Display each event row
    for event in band_calendar_events:
        st.markdown("<div style='display: flex; padding: 8px; border-bottom: 1px solid #ccc;'>"
                    f"<div style='flex: 3; text-align: center;'>{event['Event']}</div>"
                    f"<div style='flex: 2; text-align: center;'>{event['Date']}</div>"
                    f"<div style='flex: 2; text-align: center;'>{event['Time']}</div>"
                    f"<div style='flex: 3; text-align: center;'>{event['Location']}</div>"
                    "</div>", unsafe_allow_html=True)
        

    st.markdown("#")
    col1, col2, col3 = st.columns([.3, 1, .1])  # Adjust the width of the columns as needed
    with col1:
        st.write("")
    with col2:
        st.image("concert.jpg", width = 800)  # Add your image here
    with col3:
        st.write("")


# Resources Page
elif page == "Resources":
    st.title("Useful Resources")
    set_section_background_color("#b3ffb3")
    st.markdown("<p style='color: #333; font-size: 24px;'>Limgrave Middle School Band</p>", unsafe_allow_html=True)
    # Set background color for the section
    set_section_background_color("#b3ffb3")

    # Define resources
    resources = {
        "Renting instruments/buying supplies": "Olivas Music - [Website](https://www.olivasmusic.com/)",
        "Supplies to buy": " - [Supplies to buy](https://docs.google.com/document/d/1s2ooRCnHdiEiQ5rx26C38Tbra19EYkEaJuzJ7uJAtqw/edit?usp=sharing)",
        "Band Handbook": " - [Band Handbook](https://docs.google.com/document/d/1_ixyAX2Rpc4Cc7fRnCGQ14LPx6_K7BPEX52o6nFEcg4/edit?usp=sharing)"
    }

    # Display resources
   
    st.markdown("---")
    for category, link in resources.items():
        st.markdown(f"### **{category}**:")
        st.markdown(link)
        st.markdown("----")



    






















