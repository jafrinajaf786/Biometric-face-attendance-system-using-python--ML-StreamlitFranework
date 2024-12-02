# Biometric-face-attendance-system-using-python--ML-StreamlitFranework
 This is a Biometric Face Attendance System that allows automatic attendance marking by recognizing students or employees based on their facial features. The system uses machine learning to process images, and Streamlit is used to create an interactive web interface. The attendance is stored and managed in an Excel file.
# Author- Najaf Asghar Jafri
# Features
Face Recognition: The system uses a pre-trained machine learning model to recognize faces and map them to individuals.
Attendance Logging: When a face is detected, the system marks the attendance for the recognized individual.
Excel Integration: The attendance records are saved to an Excel sheet, allowing easy tracking and exporting of data.
Web Interface with Streamlit: A user-friendly interface allows users to interact with the system, view attendance, and manage settings.
# Requirements
To run the Face Attendance System, you will need the following Python libraries:
streamlit: For building the web interface.
opencv-python: For capturing video and detecting faces.
face-recognition: For recognizing and encoding faces.
pandas: For handling Excel file operations and storing attendance data.
xlrd / openpyxl: For reading and writing Excel files.
numpy: For numerical operations.
datetime: To track the time when attendance is marked.
# You can install these dependencies using pip:
pip install streamlit opencv-python face-recognition pandas xlrd openpyxl numpy

# How it Works
#  Facial Recognition:

The system uses the face_recognition library to encode faces from stored images and recognize them during the live feed.
Attendance Marking:

When a face is recognized, the system logs the current date and time and updates the attendance.xlsx file.
Excel File Management:

The system reads and writes data to the attendance.xlsx file. It appends attendance data if the individual is recognized.
# Troubleshooting
Issue: The system is not recognizing faces
Solution: Ensure that the images in the faces/ folder are clear and properly named.

Issue: Attendance is not being saved to Excel
Solution: Check the permissions of the attendance.xlsx file to ensure it's not read-only.

# Future Improvements
Integration with a database for better data management.
Real-time notifications when attendance is marked.
More advanced machine learning models for better accuracy.
Support for multiple cameras for large-scale systems.
