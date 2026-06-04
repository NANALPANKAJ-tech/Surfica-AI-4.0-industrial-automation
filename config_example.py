# ==========================================

# SURFICA-AI 4.0 Configuration File

# ==========================================

# -------------------------------

# Camera Configuration

# -------------------------------

CAMERA_INDEX = 0

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480

# -------------------------------

# CNN Model

# -------------------------------

CNN_MODEL_PATH = "models/cnn_defect_model.keras"

DEFECT_CONFIDENCE_THRESHOLD = 0.80

# -------------------------------

# YOLO Model

# -------------------------------

YOLO_MODEL_PATH = "models/surfica_yolo.pt"

YOLO_CONFIDENCE_THRESHOLD = 0.50

# -------------------------------

# LSTM Predictive Maintenance

# -------------------------------

LSTM_MODEL_PATH = "models/surfica_lstm_model.keras"

HEALTH_ALERT_THRESHOLD = 20

# -------------------------------

# Database

# -------------------------------

DATABASE_PATH = "surfica.db"

# -------------------------------

# PLC / Modbus Configuration

# -------------------------------

PLC_IP = "192.168.1.100"
PLC_PORT = 502

PLC_ENABLED = False

# Example Registers

TEMPERATURE_REGISTER = 100
PRESSURE_REGISTER = 101
LINE_SPEED_REGISTER = 102
VIBRATION_REGISTER = 103

# -------------------------------

# Dashboard

# -------------------------------

REFRESH_INTERVAL_SECONDS = 5

# -------------------------------

# Alert Settings

# -------------------------------

EMAIL_ALERTS = False

EMAIL_FROM = "[your_email@gmail.com](mailto:your_email@gmail.com)"
EMAIL_PASSWORD = "your_app_password"

EMAIL_TO = "[manager@company.com](mailto:manager@company.com)"

# -------------------------------

# Logging

# -------------------------------

LOG_LEVEL = "INFO"

# -------------------------------

# Production Settings

# -------------------------------

PLANT_NAME = "SURFICA Laminate Plant"

AUTO_REJECT_DEFECTS = False
AUTO_STOP_MACHINE = False

# -------------------------------

# Simulation Mode

# -------------------------------

SIMULATION_MODE = True
