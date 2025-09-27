import threading
import time
semaphore = threading.Semaphore(3)

def safe_print(content: str, delay=0.3, iterations=10):
    for i in range(iterations):
        with semaphore:
            time.sleep(delay)
            print(content)

first_thread = threading.Thread(target=safe_print, args=('A',), kwargs={'delay': 0.3, 'iterations': 10})
second_thread = threading.Thread(target=safe_print, args=('B',))

first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()