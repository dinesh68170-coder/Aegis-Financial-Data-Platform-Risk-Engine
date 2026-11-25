"""
Aegis — Financial Infrastructure & AI Risk Engine Launcher
Root entrypoint for Visual Studio and VS Code.
"""

import sys
import os

# Ensure local workspace is in python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from aegis.aegis_app import seed_demo_environment
from aegis.api.server import create_aegis_server
from aegis.tests.run_all import run_aegis_test_suite

def main():
    print("=" * 80)
    print(" AEGIS — FINANCIAL INFRASTRUCTURE & AI RISK ENGINE")
    print("=" * 80)
    print("Choose an action:")
    print(" [1] Run Automated Test Suite (17 Acceptance Tests)")
    print(" [2] Run Demonstration Workflow (Transfers + Risk + Recon)")
    print(" [3] Launch Interactive Web UI Server (http://localhost:8080)")
    print("=" * 80)

    choice = input("Enter choice (1, 2, or 3) [Default: 2]: ").strip() or "2"

    if choice == "1":
        run_aegis_test_suite()
    elif choice == "3":
        print("\nStarting Aegis Web Dashboard at http://localhost:8080 ...")
        server = create_aegis_server("aegis_live.db", port=8080)
        print("Server running! Open http://localhost:8080 in your browser.")
        print("Press Ctrl+C to stop.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
    else:
        seed_demo_environment("aegis_live.db")
        print("\nDemo finished successfully! You can also run choice 3 to launch the dashboard.")

if __name__ == "__main__":
    main()
