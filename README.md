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

## What the Notebook Does

The `tasks.ipynb` notebook performs the following tasks:

- The notebook executes the tasks defined in the challenge.
- Reads data from the `data/bronze` directory.
- Processes and cleans the data. 
- Writes the cleaned data to the `data/silver` directory.
- Writes corrupt data to the `data/corrupt` directory.
- Further processes the data and writes the final results to the `data/gold` directory.
