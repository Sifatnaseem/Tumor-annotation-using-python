# Tumor-annotation-using-python
Manual Tumor detection from X-ray along with the tumor description using a python program
AIM:
The aim of this project is to build a python program that helps the user manually annotate X-ray images for tumor detection and add a description of the tumor using the GUI canvas and label widgets and save the description as a text file for future reference. This will allow the user to keep a record or track of the disease and will allow the user to modify the information if needed in the future. It will ultimately save the user’s time and help them to make better-informed decisions and improve patient outcomes.
PROBLEM TO SOLVE:
The python program should be able to get the image from the user and read it. It should allow the user to draw on the area of interest in the image using a mouse. It should also allow the user to add a description of the area of interest in the form of annotation and save that information in the form of a text file for future reference.
1.	Modules /packages required: Tkinter, Pillow.
2.	Dataflow:
Firstly, the dialogue box will open for the user which will allow the user to specify an x-ray image file to upload. Then the python program will read this image and will display it on the canvas UI widget. After this, the user can draw in the region of interest as the tumor in this case with the help of a mouse, and can also enter the description including the tumor size, shape, location, and diagnosis. The description will be placed inside the label and will be shown around the area of interest which is a tumor. The user will click the save button as provided by the interface to save the image as a png file and an associated text file with the area of interest location and size, and tumor description. This will save the image with the label as a text file and the user can modify that file or image at any period of time and can also use it for future reference.
3.	INPUT: x-ray image.
4.	OUTPUT: a png image file and an associated text file with the circle location and size, and tumor description.
