from gptvision import GPTVISION
import streamlit as st
from PIL import Image
import utils
import base64
import os
from dotenv import load_dotenv

st.set_page_config(
    page_title="Lyzr Screenshot to Code",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Lyzr Screenshot to Code")
st.markdown("## Welcome to the Lyzr Screenshot to Code!")
st.markdown("In this App you need to Upload Landing Page Screenshot. This app will Generated code to build this landing page")


api = st.sidebar.text_input("Enter Your OPENAI API KEY HERE", type="password")

if api:
    openai_4o_model = GPTVISION(api_key=api,parameters={})
else:
    st.sidebar.error("Please Enter Your OPENAI API KEY")

data = "data"
os.makedirs(data, exist_ok=True)


def encode_image(image_path):
        with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')


prompt = f"""
Analyze each component of Given Landing Page Screenshot and Write a code with all components in HTML,CSS and JS.
If You Find Any image in Given Screenshot.use this image url = "https://photographylife.com/wp-content/uploads/2023/05/Nikon-Z8-Official-Samples-00002.jpg"
Do Not Miss any Components of Given Screenshot.DO Not Change Position

**1. Identify Layout and Structure:**
    Break down the screenshot into its structural components (header, navigation bar, main content, footer, etc.).
    Identify any sections, columns, rows, or grids used in the layout.
    
**2. HTML:**
    Create a semantic HTML structure based on the identified layout.
    Use appropriate HTML5 tags (e.g., <header>, <nav>, <main>, <section>, <footer>) to improve readability and accessibility.
    Ensure all text content and images are included with appropriate tags (<h1>, <p>, <img>, etc.).
    Add relevant attributes (e.g., alt for images, id and class for styling and JavaScript hooks).
    
**3. CSS:**
    Extract the styling details from the screenshot (colors, fonts, sizes, spacing, etc.).
    Create a stylesheet (internal or external) and link it to the HTML file.
    Use CSS properties to match the visual style of the screenshot (e.g., background-color, font-family, margin, padding).
    Implement responsive design principles if necessary, using media queries to ensure the layout adapts to different screen sizes.
    Include any hover effects, animations, or transitions observed in the screenshot.
    
**4. JavaScript:**
    Identify any interactive elements (e.g., buttons, forms, sliders) and determine their behavior from the screenshot.
    Write JavaScript to handle interactions (e.g., form submissions, button clicks, modals).
    Ensure the code is unobtrusive and works well with the HTML and CSS.
    Include comments to explain the purpose of the code and any specific functionalities.
    
**5. Best Practices:**
    Follow best practices for HTML, CSS, and JavaScript coding, including proper indentation, naming conventions, and code organization.
    Ensure accessibility standards are met, including proper use of ARIA roles if needed.
    Validate HTML and CSS to check for any errors or issues.
    Test the final output in different browsers to ensure cross-browser compatibility.
"""

uploaded_files = st.file_uploader("Upload Nit sketch of product", type=['png', 'jpg'])
if uploaded_files is not None:
        st.success(f"File uploaded: {uploaded_files.name}")
        file_path = utils.save_uploaded_file(uploaded_files)
        if file_path is not None:
            st.image(file_path)
            if st.button("Generate"):
                encoded_image = encode_image(file_path)
                planning = openai_4o_model.generate_text(prompt=prompt, image_url=encoded_image)
                st.markdown(planning)



