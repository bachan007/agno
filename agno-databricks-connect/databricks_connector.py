import json
from typing import Optional, Any
from agno.tools import Toolkit
from agno.utils.log import logger

try:
    import databricks.sql
except ImportError:
    raise ImportError("`databricks-sql-connector` not installed. Install it using `pip install databricks-sql-connector`")


class DatabricksSQL(Toolkit):
    """
    A toolkit for connecting to Databricks and running SQL queries.

    Args:
        server_hostname (str): Databricks server hostname.
        http_path (str): Databricks SQL Warehouse HTTP path.
        access_token (str): Databricks personal access token (PAT).
        catalog (Optional[str]): Default catalog to use.
        schema (Optional[str]): Default schema to use.
        connect (bool): Automatically establish connection on initialization.
    """

    def __init__(
        self,
        server_hostname: str,
        http_path: str,
        access_token: str,
        catalog: Optional[str] = None,
        schema: Optional[str] = None,
        connect: bool = True,
    ):
        super().__init__(name="databricks_sql")
        self.server_hostname = server_hostname
        self.http_path = http_path
        self.access_token = access_token
        self.catalog = catalog
        self.schema = schema
        self.connection: Optional[databricks.sql.Connection] = None

        if connect:
            self.connect()

        # Register query execution function
        self.register(self.run_query)

    def connect(self):
        """Establishes a connection to Databricks SQL Warehouse."""
        try:
            self.connection = databricks.sql.connect(
                server_hostname=self.server_hostname,
                http_path=self.http_path,
                access_token=self.access_token,
                catalog=self.catalog,
                schema=self.schema,
            )
            logger.info("Connected to Databricks SQL Warehouse")
        except Exception as e:
            logger.error(f"Failed to connect to Databricks: {e}")
            self.connection = None

    def run_query(self, query: str, max_results: int = 10) -> str:
        """Executes a SQL query and returns the results.

        Args:
            query (str): The SQL query to execute.
            max_results (int, optional): The maximum number of results to return. Default is 10.

        Returns:
            str: JSON-formatted query results.
        """
        if not self.connection:
            return "Error: No active Databricks connection"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()

                # Convert results to JSON format
                columns = [desc[0] for desc in cursor.description]
                data = [dict(zip(columns, row)) for row in results[:max_results]]

                return json.dumps(data, indent=2)
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            return f"Error executing query: {e}"
