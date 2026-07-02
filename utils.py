# utils.py

def fake_sanitize(input_str: str) -> str:
    # Vuln 4: Fake Sanitizer (Only strips whitespace, doesn't sanitize shell characters)
    return input_str.strip()

def build_path(base_dir: str, filename: str) -> str:
    # Vuln 8: Path Traversal helper
    return f"{base_dir}/{filename}"

def extract_kwargs(payload_dict: dict) -> dict:
    # Vuln 6: Mass Assignment helper
    return payload_dict
