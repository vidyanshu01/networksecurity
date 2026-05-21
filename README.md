🛡️ Network Security – Phishing Detection System

A Machine Learning–based Network Security application designed to detect phishing activities using structured network data.
The project includes data validation, model training, prediction pipelines, a web interface, and Docker-based deployment support.

📌 Project Overview

Phishing attacks are one of the most common cyber threats in modern networks. This project aims to:

Detect phishing attempts using machine learning techniques

Provide a web-based interface for predictions

Support data ingestion, validation, and prediction pipelines

Enable Dockerized deployment for scalability and portability

🚀 Features

✅ Data ingestion and schema validation

✅ Machine Learning model for phishing detection

✅ Prediction output storage

✅ Web application interface

✅ Docker support for deployment

✅ Modular and scalable project structure

🧠 Technology Stack

Programming Language: Python

Machine Learning: Scikit-learn (model training & prediction)

Web Framework: Flask

Containerization: Docker

Data Handling: Pandas, NumPy

Deployment Ready: AWS / Cloud compatible



 Project Structure
networksecurity/
│
├── networksecurity/        # Core application logic
├── Network_Data/           # Input / raw network data
├── valid_data/             # Validated data
├── data_schema/            # Input data schema
├── final_model/            # Trained ML model
├── Prediction_output/      # Model prediction results
├── templates/              # HTML templates (web UI)
│
├── app.py                  # Main Flask application
├── push_data.py            # Data ingestion script
├── requirements.txt        # Project dependencies
├── setup.py                # Package configuration
├── Dockerfile              # Docker configuration
├── README.md               # Project documentation
└── .gitignore





⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/vidyanshu01/networksecurity.git
cd networksecurity

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Application
Run the Flask App
python app.py


Then open your browser and go to:

http://localhost:5000

🐳 Docker Deployment
Build Docker Image
docker build -t network-security-app .

Run Docker Container
docker run -p 5000:5000 network-security-app

📊 Machine Learning Workflow

Data Collection

Schema Validation

Data Preprocessing

Model Training

Model Evaluation

Prediction Generation

Web-based Result Display

🧪 Input & Output

Input: Structured network / phishing dataset

Output:

Prediction_output/ → Stores predicted results

Classification label indicating phishing or legitimate traffic

🔐 Security Considerations

Input data is validated using predefined schemas

Designed to prevent malformed data injection

Containerized environment improves isolation

📈 Future Enhancements

🔹 Add authentication to the web app

🔹 Improve model accuracy using advanced ML algorithms

🔹 Real-time network traffic integration

🔹 CI/CD pipeline integration

🔹 Detailed performance metrics and dashboards

👨‍🎓 Author

Vidyanshu Kushawaha
B.Tech – Computer Science & Engineering
GitHub: vidyanshu01

📜 License

This project is intended for educational and research purposes.
You are free to modify and extend it for learning.
