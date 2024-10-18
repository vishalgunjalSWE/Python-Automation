import PyPDF2
import pyttsx3

# Use PdfReader instead of PdfFileReader as PdfFileReader is deprecated
pdfReader = PyPDF2.PdfReader(open(r'Python-Speech\Vishal_ATS.pdf', 'rb'))

# Initialize the Pyttsx3 engine
speaker = pyttsx3.init()

# Loop through all the pages and convert the PDF to speech
for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()

# Optionally, save the speech output to an audio file
speaker.save_to_file(text, 'audio.mp3')

#### CASE 2: READ A STRING ####
# Example of reading a string and saving it to a speech file
string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

# Initialize the Pyttsx3 engine
engine = pyttsx3.init()

# Save the string to a file (mp3 or wav)
engine.save_to_file(string, 'speech.mp3')

# Wait until the engine has finished processing
engine.runAndWait()