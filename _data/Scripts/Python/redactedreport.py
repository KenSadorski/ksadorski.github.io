from docx import Document

# Load the document
doc_path = "C:\\Users\\ksado\Downloads\\Apply\\Github\\Projects\\WrittenProjects\\AssessmentReport.docx"
doc = Document(doc_path)

# Define phrases and keywords to redact (PII elements)
pii_terms = [
    "Hunter Neroni", "Ken Sadorski", "Macomb Community College", 
    "South Campus", "C and G buildings", "Business Department", 
    "Veterans Affairs", "Financial Aid", "Counseling", 
    "Academic services", "Professor Nabozny", "G Building", "C Building", 
    "Room 406", "Room 419", "Room 311-1", "Room 200", "Room 370", 
    "Room 324-2", "MCC", "MacombHelpDesk@Gmail.com", "Survey Monkey", 
    "GoPhish", "10/2023", "11/01/2019", "October 17, 2019", 
    "October 22, 2019", "October 29, 2019", "2019", "ITIA 2800", "FALL 2019"
]

# Redact PII terms by replacing them with '[REDACTED]'
for paragraph in doc.paragraphs:
    for term in pii_terms:
        if term in paragraph.text:
            paragraph.text = paragraph.text.replace(term, "[REDACTED]")

# Save the redacted document
redacted_doc_path = "C:\\Users\\ksado\\Downloads\\Apply\\Github\\Projects\\WrittenProjects\\AssessmentReport_Redacted.docx"
doc.save(redacted_doc_path)

redacted_doc_path
