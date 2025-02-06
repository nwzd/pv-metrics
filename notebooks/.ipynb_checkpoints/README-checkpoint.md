# Project Overview

This project uses Jupyter Notebooks with Apache Spark to process and analyze data. The project structure includes directories for different stages of data processing: bronze, silver, and gold.

## Setting Up the Environment

To set up the environment, you will use Docker Compose. Follow these steps:

1. **Install Docker**: Make sure you have Docker installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).

2. **Navigate to the Project Directory**: Open a terminal and navigate to the directory containing the `docker-compose.yml` file.

3. **Start the Docker Containers**: Run the following command to start the Docker containers:

    ```sh
    docker-compose up
    ```

    This command will start a Jupyter Notebook server with Apache Spark.

4. **Accessing the Jupyter Notebook**: 

Once the Docker containers are up and running, you can access the Jupyter Notebook by opening your web browser and navigating to the following URL:
 ```sh
 http://localhost:8888
 ```


Use the token `t0k3n` to log in.

## Running the Notebook

1. **Open the Notebook**: In the Jupyter Notebook interface open the `tasks.ipynb` notebook.

2. **Execute the Notebook**: Run the cells in the notebook to execute the code. The notebook processes and analyzes data stored in the [data](http://_vscodecontentref_/5) directory.

## What the Notebook Does

The `tasks.ipynb` notebook performs the following tasks:

- Reads data from the `bronze` directory.
- Processes and cleans the data.
- Writes the cleaned data to the `silver` directory.
- Further processes the data and writes the final results to the `gold` directory.

## Running Tests

To run tests for the project, navigate to the [scripts](http://_vscodecontentref_/6) directory and run the `udfs_tests.py` script:

```sh
python udfs_tests.py