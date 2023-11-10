from pdfminer.high_level import extract_text
import nltk 
nltk.download('stopwords')
import re
from nltk.corpus import stopwords
import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')
STOPWORDS = set(stopwords.words('english'))
EDUCATION = [
        'be', 'b.e.', 'b.e', 'bs', 'b.s',
        'me', 'm.e', 'm.e.', 'ms', 'm.sc',
        'btech', 'b.tech', 'm.tech', 'mtech',
        'ssc', 'hsc', 'cbse', 'icse', 'masters', 'xii', 'bsc',
    ]

class Resumefunctions:

# Define all Function 
#!pip install pdfminer
#!pip install pdfminer.six


    

    def extract_text_from_pdf(file_path):
    
        text = extract_text(file_path)
        return text

    # Example usage: Extract text from a PDF file
    pdf_file_path = "/home/pranjal/Downloads/PRANJALRESUMEIB.pdf"
    extracted_text = extract_text_from_pdf(pdf_file_path)
    print(extracted_text)

    def CleanResume(txt):
        # Remove RT and cc
        cleanText = re.sub('RT|cc', ' ', txt)
        
        # Remove hashtags and words starting with #
        cleanText = re.sub('#\S+\s', ' ', cleanText)
        
        # Remove non-ASCII characters
        cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
        
        # Remove extra spaces
        cleanText = re.sub('\s+', ' ', cleanText)
        clean_text = re.sub('\s+', ' ', txt).strip()

        # Convert the text to lowercase
        cleanText = cleanText.lower()
        
        # Remove unwanted words and stop words
        stop_words = set(stopwords.words('english'))
        words = cleanText.split()
        cleanText = ' '.join([word for word in words if word not in stop_words])
        
        return cleanText

    def extract_name(resume_text):
        nlp_text = nlp(resume_text)

        # Initialize matcher with a vocab
        matcher = Matcher(nlp.vocab)

        # Define the pattern for the name (two consecutive proper nouns)
        pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]

        # Add the pattern to the matcher
        matcher.add('NAME', [pattern])

        # Find all matches in the text
        matches = matcher(nlp_text)

        for match_id, start, end in matches:
            span = nlp_text[start:end]
            return span.text
    name = extract_name(extracted_text)
    print(f'name', name)

    def extract_mobile_number(text):
        phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), text)

        if phone:
            number = ''.join(phone[0])
            if len(number) > 10:
                return '+' + number
            else:
                return number
    phone = extract_mobile_number(extracted_text)
    print(f"phone:", phone)

    
    def extract_email(email):
        email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", email)
        if email:
            try:
                return email[0].split()[0].strip(';')
            except IndexError:
                return None

    mail = extract_email(extracted_text)
    print(f'mail:',mail)


    nlp = spacy.load("en_core_web_sm")

    def extract_skills(sentence, skills_list):
        nlp_text = nlp(sentence)

        # Convert the sentence to lowercase for case-insensitive comparison
        sentence_lower = sentence.lower()

        # Initialize a list to store extracted skills
        extracted_skills = []

        # Check for skills in the sentence
        for skill in skills_list:
            if skill.lower() in sentence_lower:
                extracted_skills.append(skill)

        return extracted_skills

    # List of known skills
    skills_list = [
        # General Programming
        "Python",
        "Java",
        "C++",
        "JavaScript",
        "Ruby",
        "HTML",
        "CSS",
        "Git",

        # Data Science
        "R",
        "Data Manipulation",
        "Data Visualization",
        "Machine Learning",
        "Data Analysis",
        "Data Science",
        "SQL",
        "Big Data",
        "Data Mining",
        "Statistics",
        "Matplotlib",
        "Seaborn",
        "Pandas",
        "NumPy",
        "SciPy",
        "Scikit-learn",
        "TensorFlow",
        "Keras",
        "PyTorch",
        "Natural Language Processing",
        "NLP",
        "Deep Learning",

        # Web Development
        "React",
        "Angular",
        "Vue.js",
        "Node.js",
        "Express.js",
        "Django",
        "Flask",
        "RESTful APIs",
        "MongoDB",
        "MySQL",
        "Firebase",
        "Webpack",

        # Mobile App Development
        "React Native",
        "iOS",
        "Swift",
        "Android",
        "Kotlin",
        "Flutter",

        # DevOps and Cloud
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "Google Cloud",
        "Continuous Integration",
        "Continuous Deployment",
        "Jenkins",

        # UI/UX Design
        "Adobe Photoshop",
        "Adobe Illustrator",
        "Sketch",
        "User Interface Design",
        "User Experience Design",
        "Wireframing",
        "Prototyping",

        # Project Management
        "Agile",
        "Scrum",
        "Kanban",
        "Project Planning",
        "Team Leadership",

        # Business Analysis
        "Business Intelligence",
        "Requirements Gathering",
        "Data Modeling",
        "Process Mapping",
        "SWOT Analysis",

        # Sales and Marketing
        "Social Media Marketing",
        "Content Marketing",
        "Email Marketing",
        "SEO",
        "Google Analytics",
        "Market Research",
        "Sales Strategy",
        "Lead Generation",
        "Customer Relationship Management",

        # Finance and Accounting
        "Financial Analysis",
        "Budgeting",
        "Financial Modeling",
        "Bookkeeping",
        "Taxation",
        "Auditing",
        "Risk Management",

        # Human Resources
        "Talent Acquisition",
        "Employee Relations",
        "Performance Management",
        "Training and Development",
        "HR Policies and Procedures",

        # Teaching and Education
        "Curriculum Development",
        "Instructional Design",
        "Classroom Management",
        "Educational Technology",
        "Assessment and Evaluation",

        # Creative Writing
        "Copywriting",
        "Content Writing",
        "Blogging",
        "Editing",
        "Proofreading",
        "Creative Storytelling",

        # Language and Translation
        "Translation",
        "Interpretation",
        "Language Teaching",
        "Language Proficiency",

        # Healthcare and Medicine
        "Medical Diagnosis",
        "Patient Care",
        "Medical Records Management",
        "Health Informatics",
        "Medical Coding",
        "Clinical Research",

        # Engineering
        "Mechanical Engineering",
        "Electrical Engineering",
        "Civil Engineering",
        "Chemical Engineering",
        "Automotive Engineering",
        "Aerospace Engineering",
        "Industrial Engineering",
        "Software Engineering",
        "Hardware Engineering",
        "Embedded Systems",

        # Art and Design
        "Drawing",
        "Painting",
        "Illustration",
        "Animation",
        "Graphic Design",
        "Motion Graphics",
        "Photography",
        "Video Editing",

        # Hospitality and Culinary Arts
        "Cooking",
        "Baking",
        "Food Presentation",
        "Beverage Management",
        "Event Planning",
        "Customer Service",
        "Restaurant Management",

        # Retail and Sales
        "Merchandising",
        "Visual Merchandising",
        "Inventory Management",
        "Retail Sales",
        "Customer Service",

        # Legal
        "Contract Law",
        "Corporate Law",
        "Intellectual Property",
        "Legal Research",
        "Litigation",
        "Arbitration",

        # Administration
        "Office Management",
        "Administrative Support",
        "Record Keeping",
        "Event Coordination",
        "Time Management",
        "Calendar Management",

        # Social Services
        "Counseling",
        "Social Work",
        "Community Outreach",
        "Case Management",
        "Child Welfare",
        "Youth Services","Financial Analysis",
        "Financial Reporting",
        "Financial Modeling",
        "Financial Management",
        "Financial Planning",
        "Investment Banking",
        "Financial Risk Management",
        "Financial Forecasting",
        "Financial Statements",
        "Corporate Finance",
    ]
    # Extract and print skills from the input sentence
    extracted_skills = extract_skills(extracted_text, skills_list)
    if extracted_skills:
        print("Skills:", extracted_skills)
    else:
        print("No skills found in the sentence.")

    

   
    # Grad all general stop words

    # Education Degrees
    

    def extract_degree(resume_text):
        # Convert resume text to lowercase
        resume_text = resume_text.lower()

        nlp_text = nlp(resume_text)

        # Sentence Tokenizer
        nlp_text = [sent.text.strip() for sent in nlp_text.sents]

        # Extract education degree
        education_degrees = set()
        for text in nlp_text:
            for tex in text.split():
                # Replace all special symbols
                tex = re.sub(r'[?|$|.|!|,]', r'', tex)
                if tex.lower() in EDUCATION and tex.lower() not in STOPWORDS:
                    education_degrees.add(tex)

        return education_degrees
    education_degrees = extract_degree(extracted_text)

    # Print the extracted education degrees
    print("Education Degrees:", education_degrees)


    def extract_education(resume_text):
        # Convert the entire resume text and headings to lowercase for case-insensitive comparison
        resume_text_lower = resume_text.lower()
        headings_lower = ["education", "educational qualifications"]

        # Initialize variables to store the start and end indices of the education section
        start_index = -1
        end_index = -1

        for heading in headings_lower:
            heading_index = resume_text_lower.find(heading)
            if heading_index != -1:
                # Update the start_index if it is not set yet (i.e., the first heading found)
                if start_index == -1:
                    start_index = heading_index + len(heading)
                # Update the end_index with the index of the next heading or end of the document
                next_heading_index = min(
                    resume_text_lower.find(h, heading_index + len(heading)) for h in headings_lower + ["work experience", "experience", "projects", "skills", "summary", "achievements", "contact"]
                    if h in resume_text_lower[heading_index + len(heading):]
                )
                if next_heading_index != -1:
                    end_index = next_heading_index
                else:
                    end_index = len(resume_text)

        # Extract the education section
        if start_index != -1 and end_index != -1:
            education_section = resume_text[start_index:end_index].strip()
            return education_section
        else:
            return None
    # Assuming you have defined the extract_education function above,
    # you can test it with your resume text
    education = extract_education(extracted_text)
    if education:
        print("Education:\n", education)
    else:
        print("Education not found")


    def extract_location(resume_text):
        # Use regex to find the location pattern
        pattern = r"([A-Za-z]+,\s*[A-Za-z]+\s*[A-Za-z]+,\s*[A-Za-z]+\s*-\s*\d+)"
        matches = re.findall(pattern, resume_text,re.IGNORECASE)
        if matches:
            return matches[0].strip()
        return None
    location = extract_location(extracted_text)
    print("Location:", location)


    def extract_work_experience(resume_text):
        # Convert the entire resume text and headings to lowercase for case-insensitive comparison
        resume_text_lower = resume_text.lower()
        headings_lower = ["work experience", "experience"]

        # Initialize variables to store the start and end indices of the work experience section
        start_index = -1
        end_index = -1

        for heading in headings_lower:
            heading_index = resume_text_lower.find(heading)
            if heading_index != -1:
                # Update the start_index if it is not set yet (i.e., the first heading found)
                if start_index == -1:
                    start_index = heading_index + len(heading)
                # Update the end_index with the index of the next heading or end of the document
                next_heading_index = min(
                    resume_text_lower.find(h, heading_index + len(heading)) for h in headings_lower + ["education", "skills", "projects", "summary", "achievements", "contact"]
                    if h in resume_text_lower[heading_index + len(heading):]
                )
                if next_heading_index != -1:
                    end_index = next_heading_index
                else:
                    end_index = len(resume_text)

        # Extract the work experience section
        if start_index != -1 and end_index != -1:
            work_experience = resume_text[start_index:end_index].strip()
            return work_experience
        else:
            return None
    work_experience = extract_work_experience(extracted_text)
    if work_experience:
        print("Work Experience:\n", work_experience)
    else:
        print("Work Experience not found")

    def extract_projects(resume_text):
        # Convert the entire resume text and headings to lowercase for case-insensitive comparison
        resume_text_lower = resume_text.lower()
        headings_lower = ["projects", "personal projects"]

        # Initialize variables to store the start and end indices of the projects section
        start_index = -1
        end_index = -1

        for heading in headings_lower:
            heading_index = resume_text_lower.find(heading)
            if heading_index != -1:
                # Update the start_index if it is not set yet (i.e., the first heading found)
                if start_index == -1:
                    start_index = heading_index + len(heading)
                # Update the end_index with the index of the next heading or end of the document
                next_heading_index = min(
                    resume_text_lower.find(h, heading_index + len(heading)) for h in headings_lower + ["work experience", "experience", "education", "skills", "summary", "achievements", "contact"]
                    if h in resume_text_lower[heading_index + len(heading):]
                )
                if next_heading_index != -1:
                    end_index = next_heading_index
                else:
                    end_index = len(resume_text)

        # Extract the projects section
        if start_index != -1 and end_index != -1:
            projects_section = resume_text[start_index:end_index].strip()
            return projects_section
        else:
            return None

    projects = extract_projects(extracted_text)
    if projects:
        print("Projects:\n", projects)
    else:
        print("Projects not found")

    
    # Load the NER model
    nlp = spacy.load("en_core_web_sm")

    def extract_languages(resume_text):
        languages = []
        doc = nlp(resume_text)
        for ent in doc.ents:
            if ent.label_ == "LANGUAGE":
                languages.append(ent.text.strip())
        return languages

    def extract_additional_skills(resume_text):
        additional_skills = []
        # Assuming you have a list of additional skills to search for
        skills_to_search = ["python", "java", "data analysis", "project management", "communication", "teamwork", "problem-solving"]
        for skill in skills_to_search:
            if skill.lower() in resume_text.lower():
                additional_skills.append(skill)
        return additional_skills

    languages = extract_languages(extracted_text)
    print("Languages:", languages)

    additional_skills = extract_additional_skills(extracted_text)
    print("Additional Skills:", additional_skills)

    locations = extract_location(extracted_text)
    print("Locations:", locations)

Resume = Resumefunctions()
mobile = Resume.extract_mobile_number()
print(mobile)
