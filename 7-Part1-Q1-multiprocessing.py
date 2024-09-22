import multiprocessing as mp
import time

# Example function that simulates processing a chunk of records
def process_data_chunk(data_chunk):
    # Simulate some heavy computation
    result = [x ** 2 for x in data_chunk]
    return result

def parallel_processing(data, num_processes):
    # Split the data into chunks
    chunk_size = len(data) // num_processes
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Create a pool of worker processes
    with mp.Pool(processes=num_processes) as pool:
        # Use pool.map to parallelize the execution of process_data_chunk
        results = pool.map(process_data_chunk, chunks)
    
    # Combine the results from all processes
    return [item for sublist in results for item in sublist]

if __name__ == "__main__":
    # Example: Simulate a large dataset with millions of records
    data = list(range(1, 10000000))
    
    # Measure execution time
    start_time = time.time()
    
    # Specify the number of cores/processes you want to use
    num_processes = mp.cpu_count()  
    
    # Run the parallel processing
    processed_data = parallel_processing(data, num_processes)
    
    # Print the results (optional)
    # print(processed_data)
    
    print(f"Processing completed in {time.time() - start_time} seconds")
