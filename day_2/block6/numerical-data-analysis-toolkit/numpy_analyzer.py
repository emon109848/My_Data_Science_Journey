import numpy as np

def load_data(filepath):
    """Load CSV dataset"""
    data = np.loadtxt(filepath, delimiter=",")
    return data


def compute_statistics(data):
    """Compute basic statistics"""
    stats = {}

    stats["mean"] = np.mean(data, axis=0)
    stats["median"] = np.median(data, axis=0)
    stats["std"] = np.std(data, axis=0)
    stats["min"] = np.min(data, axis=0)
    stats["max"] = np.max(data, axis=0)

    return stats


def compute_correlation(data):
    """Compute correlation matrix"""
    return np.corrcoef(data, rowvar=False)


def normalize_data(data):
    """Z-score normalization"""
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    normalized = (data - mean) / std
    return normalized


def save_results(filepath, stats, corr_matrix):
    """Save results to text file"""
    with open(filepath, "w") as f:
        f.write("=== BASIC STATISTICS ===\n")
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")

        f.write("\n=== CORRELATION MATRIX ===\n")
        f.write(str(corr_matrix))


def main():
    input_file = "input_data.csv"
    output_file = "results.txt"

    data = load_data(input_file)

    stats = compute_statistics(data)
    corr_matrix = compute_correlation(data)
    normalized = normalize_data(data)

    save_results(output_file, stats, corr_matrix)

    print("Analysis complete.")
    print("Results saved to", output_file)


if __name__ == "__main__":
    main()
