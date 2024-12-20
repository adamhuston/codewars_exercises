import time
import threading

def stopwatch():
    print("Press Enter to start the stopwatch")
    input()
    start_time = time.time()
    print("Stopwatch started. Press Enter to stop.")
    input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    stopwatch()
    def print_current_time(start_time):
        while True:
            elapsed_time = time.time() - start_time
            print(f"\rElapsed time: {elapsed_time:.2f} seconds", end="")
            time.sleep(1)

    if __name__ == "__main__":
        print("Press Enter to start the stopwatch")
        input()
        start_time = time.time()
        threading.Thread(target=print_current_time, args=(start_time,), daemon=True).start()
        print("Stopwatch started. Press Enter to stop.")
        input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nFinal elapsed time: {elapsed_time:.2f} seconds")