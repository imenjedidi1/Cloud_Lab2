import azure.functions as func
import azure.durable_functions as df
import logging
async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    try:
        # Get the orchestrator name from the route
        function_name = req.route_params.get("functionName")

        # Start the orchestrator without requiring input data
        instance_id = await client.start_new(function_name, None, None)
        logging.info(f"Started orchestration with ID = '{instance_id}'.")

        return client.create_check_status_response(req, instance_id)
    except Exception as e:
        logging.error(f"Error starting orchestration: {str(e)}")
        return func.HttpResponse(
            f"Failed to start orchestration. Error: {str(e)}",
            status_code=500
        )
