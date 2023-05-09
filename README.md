# Dockerized Data Pipeline for Twitter Sentiment Analysis

This project aims to build a Dockerized Data Pipeline that collects tweets, analyzes their sentiment, and publishes the best or worst sentiment on Slack every 10 minutes. The pipeline involves various components such as data collection, storage, ETL, sentiment analysis, and integration with Slack. This README file provides an overview of the project and guides users on how to set up and run the pipeline.

## Project Structure

The project repository is organized as follows:

```
- docker-compose.yml
- README.md
- /etl
    - etl.py
- /sentiment_analysis
    - sentiment_analysis.py
- /twitter_data_collector
    - twitter_data_collector.py
- /slack_publisher
    - slack_publisher.py
```

The main components of the pipeline include:

- `docker-compose.yml`: Defines the Docker services and their configurations.
- `etl/etl.py`: Extracts data from MongoDB, transforms it, and loads it into PostgreSQL.
- `sentiment_analysis/sentiment_analysis.py`: Performs sentiment analysis on the text data.
- `twitter_data_collector/twitter_data_collector.py`: Collects tweets and stores them in MongoDB.
- `slack_publisher/slack_publisher.py`: Publishes selected tweets' sentiment on Slack.

## Prerequisites

Before running the pipeline, ensure that you have the following dependencies installed:

- Docker
- Docker Compose

## Setup Instructions

To set up and run the pipeline, follow these steps:

1. Clone the project repository from GitHub:

   ```shell
   git clone github.com/elendarn/etl_pipeline
   ```

2. Navigate to the project directory:

   ```shell
   cd dockerized-data-pipeline
   ```

3. Build and start the Docker containers using Docker Compose:

   ```shell
   docker-compose up -d
   ```

   This command will create and start the necessary containers, including MongoDB, PostgreSQL, and the pipeline components.

4. Wait for the containers to start and initialize. You can check the logs to ensure everything is running smoothly:

   ```shell
   docker-compose logs -f
   ```

   Press `Ctrl + C` to exit the log view.

5. The data pipeline will start collecting tweets, analyzing their sentiment, and publishing the results on Slack automatically every 10 minutes. You can view the logs to monitor the pipeline's progress:

   ```shell
   docker-compose logs -f slack_publisher
   ```

   Press `Ctrl + C` to exit the log view.

6. To stop the pipeline and clean up the Docker containers, run the following command:

   ```shell
   docker-compose down
   ```

   This will stop and remove the containers, but the data stored in MongoDB and PostgreSQL will be preserved.

## Configuration

The project comes with default configurations for various components. However, you may modify these configurations as per your requirements:

- Twitter API credentials: Update the `twitter_collector/twitter_collector.py` file with your Twitter API credentials. You can create a Twitter developer account and generate API keys and access tokens.

- Slack API credentials: Update the `slack_publisher/slack_publisher.py` file with your Slack API credentials. Create a Slack app and obtain the necessary tokens to publish messages.

## Notes

- This project serves as a learning opportunity for Docker and ETL concepts in a data engineering context. Although the same task could be accomplished with fewer components, the goal is to gain experience and understanding of these technologies.

- Ensure that you comply with Twitter's terms of service and API usage guidelines when collecting and analyzing tweets.

- Feel free to explore and enhance the pipeline as per your requirements and learning objectives.

## Conclusion

The Dockerized Data Pipeline for Twitter Sentiment Analysis
