# THPT2024 Data Pipeline Project

## Project Description
The THPT2024 Data Pipeline project is a real-time system designed to collect, process, store, and visualize national high school exam scores from the year 2024. This system is built to operate in real-time, allowing for the continuous collection of exam results from external sources, their prompt processing, and the subsequent storage and visualization of score distributions and rankings.

## Project Components

### 1. Data Crawler
- **Purpose**: To collect exam scores from websites that provide THPT national exam results.
- **Technology**: Utilizes Selenium to automate web browsing and data extraction.
- **Outcome**: The collected exam scores are converted to JSON and sent to the processing pipeline for further action.

### 2. Data Processing & Storage
- **Purpose**: To process and store the exam scores in a database.
- **Technology**:
  - Django ORM is used for database interactions with SQLite.
  - The models include `DimStudents`, `DimSubjects`, and `FactScores` to store information about students, subjects, and scores respectively.
- **Features**:
  - Stores exam scores in the database.
  - Updates and processes data when changes occur.
  - Queries data based on various criteria.

### 3. Real-time Data Visualization
- **Purpose**: To visualize exam score data in real-time.
- **Technology**:
  - Uses Matplotlib for creating score distribution and ranking charts.
  - Django provides an API to return the chart images in base64 format.
  - JavaScript is used on the frontend to refresh the charts every second.
- **Charts**:
  - Bar chart for the median scores of each subject.
  - Box plot for visualizing the score distribution across subjects.

### 4. Kafka Integration
- **Purpose**: To manage the data pipeline in real-time using Apache Kafka.
- **Technology**:
  - Kafka Consumer is used to collect data from topics and store it in the database.
  - Manages data flow between different components of the system.
- **Features**:
  - Real-time data management.
  - Integration with the processing and storage systems.

## Installation Guide

### System Requirements
- Python 3.12+
- Django 4.0+
- Docker (Docker Compose recommended)
- Apache Kafka
- Selenium WebDriver (ChromeDriver or GeckoDriver)

### Installation and Running the Project

1. **Clone the project from GitHub:**
    ```bash
    git clone https://github.com/your-username/THPT2024DataPipeline.git
    cd THPT2024DataPipeline
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the database:**
    - Edit the `settings.py` file to configure SQLite or PostgreSQL as your database.

4. **Run Django migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the project:**
    ```bash
    python manage.py runserver
    ```

6. **Run Kafka Consumer in Docker:**
    - Use Docker Compose to start Kafka and the Consumer.
    ```bash
    docker-compose up
    ```

## Usage

- Access the website at `http://localhost:8000` to view the real-time visualizations.
- Use the API to retrieve real-time exam scores.

## Contributing
We welcome contributions from the community. If you have ideas or would like to contribute to the project, please create a Pull Request or contact us.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
