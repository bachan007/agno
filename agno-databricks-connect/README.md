# Databricks Connection Setup

## Prerequisites

Before running the code, ensure you have the following prerequisites met:

1. **Install Required Libraries:**
   - Run the following command to install dependencies from `requirements.txt`:
     ```sh
     pip install -r requirements.txt
     ```

2. **Set Environment Variables in Script:**
   - The script automatically sets the required environment variables using `os`.
   - Example snippet from `query_databricks.py`:
     ```python
     import os
     os.environ["LLM_API_KEY"] = "your_api_key"
     os.environ["DATABRICKS_HOST"] = "https://your-databricks-instance"
     os.environ["DATABRICKS_TOKEN"] = "your-databricks-token"
     ```

3. **Configure Databricks Credentials:**
   - Ensure the Databricks credentials are correctly set within the script.

## Running the Script

Once the prerequisites are met, execute the script:

```sh
python query_databricks.py
```

The script will prompt you to enter a query. Provide the query as input, then sit back and relax while the system processes it and returns the output.

---

### Notes:
- Ensure that you have the correct permissions to access Databricks.
- If any issues arise, check your environment variables and credentials before troubleshooting further.

Happy querying! 🚀

