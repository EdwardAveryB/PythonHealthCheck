from health_checker.checker import HealthChecker
import argparse
import asyncio

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the health checker")
    parser.add_argument("config", help="Path to YAML configuration file")
    parser.add_argument("--interval", type=int, default=15, help="Health check interval in seconds")
    args = parser.parse_args()

    checker = HealthChecker(args.config, args.interval)
    
    try:
        asyncio.run(checker.run_health_checks())
    except KeyboardInterrupt:
        print("\nHealth checker stopped.")
