import sqlite3
import subprocess
import requests
import os

class DatabaseCore:
    def raw_execute(self, query: str):
        # Sink for Vuln 1 (SQLi), Vuln 2 (SQLi Fan-Out), Vuln 6 (Mass Assignment), Vuln 10 (Dilution)
        conn = sqlite3.connect(':memory:')
        conn.execute(query)

class SystemCore:
    def run_cmd(self, command: str):
        # Sink for Vuln 4 (Fake Sanitizer)
        subprocess.run(command, shell=True)
        
    def read_file(self, filepath: str):
        # Sink for Vuln 8 (Path Traversal)
        with open(filepath, 'r') as f:
            return f.read()

class NetworkCore:
    def fetch_url(self, url: str):
        # Sink for Vuln 2 (SSRF Fan-Out), Vuln 9 (Blind SSRF)
        requests.get(url)

class RenderCore:
    def render_html(self, template_str: str):
        # Sink for Vuln 7 (SSTI)
        # Using a mock render to simulate SSTI
        pass

class AuthCore:
    def delete_record(self, record_id: str):
        # Sink for Vuln 5 (IDOR Cascade)
        # Assumes missing auth checks
        pass

class PaymentCore:
    def process_transaction(self, amount: str):
        # Sink for Vuln 3 (Parameter Swap)
        subprocess.run(f"process_payment {amount}", shell=True)

db_core = DatabaseCore()
sys_core = SystemCore()
net_core = NetworkCore()
render_core = RenderCore()
auth_core = AuthCore()
payment_core = PaymentCore()
