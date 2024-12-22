import time
from src.calculator import add

def benchmark_addition():
    start_time = time.perf_counter()
    for _ in range(1_000_000):
        add(10, 5)
    end_time = time.perf_counter()
    print(f"Benchmark: add(10, 5) executed 1,000,000 times in {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    print("Running Benchmark Test:")
    benchmark_addition()
