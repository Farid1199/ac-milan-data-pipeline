#  AC Milan Performance ETL Pipeline (2023/24 Season)

##  Project Overview
This project is an automated **ETL (Extract, Transform, Load)** pipeline designed to process and analyze AC Milan's performance data for the 2023/24 Serie A season. 

The goal was to take raw match and player data, engineer new performance metrics (like Goal Contributions and Match Goal Differences), and load them into a structured SQL database for professional-grade analytics.

---

##  ETL Architecture
The pipeline follows a modular architecture to ensure clean code and scalability:

```mermaid
graph LR
    A[Raw CSV Data] --> B[Extract]
    B --> C[Transform]
    C --> D[Load]
    D --> E[(SQLite DB)]
    D --> F[Clean CSV Exports]
    E --> G[SQL Analytics]



##  Project Structure
    ac-milan-data-pipeline/
│
├── data/               # Raw input data (Matches & Players)
├── scripts/            # Python ETL logic
│   ├── extract.py      # Data ingestion logic
│   ├── transform.py    # Feature engineering & cleaning
│   ├── load.py         # Database & Export logic
│   └── etl_pipeline.py # Master execution script
├── database/           # Produced SQLite database file
├── exports/            # Clean, transformed CSVs for reporting
├── sql/                # Analytical queries for business insights
├── requirements.txt    # Project dependencies
└── README.md


## Technologies Used

    Language: Python 3.x

    Data Manipulation: Pandas

    Database Connection: SQLAlchemy

    Database: SQLite

    Environment: GitHub Codespaces / VS Code

🚀 How to Run

    Clone the repository:
    code Bash

    git clone <your-repo-link>

    Install dependencies:
    code Bash

    pip install -r requirements.txt

    Run the full pipeline:
    code Bash

    python3 scripts/etl_pipeline.py