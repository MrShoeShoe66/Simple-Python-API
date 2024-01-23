import time
import util.getRoutes as gr

total_time = 0

for _ in range(100):
    start_time = time.time()

    imported_modules = gr.import_files_from_folder("routes")

    end_time = time.time()

    execution_time = end_time - start_time
    total_time += execution_time

    time.sleep(1)

average_time = total_time / 100
print("Average execution time:", average_time, "seconds")
