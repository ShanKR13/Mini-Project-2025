# Deep Learning Based Automatic Music Transcription using CR-GCN
# Overview
This project implements an enhanced Channel Relationship-Based Graph Convolutional Network (CR-GCN) for Automatic Music Transcription (AMT) of polyphonic piano recordings. The model combines Convolutional Neural Networks (CNNs) for spatial feature extraction, Bidirectional Long Short-Term Memory (BiLSTM) for temporal modeling, and Graph Convolutional Networks (GCNs) to capture note interdependencies. Trained and evaluated on the MAESTRO v2.0.0 dataset, the model achieves a frame-level F1-score of 0.8588, demonstrating competitive performance in transcribing complex polyphonic music into MIDI files and generating music sheets.
The project includes a web application built with Django, allowing users to upload .wav audio files and receive corresponding music sheets. The transcription pipeline leverages music21 and LilyPond for sheet music generation, with preprocessing and feature extraction optimized for real-time applications.
## Features

Hybrid Deep Learning Model: Integrates CNN, BiLSTM, and GCN for robust AMT.
Data Preprocessing: Processes MAESTRO dataset audio and MIDI files into PyTorch-compatible formats.
Web Application: Django-based interface for uploading audio files and viewing generated music sheets.
Real-Time Transcription: Try it yourself with our Jupyter notebook for real-time AMT.

## Architecture 
![image](https://github.com/user-attachments/assets/acea78ac-900c-4903-94f1-92db87e11557)
# Website
![image](https://github.com/user-attachments/assets/dc546cfd-4659-45c1-bd9e-5c150a727471)
# Sample Screenshots of Try it Yourself !
![image](https://github.com/user-attachments/assets/cc1a7da1-c1b2-4a0d-b934-42b286a98b4f)
![image](https://github.com/user-attachments/assets/a43cbdf2-29ca-4fc9-be1a-8dc87bb6c7a7)




## Installation
To set up the project locally, follow these steps:

Clone the Repository:
git clone https://github.com/SelvaKarthik01/AMT_using_CR_GCN.git
cd AMT_using_CR_GCN


Install Dependencies:Ensure Python 3.8+ is installed, then install required packages:
pip install -r requirements.txt

Required libraries include torch, librosa, mido, music21, django, and numpy. Install LilyPond for sheet music generation:

Download and install LilyPond.
Update the lilypondPath in Try_it_Yourself/AMT_using_CR_GCN_Final_Real_Time.ipynb to your LilyPond executable path.


Download MAESTRO Dataset:Download the MAESTRO v2.0.0 dataset is the one that we used if you want to retrain


## Usage

Preprocessing:Run the preprocessing script to prepare the MAESTRO dataset:
python preprocess_maestro.py

This generates .pt and .tsv files in the dataset directory.

Training the Model:Train the CR-GCN model using:
python train_model.py

The model uses an Adam optimizer with exponential decay and trains for 100 epochs.

Running the Web Application:Start the Django server:
python manage.py runserver

Access the application at http://localhost:8000 and upload .wav files to generate music sheets.

You can check through this in detail inside the 2nd Review Training codes Folder under data-preprocessing-and-visualization.ipynb and amt-using-cr-gcn-f1-score-85-highest.ipynb for training details.

Try It Yourself!:To experience real-time transcription, navigate to the Try_it_Yourself folder and open the AMT_using_CR_GCN_Final_Real_Time.ipynb notebook in Google Colab:

Upload a .wav file and run the notebook to generate MIDI files and music sheets.
Important: This notebook is optimized for Google Colab to leverage its computational resources and dependencies. Ensure you have a Google account and access to Colab.



# Try It Yourself!
Want to transcribe your own audio? Check out the Try_it_Yourself folder in this repository! We’ve provided a Jupyter notebook, AMT_using_CR_GCN_Final_Real_Time.ipynb, that allows you to upload a .wav file and generate its music sheet in real time. For the best experience, run this notebook in Google Colab to ensure all dependencies (e.g., music21, LilyPond) work seamlessly. Follow the instructions in the notebook to upload your audio and visualize the transcribed music sheet.
Base Paper Reference
This project builds upon the work in:

Xiao, Z., Chen, X., & Zhou, L. (2023). Polyphonic Piano Transcription Based on Graph Convolutional Network. Signal Processing, 212, 109134. ISSN: 0165-1684.

## Results

Frame-Level F1-Score: 0.8588
Note-Level Onset F1-Score: 0.8508
Note with Offset F1-Score: 0.8510The model outperforms several baselines (e.g., Onsets and Frames: 0.7894) but falls short of the original CR-GCN (0.9277), indicating room for improvement in handling complex polyphonic structures.

## Future Work

Integrate attention mechanisms in GCN for better note interdependency modeling.
Enhance generalization with data augmentation (e.g., synthetic noise injection).
Implement bidirectional data exchange in the web application for seamless MIDI and sheet music delivery.

## Acknowledgments
We thank SASTRA Deemed to be University, our guide Dr. Emily Jenifer A, and the MAESTRO dataset creators for their support and resources.
## Team Members :
Selva Karthik S
Shantosh Kumar R
Rithvik L

## License
This project is licensed under the MIT License. See the LICENSE file for details.
