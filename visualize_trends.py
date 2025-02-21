import pandas as pd
import matplotlib.pyplot as plt
import os

# File path for availability trends
TRENDS_FILE = "logs/availability_trends.csv"
OUTPUT_IMAGE = "logs/availability_trends.png"

# Define alert threshold (e.g., below 80% is considered critical)
ALERT_THRESHOLD = 80.0  

def plot_availability_trends():
    """Read availability data and generate a graph with alerts."""
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

    # Create the plot
    plt.figure(figsize=(10, 5))
    
    for domain in df["domain"].unique():
        domain_df = df[df["domain"] == domain]

        # Identify low availability points
        low_availability = domain_df["availability"] < ALERT_THRESHOLD

        # Plot normal availability in blue
        plt.plot(domain_df["timestamp"], domain_df["availability"], marker="o", linestyle="-", label=domain, color="blue")

        # Highlight critical availability drops in red
        plt.scatter(domain_df["timestamp"][low_availability], domain_df["availability"][low_availability], color="red", label=f"{domain} (Low Availability)")

        # Check if any domain is below the threshold
        if any(low_availability):
            print(f"⚠️ WARNING: {domain} dropped below {ALERT_THRESHOLD}% availability!")

    # Formatting the graph
    plt.xlabel("Timestamp")
    plt.ylabel("Availability (%)")
    plt.title("Long-Term Availability Trends with Alerts")
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
