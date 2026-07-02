from repositories import execute_user_query, save_order, remove_user_record, update_user_record, complex_query_builder
from core_sinks import net_core, sys_core, payment_core
from utils import build_path

def manage_user_query(query: str):
    # Vuln 1: 7-Layer SQLi
    execute_user_query(query)

def process_warehouse_notification(order_id: str):
    # Vuln 2: Multi-Sink Fan-Out (SSRF branch)
    net_core.fetch_url(f"http://warehouse-api/notify?order={order_id}")

def dispatch_payment(amount: str):
    # Vuln 3: Parameter Swap
    payment_core.process_transaction(amount)

def execute_system_task(command: str):
    # Vuln 4: Fake Sanitizer
    sys_core.run_cmd(command)

def handle_user_deletion(user_id: str):
    # Vuln 5: Missing Auth IDOR Cascade
    remove_user_record(user_id)

def apply_user_updates(**kwargs):
    # Vuln 6: Mass Assignment
    update_user_record(**kwargs)
    
def load_file_content(filename: str):
    # Vuln 8: Path Traversal
    full_path = build_path("/var/www/uploads", filename)
    return sys_core.read_file(full_path)

def dispatch_webhook(url: str):
    # Vuln 9: Blind SSRF
    net_core.fetch_url(url)

def dispatch_complex_task(a, b, c, d, e):
    # Vuln 10: Taint Dilution
    complex_query_builder(a, b, c, d, e)
