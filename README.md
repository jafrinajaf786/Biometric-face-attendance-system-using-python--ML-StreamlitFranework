# Biometric-face-attendance-system-using-python--ML-StreamlitFranework
 This is a Biometric Face Attendance System that allows automatic attendance marking by recognizing students or employees based on their facial features. The system uses machine learning to process images, and Streamlit is used to create an interactive web interface. The attendance is stored and managed in an Excel file.<br>
# Author- Najaf Asghar Jafri
# Features
Face Recognition: The system uses a pre-trained machine learning model to recognize faces and map them to individuals.
<br>
Attendance Logging: When a face is detected, the system marks the attendance for the recognized individual.
<br>
Excel Integration: The attendance records are saved to an Excel sheet, allowing easy tracking and exporting of data.<br>
Web Interface with Streamlit: A user-friendly interface allows users to interact with the system, view attendance, and manage settings.<br>
# Requirements
To run the Face Attendance System, you will need the following Python libraries:<br>
streamlit: For building the web interface.<br>
opencv-python: For capturing video and detecting faces.<br>
face-recognition: For recognizing and encoding faces.<br>
pandas: For handling Excel file operations and storing attendance data.<br>
xlrd / openpyxl: For reading and writing Excel files.<br>
numpy: For numerical operations.<br>
datetime: To track the time when attendance is marked.<br>
# You can install these dependencies using pip:
pip install streamlit opencv-python face-recognition pandas xlrd openpyxl numpy

# How it Works
#  Facial Recognition:

The system uses the face_recognition library to encode faces from stored images and recognize them during the live feed.<br>
Attendance Marking:

When a face is recognized, the system logs the current date and time and updates the attendance.xlsx file.<br>
Excel File Management:

The system reads and writes data to the attendance.xlsx file. It appends attendance data if the individual is recognized.<br>

# Future Improvements
Integration with a database for better data management.<br>
Real-time notifications when attendance is marked.<br>
More advanced machine learning models for better accuracy.<br>
Support for multiple cameras for large-scale systems.<br>
