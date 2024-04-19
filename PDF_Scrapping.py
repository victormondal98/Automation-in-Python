"""
To scrap any PDF we need a Python library called 'camelot'
But to use camelot, you must install two libraries first 'tk' and 'ghostscript'

If the PDF is scanned then, the python needs image interpreters to read the PDF. In this case
additional library is required. We can install 'opencv-python' library and cv2 method inside of it,
for image processing
"""


import camelot
import cv2

c = cv2.imread("C:\\Users\\USER\\Downloads\\Transcripts_4_years_of_Higher_Education_Victor_Mondal.pdf")

print(c)

# Define the file path using string concatenation
# file_path = "C:\\Users\\USER\\Downloads\\Transcripts_4_years_of_Higher_Education_Victor_Mondal.pdf"
File_Path = "C:\\Users\\USER\\Downloads\\foo.pdf"
fungy = camelot.read_pdf(File_Path, pages='1')
print(fungy)




