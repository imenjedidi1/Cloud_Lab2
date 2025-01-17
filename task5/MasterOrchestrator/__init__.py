import azure.durable_functions as df
import logging

def orchestrator_function(context: df.DurableOrchestrationContext):
     # Step 1: Get input data from Azure Blob Storage
    input_data = yield context.call_activity("GetInputDataFn", None)
    logging.info(f"Fetched input data: {input_data}")

    # Step 2: Map
    mapper_tasks = []
    for line in input_data:
        line_number, line_content = line  # Unpack (line_number, line_content)
        mapper_tasks.append(context.call_activity("Mapper", (line_number, line_content)))

    # Run mappers in parallel
    map_outputs = yield context.task_all(mapper_tasks)
    map_outputs = [item for sublist in map_outputs for item in sublist]  # Flatten

    # Step 3: Shuffle
    shuffler_output = yield context.call_activity("Shuffler", map_outputs)

    # Step 4: Reduce
    reducer_tasks = []
    for word, values in shuffler_output.items():
        reducer_tasks.append(context.call_activity("Reducer", (word, values)))

    # Run reducers in parallel
    reduce_outputs = yield context.task_all(reducer_tasks)

    return reduce_outputs  # Final results

main = df.Orchestrator.create(orchestrator_function)
