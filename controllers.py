from services import (
    service_user_query,
    service_process_checkout,
    service_process_payment,
    service_run_task,
    service_delete_user,
    service_update_profile,
    service_generate_invoice,
    service_read_upload,
    service_trigger_webhook,
    service_complex_op
)

def controller_search_users(query: str):
    # Vuln 1: 7-Layer SQLi
    service_user_query(query)

def controller_checkout(order_id: str):
    # Vuln 2: Multi-Sink Fan-Out
    service_process_checkout(order_id)

def controller_pay(unsafe_val: str, safe_val: str):
    # Vuln 3: Parameter Swap
    # Note how the order is swapped here before passing to the service
    service_process_payment(safe_val, unsafe_val)

def controller_system_task(command: str):
    # Vuln 4: Fake Sanitizer
    service_run_task(command)

def controller_remove_user(user_id: str):
    # Vuln 5: Missing Auth IDOR Cascade
    service_delete_user(user_id)

def controller_edit_profile(**kwargs):
    # Vuln 6: Mass Assignment
    service_update_profile(**kwargs)

def controller_invoice(email_body: str):
    # Vuln 7: SSTI
    service_generate_invoice(email_body)

def controller_download(filename: str):
    # Vuln 8: Path Traversal
    return service_read_upload(filename)

def controller_webhook(url: str):
    # Vuln 9: Blind SSRF
    service_trigger_webhook(url)

def controller_complex(a, b, c, d, e):
    # Vuln 10: Taint Dilution
    service_complex_op(a, b, c, d, e)
