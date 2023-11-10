#Gradio 
import gradio as gr
from resumeextractionfnc import ResumeFunctions
from pdfminer.high_level import extract_text

# Instantiate the class
resume_handler = ResumeFunctions()

# Function to extract text from a PDF
def extract_text_from_pdf(file_path):
    text = extract_text(file_path)
    return text

# Function to process the resume text and extract information
def extract_resume_information(pdf_file_path):
    # Extract text from the PDF file
    extracted_text = extract_text_from_pdf(pdf_file_path)
    
    # Process the extracted text using ResumeFunctions class
    if not isinstance(extracted_text, str):
        return "Error: extracted_text is not a valid string."

    # Extract and print Name
    name = resume_handler.extract_name(extracted_text)
    if name:
        name_output = "Name: " + name
    else:
        name_output = "Name not found"

    # Extract and print Contact Number
    contact_number = resume_handler.extract_mobile_number(extracted_text)
    if contact_number:
        contact_output = "Contact Number: " + contact_number
    else:
        contact_output = "Contact Number not found"

    # Extract and print Email
    email = resume_handler.extract_email(extracted_text)
    if email:
        email_output = "Email: " + email
    else:
        email_output = "Email not found"

    # Extract and print Education
    extracted_education = resume_handler.extract_education(extracted_text)
    if extracted_education:
        education_output = "Education: " + extracted_education
    else:
        education_output = "No education information found"

    # Extract and print Degree
    education_degrees = resume_handler.extract_degree(extracted_text)
    if education_degrees:
        degree_output = "Degree: " + education_degrees
    else:
        degree_output = "No Degree information found"

    # Extract Location
    location = resume_handler.extract_location(extracted_text)
    location_output = "Location: " + location

    # Extract work exp
    work_experience = resume_handler.extract_work_experiences(extracted_text)
    work_experience_output = "Work Experience: " + work_experience

    # Extract and print skills from the input sentence
    skills_list = ['skill1', 'skill2', 'skill3']  # Replace with your actual skills list
    extracted_skills = resume_handler.extract_skills(extracted_text, skills_list)
    if extracted_skills:
        skills_output = "Skills: " + ", ".join(extracted_skills)
    else:
        skills_output = "No skills found in the sentence."

    # Extract projects
    projects = resume_handler.extract_projects(extracted_text)
    if projects:
        projects_output = "Projects:\n" + projects
    else:
        projects_output = "Projects not found"

    # Combine all the extracted information
    result = (
        name_output + "\n"
        + contact_output + "\n"
        + email_output + "\n"
        + education_output + "\n"
        + degree_output + "\n"
        + location_output + "\n"
        + work_experience_output + "\n"
        + skills_output + "\n"
        + projects_output
        # Add other information if needed
    )
    return result

# Gradio Interface
iface = gr.Interface(
    fn=extract_resume_information,
    inputs=gr.inputs.File(label="Upload Resume PDF"),
    outputs="text",
    live=True,
    title="Resume Information Extractor",
    description="Extract Name, Contact Number, Email, Education, Skills, Degree, Location, Work Experience, and Projects from a Resume.",
    debug=True  # Enable Gradio's debug mode
)

# Launch the Gradio interface
iface.launch()
