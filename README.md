# Chronic Kidney Disease Prediction Web Application

This project is a web-based application designed to predict the likelihood of Chronic Kidney Disease (CKD) based on various patient parameters. It provides a user-friendly interface for inputting medical data and visualizes the prediction results, including probabilities, using a modern and responsive design.
## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contact](#contact)

## Features
- **Intuitive Data Input**: A comprehensive form allows users to enter 24 different medical parameters.
- **Real-time Prediction**: Submits data to a Flask backend for immediate prediction.
- **Visualized Probabilities**: Displays prediction outcomes (CKD Detected / No CKD) with a dynamic pie chart showing the probability distribution.
- **Responsive Design**: Optimized for seamless viewing and interaction across various devices.
- **Enhanced Styling**: Modern UI with a relevant background image, subtle hover effects, and clear visual feedback for results.
- **Error Handling**: Provides user-friendly messages for network errors or unexpected server responses.
## Technologies Used

**Backend:**
- Python
- Flask
- Scikit-learn 
- Pandas 

**Frontend:**
- HTML5
- CSS3
- JavaScript 
- Chart.js

## Project Structure

```
chronic-kidney-disease-prediction/
│
├── app.py                   # Main Flask backend script
├── requirements.txt         # Required Python packages
├── README.md                # Project documentation
│
├── static/                  # Static assets
│   ├── style.css            # CSS styles for the frontend
│   ├── script.js            # JavaScript for interactivity
│   └── background.jpg       # Optional background image
│
├── templates/               # HTML templates
│   └── index.html           # Main user interface
│
├── model/                   # (Optional) Trained ML model
│   └── ckd_model.pkl        # Trained model file
│
└── utils/                   # (Optional) Utility functions
    └── preprocess.py        # Preprocessing logic
```
 # Data preprocessing before prediction
## Setup and Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/FARDeen9307/chronic-kidney-disease-prediction.git
   cd chronic-kidney-disease-prediction
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

   On Windows:
   ```bash
   .\venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   _If `requirements.txt` is missing, install manually:_
   ```bash
   pip install Flask scikit-learn pandas
   ```

4. **Add background image (optional):**
   Save an image as `background.jpg` inside the `static/` folder.

5. **Run the application:**
   ```bash
   flask run
   ```
   or
   ```bash
   python app.py
   ```

   Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage
- Open the web browser and visit [http://localhost:5000](http://localhost:5000)
- Fill the form with 24 medical parameters.
- Click "Predict".
- View result and probability pie chart.

## Future Enhancements
- Model retraining/update mechanism
- User login and history tracking
- Field explanation tooltips
- Enhanced confidence score display
- Additional visualizations
- Robust input validation
- Docker containerization
- Database integration

## Contact
**Fardeen Khan**  
GitHub: [FARDeen9307](https://github.com/FARDeen9307)




