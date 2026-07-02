from core_sinks import db_core, auth_core

# Repositories layer interacts directly with core sinks

def execute_user_query(query: str):
    # Vuln 1: 7-Layer SQLi
    db_core.raw_execute(query)

def save_order(order_data: str):
    # Vuln 2: Multi-Sink Fan-Out (SQLi branch)
    db_core.raw_execute(f"INSERT INTO orders VALUES ('{order_data}')")

def remove_user_record(user_id: str):
    # Vuln 5: Missing Auth IDOR Cascade
    auth_core.delete_record(user_id)

def update_user_record(**kwargs):
    # Vuln 6: Mass Assignment Deep Dive
    # Constructing a dynamic query from kwargs
    set_clause = ", ".join([f"{k}='{v}'" for k, v in kwargs.items()])
    db_core.raw_execute(f"UPDATE users SET {set_clause}")

def complex_query_builder(arg1, arg2, arg3, arg4, arg5):
    # Vuln 10: Taint Dilution. arg4 is the tainted one.
    db_core.raw_execute(f"SELECT * FROM table WHERE col='{arg4}'")
