# MNIST Digit Classifier

A web application that uses machine learning to recognize handwritten digits. The system consists of a RandomForest classifier trained on the MNIST dataset, served through a FastAPI backend with a simple HTML/JavaScript frontend.

## Features

- Real-time digit classification
- Simple and intuitive web interface
- RESTful API endpoint for predictions
- Support for image upload and preview
- Fast response time

## Technical Stack

- **Backend:**
  - Python 3.12
  - FastAPI
  - scikit-learn (RandomForestClassifier)
  - Pillow for image processing
  - uvicorn server

- **Frontend:**
  - HTML5
  - CSS3
  - Vanilla JavaScript

## Installation

1. Clone the repository:
```bash
git clone https://github.com/itspranaw/detectnum-fastapi.git
cd mnist-classifier
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Training the Model

Run the training script to generate the model:
```bash
python train_model.py
```

This will:
- Download the MNIST dataset
- Train a RandomForestClassifier
- Save the model as 'mnist_model.pkl'

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. Open `index.html` in your web browser

The application will be available at `http://localhost:8000`

## API Endpoints

- GET `/`: Health check endpoint
- POST `/predict-image`: Accepts image file and returns predicted digit
  - Request: multipart/form-data with 'file' field
  - Response: JSON with 'prediction' field

## Project Structure

```
mnist-classifier/
├── main.py             # FastAPI application
├── train_model.py      # Model training script
├── mnist_model.pkl     # Trained model (generated)
├── index.html         # Frontend interface
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Usage

1. Open the web interface
2. Upload an image of a handwritten digit
3. Click "Predict Digit"
4. View the predicted number

## Model Performance

The RandomForestClassifier achieves approximately 96-97% accuracy on the test set.

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Requirements

See `requirements.txt` for a complete list of dependencies. Main requirements:

- Python 3.12+
- FastAPI
- scikit-learn
- Pillow
- uvicorn
- numpy

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

@itspranaw
