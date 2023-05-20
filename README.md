
# Face Mask Detection Based Door Lock System

This project aims to detect whether a person is wearing a face mask or not using computer vision techniques and a convolutional neural network (CNN) model. If the person is wearing a face mask, the system will automatically open the door to allow entry. However, if the person is not wearing a face mask, the system will deny access and activate an alarm.

## Project Overview
The Face-Mask-Detection-Based-Door Lock System operates in two main steps: face mask detection and door control. It utilizes the VGG19 CNN model for face mask classification and OpenCV for real-time face localization using a webcam. Additionally, an Arduino microcontroller is employed to control the door and sound the alarm.

## System Flow

**Face Mask Detection:** In this step, VGG19 model is used , a pre-trained CNN architecture, to classify whether a person is wearing a face mask or not. The model is trained on a dataset of images containing individuals with and without face masks. The training process involves optimizing the model's parameters over 19 epochs to achieve accurate predictions.

**Face Localization**: OpenCV, a popular computer vision library, is employed to detect and localize faces in real-time using a webcam. This part of the system helps isolate the region of interest (ROI) for face mask detection.

**Door Control and Alarm:** An Arduino microcontroller is utilized to interface with the door and alarm system. A servo motor is connected to control the door's opening and closing, while a buzzer is used to generate an audible alarm. The Arduino receives signals from the face mask detection system to determine whether to open the door or activate the alarm.

## Prerequisites
To run this project, ensure that you have the following prerequisites installed:

Python 3.x: https://www.python.org/downloads/ \
OpenCV: pip install opencv-python\
TensorFlow: pip install tensorflow\
Arduino IDE: https://www.arduino.cc/en/software \
Required libraries for Arduino: Servo and Tone\
PySerial: pip install pyserial





## Installation

Getting Started
To set up the project on your local machine, follow these steps:

1. Clone the repository:

```bash
  git clone https://github.com/Taha533/Face-Mask-Detection-Based-Door-lock-System.git
```
2. Change into the project directory:

```bash
  cd Face-Mask-Detection-Based-Door-Lock-System
```
3. Upload the Arduino code to your Arduino board:
Open arduino_code.ino in the Arduino IDE. Connect your Arduino board to your computer using a USB cable. Click the "Upload" button in the Arduino IDE to flash the code onto the board.

4. Install the required Python dependencies:
    
```bash
  pip install -r requirements.txt
```
5. Just to classify face mask:

```bash
  python Mask_Detection.py
```
6. To run the whole system, with Arduino:
```bash
  python Face_Mask_Detection_with_arduino.py
```

## Configuration


**WEBCAM_INDEX:** The index of the webcam device to be used. If you only have one webcam, the default value of 0 should work. Otherwise, you may need to adjust this value accordingly.

### For Arduino code:
**SERVO_PIN:** Set the Arduino pin number that is connected to the servo motor controlling the door.\
**BUZZER_PIN:** Set the Arduino pin number that is connected to the buzzer for the alarm system.\
**DOOR_OPEN_ANGLE:** The angle at which the servo motor should rotate to open the door.\
**DOOR_CLOSED_ANGLE:** The angle at which the servo motor should rotate to close the door.\
Feel free to modify these configuration options based on your setup and hardware connections.

## Usage
1. Connect your Arduino board to the computer and ensure it is recognized by the system.
2. Run the "Face Mask Detection with arduino.py" script using the following command:

```bash
  python Face_Mask_Detection_with_arduino.py
```
3. The script will initiate the webcam and start the face mask detection system. It will display the live video feed with bounding boxes around detected faces and corresponding labels indicating if a face mask is detected or not.
4. When a person with a face mask approaches the camera, the system will open the door automatically, granting access.
5. If a person is detected without a face mask, the system will activate the alarm by sounding the buzzer and deny access by keeping the door closed.
6. Press the Esc key to quit the application and stop the system.

## Sample Images:

1. Buzzer Connection:

![Buzzer Connection](https://github.com/Taha533/Face-Mask-Detection-Based-Door-lock-System/blob/main/buzzer_conn.jpg?raw=true)

2. Servo Motor Connection:

![Motor Connection](https://github.com/Taha533/Face-Mask-Detection-Based-Door-lock-System/blob/main/servo_motor_conn.jpg?raw=true)

3. Project Demonstration:

![Project Demonstration](https://github.com/Taha533/Face-Mask-Detection-Based-Door-lock-System/blob/main/project_demonstration.jpg?raw=true)

## Contributing
Contributions to the Face-Mask-Detection-Based-Door Lock System project are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request. Additionally, you can open issues to report any problems or provide suggestions.

## License
The Face-Mask-Detection-Based-Door Lock System project is licensed under the [MIT License](https://github.com/Taha533/Face-Mask-Detection-Based-Door-lock-System/blob/main/LICENSE).


## Acknowledgments
This project was inspired by the need for enhanced safety measures during the COVID-19 pandemic. It combines computer vision techniques, machine learning, and microcontroller programming to create an automated door lock system with face mask detection.

Special thanks to the following resources:

VGG19 Model: https://arxiv.org/abs/1409.1556 \
OpenCV Library: https://opencv.org/ \
Arduino: https://www.arduino.cc/

## Contact
For any questions, concerns, or inquiries, please contact taha15@cse.pstu.ac.bd 

Thank you for using the Face-Mask-Detection-Based-Door Lock System! I hope it proves to be a valuable contribution to your security needs.


