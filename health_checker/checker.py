import asyncio
import os
import aiohttp
import yaml
import argparse
import logging
import time
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
    
    def load_yaml(self) -> List[Dict]:
        """Load the endpoints from the YAML configuration file."""
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)

    async def check_endpoint(self, session: aiohttp.ClientSession, endpoint: Dict):
        """Perform a health check on a single endpoint."""
        url = endpoint.get("url")
        name = endpoint.get("name", "Unknown Endpoint")
        method = endpoint.get("method", "GET").upper()
        headers = endpoint.get("headers", {})
        body = endpoint.get("body", None)
        domain = url.split("/")[2]  # Extract domain from URL

        latency = None  # Ensure latency always exists
        status = "DOWN"  # Default to DOWN in case of failure

        start_time = time.time()
        try:
            async with session.request(method, url, headers=headers, json=body) as response:
                latency = (time.time() - start_time) * 1000  # Convert to ms
                if 200 <= response.status < 300 and latency < 500:
                    status = "UP"

        except Exception as e:
            logging.warning(f"[bold yellow]{name} ({url}) failed with error:[/bold yellow] {e}")

        # Track stats
        self.domain_stats[domain]['total'] += 1
        if status == "UP":
            self.domain_stats[domain]['up'] += 1

        latency_display = f"{latency:.2f}ms" if latency is not None else "N/A"
        log_color = "[green]" if status == "UP" else "[red]"
        logging.info(f"{log_color}{name} ({url}) - Status: {status} - Latency: {latency_display}[/]")

    async def run_health_checks(self):
        """Continuously check endpoints every interval."""
        async with aiohttp.ClientSession() as session:
            while True:
                tasks = [self.check_endpoint(session, ep) for ep in self.endpoints]
                await asyncio.gather(*tasks)
                
                # Log availability stats
                for domain, stats in self.domain_stats.items():
                    availability = (stats['up'] / stats['total']) * 100
                    logging.info(f"[cyan]{domain} has {availability:.0f}% availability[/cyan]")
                
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
