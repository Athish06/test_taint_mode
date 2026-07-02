from managers import (
    manage_user_query, 
    process_warehouse_notification, 
    dispatch_payment, 
    execute_system_task,
    handle_user_deletion,
    apply_user_updates,
    load_file_content,
    dispatch_webhook,
    dispatch_complex_task
)
from core_sinks import render_core
from repositories import save_order

def service_user_query(query: str):
    # Vuln 1: 7-Layer SQLi
    manage_user_query(query)

def service_process_checkout(order_id: str):
    # Vuln 2: Multi-Sink Fan-Out
    # Branch 1: SSRF
    process_warehouse_notification(order_id)
    # Branch 2: SQLi
    save_order(order_id)

def service_process_payment(safe_amount: str, unsafe_amount: str):
    # Vuln 3: Parameter Swap
    # Note how safe_amount is ignored, and unsafe_amount is passed to the dispatcher
    dispatch_payment(unsafe_amount)

def service_run_task(command: str):
    # Vuln 4: Fake Sanitizer
    execute_system_task(command)

def service_delete_user(user_id: str):
    # Vuln 5: Missing Auth IDOR Cascade
    handle_user_deletion(user_id)

def service_update_profile(**kwargs):
    # Vuln 6: Mass Assignment
    apply_user_updates(**kwargs)

def service_generate_invoice(email_body: str):
    # Vuln 7: SSTI
    # Render is done directly here for variation
    render_core.render_html(email_body)

def service_read_upload(filename: str):
    # Vuln 8: Path Traversal
    return load_file_content(filename)

def service_trigger_webhook(url: str):
    # Vuln 9: Blind SSRF
    dispatch_webhook(url)

def service_complex_op(a, b, c, d, e):
    # Vuln 10: Taint Dilution
    dispatch_complex_task(a, b, c, d, e)
