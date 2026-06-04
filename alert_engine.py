# alert_engine.py
# SURFICA-AI 4.0 Alert Engine

def evaluate_alerts(data):
    """
    Evaluate machine data and return structured alert information.
    Includes rolling defect count tracking for quality alerts.
    """
    alerts = []

    # Safe extraction with defaults
    temperature = float(data.get("temperature") or 0)
    pressure = float(data.get("pressure") or 0)
    vibration = float(data.get("vibration") or 0)
    line_speed = float(data.get("line_speed") or 0)
    
    # Defect logic: use explicit count if available, else boolean
    defect_count = int(data.get("defect_count") or 0)
    defect_detected = bool(data.get("defect_detected", False))
    
    # If no count provided but defect detected, treat as single defect event
    effective_defect_count = defect_count if defect_count > 0 else (1 if defect_detected else 0)

    # Temperature checks (aligned with config.py thresholds)
    if temperature >= 200:
        alerts.append("CRITICAL: Temperature above 200°C")
    elif temperature >= 185:
        alerts.append("WARNING: Temperature near limit")

    # Pressure check
    if pressure >= 100:
        alerts.append("WARNING: High pressure detected")

    # Vibration check
    if vibration >= 8:
        alerts.append("WARNING: High vibration detected")

    # Quality check — uses effective defect count
    if effective_defect_count >= 5:
        alerts.append("QUALITY ALERT: Multiple defects detected")
    elif effective_defect_count >= 1:
        alerts.append("INFO: Defect detected in current cycle")

    # Line status check
    if line_speed <= 0:
        alerts.append("LINE ALERT: Production line stopped")

    # Determine alert level based on highest severity
    if any("CRITICAL" in alert for alert in alerts):
        alert_level = "CRITICAL"
    elif any("QUALITY ALERT" in alert or "WARNING" in alert or "LINE ALERT" in alert for alert in alerts):
        alert_level = "WARNING"
    elif any("INFO" in alert for alert in alerts):
        alert_level = "INFO"
    else:
        alert_level = "NORMAL"

    # Build combined message
    if alerts:
        alert_message = " | ".join(alerts)
    else:
        alert_message = "Machine condition normal."

    return {
        "alerts": alerts,
        "alert_level": alert_level,
        "alert_message": alert_message,
        "effective_defect_count": effective_defect_count,
    }
