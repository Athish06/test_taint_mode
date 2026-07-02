from fastapi import FastAPI, Request
from controllers import (
    controller_search_users,
    controller_checkout,
    controller_pay,
    controller_system_task,
    controller_remove_user,
    controller_edit_profile,
    controller_invoice,
    controller_download,
    controller_webhook,
    controller_complex
)
from utils import fake_sanitize, extract_kwargs

app = FastAPI()

# Vuln 1: The 7-Layer SQLi
@app.get("/search")
def search_users(q: str):
    controller_search_users(q)

# Vuln 2: The Multi-Sink Fan-Out (SSRF + SQLi)
@app.post("/checkout")
def checkout(order_id: str):
    controller_checkout(order_id)

# Vuln 3: The Parameter Swap Trap
@app.post("/pay")
def pay(safe_val: str, unsafe_val: str):
    # Passes safe_val and unsafe_val. The controller swaps them!
    controller_pay(safe_val, unsafe_val)

# Vuln 4: The Fake Sanitizer
@app.post("/run_task")
def run_task(cmd: str):
    # Passes through the fake sanitizer
    sanitized = fake_sanitize(cmd)
    controller_system_task(sanitized)

# Vuln 5: The Missing Auth IDOR Cascade
@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    # No @auth_required decorator here!
    controller_remove_user(user_id)

# Vuln 6: The Mass Assignment Deep Dive
@app.put("/profile")
async def update_profile(request: Request):
    payload = await request.json()
    kwargs = extract_kwargs(payload)
    controller_edit_profile(**kwargs)

# Vuln 7: The Server-Side Template Injection (SSTI)
@app.post("/invoice")
def generate_invoice(email_body: str):
    controller_invoice(email_body)

# Vuln 8: The Path Traversal
@app.get("/download")
def download_file(filename: str):
    return controller_download(filename)

# Vuln 9: The Blind SSRF (Webhooks)
@app.post("/webhook")
def register_webhook(url: str):
    controller_webhook(url)

# Vuln 10: The Overloaded Function (Taint Dilution)
@app.get("/complex")
def complex_route(target: str):
    # Passes 'target' as the 4th argument
    controller_complex("safe1", "safe2", "safe3", target, "safe5")
