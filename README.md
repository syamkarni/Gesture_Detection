# Gesture Detection Project

## Description
This project implements a gesture detection system using OpenCV and MediaPipe. It processes a given input image and a video stream to detect specific gestures. The system uses pose estimation algorithms provided by MediaPipe to detect and track human poses in real-time.

## Algorithms Used
- **Pose Estimation**: Utilizes MediaPipe's pose estimation capabilities to detect human poses in images and video streams.
- **Similarity Function**: Implements a custom similarity function to compare keypoints of the detected pose against a reference pose. This function calculates the average Euclidean distance between corresponding keypoints.

## Evaluation of Similarity Function
The similarity function is crucial for determining the resemblance between the reference gesture and detected poses. It effectively calculates the average Euclidean distance, providing a straightforward and computationally efficient approach to gesture comparison. However, its performance may vary based on the complexity of gestures and the quality of pose detection. Fine-tuning the threshold value and experimenting with different sets of keypoints can optimize detection accuracy.

## Setup and Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Setting Up a Virtual Environment
It's recommended to set up a virtual environment for Python projects to manage dependencies. Here's how to do it:

1. **Create a Virtual Environment:**
   ```bash
   python3 -m venv myenv
   ```

2. **Activate the Virtual Environment:**

   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source myenv/bin/activate
     ```

### Installing Dependencies
Install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running the Program

1. Place your input image (e.g., `test.jpg`) and video file (e.g., `video.mp4`) in the project directory.

2. Run the main script:
   ```bash
   python det_video.py
   ```

3. The program will process the video stream and display detected gestures in real-time.

## Project Structure

- `main.py`: Contains the main pose detection functions using MediaPipe.
- `gesture_sim.py`: Implements the similarity function for comparing gestures.
- `video_annotat.py`: Handles the annotation of detected gestures on the video frames.
- `det_video.py`: The main driver script that integrates all components.

## Notes
- Ensure that the versions of Python, OpenCV, and MediaPipe in your `requirements.txt` are compatible.
- Adjust the threshold value in `det_video.py` as needed for optimal gesture detection sensitivity.