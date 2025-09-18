def ocpi_response(data, status_code=1000, status_message="Success"):
    """
    Wraps the response in OCPI format.
    """
    return {
        "data": data,
        "status_code": status_code,
        "status_message": status_message,
        "timestamp": None  # Optionally add a timestamp if needed
    }
