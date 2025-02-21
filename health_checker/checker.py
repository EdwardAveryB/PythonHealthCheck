import asyncio
import os
import aiohttp
import yaml
import argparse
import logging
import time
import csv
import json
from collections import defaultdict
from typing import Dict, List
from rich.console import Console
from rich.logging import RichHandler

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Define log file path
LOG_FILE = os.path.join(LOG_DIR, "health_checker.log")

# Configure logging to both console and log file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        RichHandler(markup=True),  # Colorized console output
        logging.FileHandler(LOG_FILE)  # Save logs to logs/health_checker.log
    ],
)

console = Console()

class HealthChecker:
    def __init__(self, config_path: str, interval: int = 15):
        self.config_path = config_path
        self.interval = interval
        self.endpoints = self.load_yaml()
        self.domain_stats = defaultdict(lambda: {'total': 0, 'up': 0})
        self.results = []  # Store health check data for reports
    
    def load_yaml(self) -> List[Dict]:
        """Load the endpoints from the YAML configuration file."""
        with open(self.config_path, "r") as file:
            return yaml.safe_load(file)


    def save_reports(self):
        """Append collected health check results to CSV & JSON for long-term tracking."""
        os.makedirs("logs", exist_ok=True)  # Ensure logs directory exists

        # Append to CSV file
        csv_file = "logs/availability_report.csv"
        file_exists = os.path.isfile(csv_file)
        
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["timestamp", "domain", "endpoint", "status", "latency"])
            if not file_exists:
                writer.writeheader()  # Write headers only if the file is new
            writer.writerows(self.results)

        # Append to JSON file
        json_file = "logs/availability_report.json"
        if os.path.isfile(json_file):
            with open(json_file, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        existing_data.extend(self.results)

        with open(json_file, "w") as file:
            json.dump(existing_data, file, indent=4)

        logging.info("[cyan]Updated reports in logs/availability_report.csv and logs/availability_report.json[/cyan]")

    async def check_endpoint(self, session: aiohttp.ClientSession, endpoint: Dict):
        """Perform a health check on a single endpoint and store results."""
        url = endpoint.get("url")
        name = endpoint.get("name", "Unknown Endpoint")
        method = endpoint.get("method", "GET").upper()
        headers = endpoint.get("headers", {})
        body = endpoint.get("body", None)
        domain = url.split("/")[2]  # Extract domain from URL

        latency = None
        status = "DOWN"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        start_time = time.time()
        try:
            async with session.request(method, url, headers=headers, json=body) as response:
                latency = (time.time() - start_time) * 1000  # Convert to ms
                if 200 <= response.status < 300 and latency < 500:
                    status = "UP"
        except Exception as e:
            logging.warning(f"[bold yellow]{name} ({url}) failed with error:[/bold yellow] {e}")

        # Store result for reporting
        self.results.append({
            "timestamp": timestamp,
            "domain": domain,
            "endpoint": name,
            "status": status,
            "latency": f"{latency:.2f}ms" if latency is not None else "N/A",
        })

        # Track domain stats
        self.domain_stats[domain]['total'] += 1
        if status == "UP":
            self.domain_stats[domain]['up'] += 1

        latency_display = f"{latency:.2f}ms" if latency is not None else "N/A"
        log_color = "[green]" if status == "UP" else "[red]"
        logging.info(f"{log_color}{name} ({url}) - Status: {status} - Latency: {latency_display}[/]")

    def update_availability_trends(self):
        """Track and log long-term availability trends across multiple runs."""
        trends_file = "logs/availability_trends.csv"
        file_exists = os.path.isfile(trends_file)

        with open(trends_file, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["timestamp", "domain", "availability"])
            if not file_exists:
                writer.writeheader()

            for domain, stats in self.domain_stats.items():
                availability = (stats["up"] / stats["total"]) * 100
                writer.writerow({"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), "domain": domain, "availability": f"{availability:.2f}"})

        logging.info("[magenta]Updated long-term availability trends in logs/availability_trends.csv[/magenta]")


    async def run_health_checks(self):
        """Continuously check endpoints, log availability, save reports, and track trends."""
        async with aiohttp.ClientSession() as session:
            while True:
                tasks = [self.check_endpoint(session, ep) for ep in self.endpoints]
                await asyncio.gather(*tasks)

                # Log availability stats
                for domain, stats in self.domain_stats.items():
                    availability = (stats["up"] / stats["total"]) * 100
                    logging.info(f"[cyan]{domain} has {availability:.0f}% availability[/cyan]")

                # Save reports and update trends
                self.save_reports()
                self.update_availability_trends()

                await asyncio.sleep(self.interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Endpoint Health Checker")
    parser.add_argument("config", help="Path to YAML configuration file")
    parser.add_argument("--interval", type=int, default=15, help="Health check interval in seconds")
    args = parser.parse_args()

    checker = HealthChecker(args.config, args.interval)
    try:
        asyncio.run(checker.run_health_checks())
    except KeyboardInterrupt:
        logging.info("[bold yellow]Health checker stopped.[/bold yellow]")
