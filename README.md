
# Pathogen Detection AI

This project is a **Pathogen Detection AI** web application that predicts bacterial types and antibiotic resistance from images using deep learning models. The backend is powered by **Python** with **FastAPI**, and the frontend is built using **HTML**, **CSS**, and **JavaScript**.

The system uses a **ResNet-18** model to predict bacterial types and resistance, taking an image input, processing it through the model, and returning the prediction to the frontend for display.

## Table of Contents

- [Picture of the Program Working](#picture-of-the-program-working)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Backend (FastAPI)](#backend-fastapi)
- [Frontend (HTML, CSS, JavaScript)](#frontend-html-css-javascript)
- [Models Used](#models-used)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Dependencies](#dependencies)
- [License](#license)


## Picture of the Program Working
![image](https://github.com/user-attachments/assets/c8fe33bf-c666-45f0-99aa-c22004beff0f)

## Installation

### 1. Clone the repository:
   To get started, clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/Pathogen_Detection_AI.git
   cd Pathogen_Detection_AI
   ```

### 2. Set up the backend environment:

   The backend is built using **FastAPI** and relies on **PyTorch** for deep learning tasks. To set it up, follow these steps:

   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```

   - **requirements.txt** should include:
     ```txt
     fastapi
     uvicorn
     torch
     torchvision
     Pillow
     numpy
     ```

   **Important**: Make sure to have Python **3.7+** installed on your system. If you have issues with dependencies, consider using a **virtual environment** (e.g., `venv`).

### 3. Set up the frontend environment:

   - The frontend is built using **HTML**, **CSS**, and **JavaScript**. It allows users to upload images and view predictions from the backend.
   
   - Navigate to the `frontend` directory:
     ```bash
     cd frontend
     ```

   - Install frontend dependencies using **npm**:
     ```bash
     npm install
     ```

### 4. Running the FastAPI backend:

   After setting up the backend and frontend, you need to run the backend server.

   - Start the FastAPI server:
     ```bash
     uvicorn main:app --reload
     ```

   - This will start the backend server, which will be accessible at `http://localhost:8000`.

### 5. Running the frontend:

   After setting up the frontend environment, you need to start the frontend server:

   - Run the frontend with:
     ```bash
     npm run start
     ```

   - This will start the frontend on `http://localhost:3000`.

### 6. Open the application:

   After the backend and frontend are running, open your browser and go to `http://localhost:3000` to interact with the web application.


## Project Structure

Here’s a high-level view of the project structure:

```
Pathogen_Detection_AI/
├── backend/                        # Backend folder
│   ├── main.py                     # FastAPI backend
│   ├── models/                     # Pre-trained models folder
│   ├── requirements.txt            # Python dependencies
│   └── utils.py                    # Helper functions (e.g., image preprocessing)
│
├── frontend/                       # Frontend folder
│   ├── index.html                  # Main HTML file
│   ├── app.js                      # JavaScript for interacting with backend
│   ├── style.css                   # Styling for frontend
│   └── package.json                # Frontend dependencies
│
├── .gitignore                      # Gitignore file
└── README.md                       # Project documentation
```


## Backend (FastAPI)

The backend is powered by **FastAPI**, which serves the model and handles incoming requests from the frontend.

### main.py (Backend)
- **FastAPI app** is defined in `main.py`. It handles HTTP requests and loads the ResNet-18 model for bacterial detection.
  
- **Image Uploading and Processing**: The backend allows users to upload an image, which is processed using a pre-trained ResNet-18 model to classify bacterial types.

- **Model Loading**: The `ResNet-18` model is loaded from the `models` directory (where your saved models reside).

- **API Endpoints**:
  - **POST /predict/**: Accepts an image and returns a bacterial classification prediction.

### models/
In this directory, you store the **pre-trained ResNet-18 models** used for bacterial detection and antibiotic resistance prediction.

- **bacteria_detector.pth**: Model trained for detecting bacterial types.
- **resistance_predictor.pth** (optional): Model trained for predicting antibiotic resistance.

- These models should be trained using PyTorch and saved as `.pth` files.

### utils.py (Helper Functions)
This file contains helper functions, such as image preprocessing for the model, that can be reused in the backend logic.


## Frontend (HTML, CSS, JavaScript)

The frontend is responsible for interacting with users, uploading images, and displaying the results.

### index.html
The HTML file serves as the main layout for the page, with:
- An input field for uploading images.
- A button to submit the image.
- A section to display the results of the prediction.

### app.js
This JavaScript file is used for:
- Handling the form submission (sending the image to the backend via a **POST** request).
- Displaying the response from the backend (bacteria type and antibiotic resistance prediction).

### style.css
This file contains basic styling to ensure the frontend is user-friendly and aesthetically clean.


## Models Used

The project uses **ResNet-18**, a Convolutional Neural Network (CNN), which is a pre-trained model for classification tasks. Two models are involved:

1. **Bacteria Detection Model**: Uses the `ResNet-18` architecture to classify bacterial types based on image input.
2. **Antibiotic Resistance Model** (Optional): Predicts antibiotic resistance based on images. This model is not implemented in this current version, but can be added by uncommenting the relevant sections in `main.py`.

## Running the Application

### Backend:

1. **Start the FastAPI backend**:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will be accessible at `http://localhost:8000`.

### Frontend:

2. **Start the frontend**:
   ```bash
   cd frontend
   npm run start
   ```
   The frontend will be accessible at `http://localhost:3000`.

### Accessing the Application:

After both servers are running:
- Visit `http://localhost:3000` on your browser to interact with the web interface.
- Upload an image for bacterial detection, and see the result returned by the model.


## API Endpoints

### POST /predict/
**Description**: Accepts an image and returns the prediction of bacterial type.

- **Request**:  
  - **Method**: POST  
  - **Content-Type**: `multipart/form-data`  
  - **Body**: Upload an image file (JPEG, PNG).

- **Response**:  
  - **Success**:  
    ```json
    {
      "bacteria_type": 1
    }
    ```
  - **Failure**:  
    ```json
    {
      "error": "Error message describing the issue"
    }
    ```


## Dependencies

### Backend Dependencies:
In `requirements.txt`:
- `fastapi`: Web framework for the backend.
- `uvicorn`: ASGI server for serving the FastAPI app.
- `torch`: PyTorch for model handling.
- `torchvision`: For model architecture like ResNet.
- `Pillow`: For image processing.
- `numpy`: For handling array operations.

### Frontend Dependencies:
- `npm` and `Node.js` for JavaScript dependencies.
- **package.json** lists dependencies for frontend components.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
