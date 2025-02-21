import pandas as pd
import matplotlib.pyplot as plt
import os

# File path for availability trends
TRENDS_FILE = "logs/availability_trends.csv"
OUTPUT_IMAGE = "logs/availability_trends.png"

def plot_availability_trends():
    """Read availability data and generate a graph."""
    if not os.path.exists(TRENDS_FILE):
        print("No availability trends data found. Run the health checker first.")
        return

    # Load the CSV data
    df = pd.read_csv(TRENDS_FILE)

    if df.empty:
        print("No data available in availability trends file.")
        return

    # Convert timestamp to datetime for proper plotting
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Plot availability for each domain
    plt.figure(figsize=(10, 5))
    for domain in df["domain"].unique():
        domain_df = df[df["domain"] == domain]
        plt.plot(domain_df["timestamp"], domain_df["availability"], marker="o", linestyle="-", label=domain)

    # Formatting the graph
    plt.xlabel("Timestamp")
    plt.ylabel("Availability (%)")
    plt.title("Long-Term Availability Trends")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Save the figure
    plt.tight_layout()
    plt.savefig(OUTPUT_IMAGE)
    print(f"Graph saved as {OUTPUT_IMAGE}")

    # Display the graph
    plt.show()

if __name__ == "__main__":
    plot_availability_trends()
