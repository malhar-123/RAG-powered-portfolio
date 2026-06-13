"""
Malhar Gudekar — Portfolio Knowledge Base
Each string is an independently retrievable document chunk.
"""

DOCUMENTS = [

    # ── PERSONAL BIO ──────────────────────────────────────────────────────────
    """Malhar Gudekar is a Data Engineer and AI/ML Engineer based in the USA.
He builds production-grade data pipelines and intelligent AI systems — from raw
ingestion through deployed ML models.
Core stack: PySpark, Kafka, Airflow, dbt, FastAPI, PostgreSQL, PyTorch, LLMs, RAG.
Open to full-time roles in Data Engineering, ML Engineering, or Analytics Engineering.
Contact: gudekar2@illinois.edu
LinkedIn: https://linkedin.com/in/malhar-gudekar
GitHub: https://github.com/malhar-123""",

    # ── EDUCATION ─────────────────────────────────────────────────────────────
    """Malhar holds a Master of Science in Information Management from the University
of Illinois Urbana-Champaign (UIUC), completed 2024-2025 in Champaign IL.
Coursework: distributed systems, NLP, data engineering pipelines, machine learning,
deep learning, and human-centered AI design.

He also holds a Bachelor of Engineering in Computer Science from Mumbai University,
completed 2019-2023 in Mumbai India.
Strong foundations in algorithms, data structures, operating systems, and software
engineering. Projects spanned mobile development, data analytics, and systems
programming.""",

    # ── EXPERIENCE: UIUC iSchool Research Assistant ───────────────────────────
    """Malhar worked as a Research Assistant at the University of Illinois
Urbana-Champaign iSchool from May 2025 to Present (Champaign IL).
He owned end-to-end design and integration of a cross-platform mHealth system
ingesting wearable health data for 100+ users.
He optimized PostgreSQL schema, indexing strategies, and query execution plans,
improving query performance by 38%.
He built production-ready Python pipelines with RAG-based context summarization,
boosting multi-turn LLM response accuracy by 43%.
He developed backend workflows for real-time, fault-tolerant processing of
longitudinal health data.
Tech stack: Python, PostgreSQL, RAG, FastAPI, Flutter, Wearable Data.""",

    # ── EXPERIENCE: UIUC CHI Infodemic Research ───────────────────────────────
    """Malhar worked as a Research Assistant at the University of Illinois
Urbana-Champaign CHI AI in Infodemic Management lab from January 2025 to
May 2025 (Champaign IL).
He designed and deployed scalable NLP pipelines to process high-volume social
media datasets, cutting processing latency by 41%.
He built distributed inference pipelines using Hugging Face transformers and
Neo4j for real-time infodemic detection and pattern recognition.
He developed production-grade REST APIs using FastAPI with validation, error
handling, and monitoring across distributed system architectures.
This work supported WHO-aligned health misinformation detection at scale.
Tech stack: NLP, Hugging Face, Neo4j, FastAPI, Kafka, AWS EKS, Docker.""",

    # ── EXPERIENCE: Business Intelligence Group ────────────────────────────────
    """Malhar worked as a Technical Consultant at the Business Intelligence Group
from August 2025 to December 2025 (Champaign IL).
He architected a microservices-based RAG system using FastAPI, PostgreSQL, and
vector embeddings for production-grade document retrieval of healthcare payer rules.
He designed fault-tolerant ETL pipelines to process and index large document
datasets for low-latency retrieval.
He improved overall system performance by 64% through optimized indexing strategies
and query tuning.
He built backend services enabling real-time, high-performance querying of
unstructured data across distributed architectures.
Tech stack: RAG, ETL, FastAPI, PostgreSQL, pgVector, Vector Embeddings, Selenium.""",

    # ── EXPERIENCE: Swift Mobil ───────────────────────────────────────────────
    """Malhar worked as a Data Analyst at Swift Mobil Software Solutions Provider
from July 2023 to December 2023 (Mumbai India).
He built interactive Power BI dashboards for logistics and mobility KPIs,
reducing reporting time by 40%.
He processed and optimized large-scale operational datasets using Python and
PySpark to identify failure patterns and trends.
He developed SQL and graph queries for dependency mapping and root-cause analysis,
speeding issue resolution by 26%.
Tech stack: Power BI, PySpark, Python, SQL, Neo4j, Graph Queries, AWS S3.""",

    # ── EXPERIENCE: PScope Technologies ──────────────────────────────────────
    """Malhar worked as a Data Analyst at PScope Technologies Pvt. Ltd.
from January 2023 to June 2023 (Mumbai India).
He developed and maintained 20+ Power BI dashboards across Sales, Finance,
and Operations using SQL and DAX.
He automated recurring Excel reporting workflows using VBA, cutting report
preparation time by 42%.
He improved data consistency across weekly reporting cycles through validation
and transformation logic.
Tech stack: Power BI, SQL, DAX, VBA, Excel, Jira.""",

    # ── PROJECT: F1 Race Prediction ───────────────────────────────────────────
    """Project: F1 Race Outcome Prediction (Sports Analytics).
Malhar engineered 18 features from FastF1 telemetry covering lap times, driver
form, and team performance.
He combined Gradient Boosting with 5,000-run Monte Carlo simulations to predict
grid finishing positions.
Achieved R2 0.687 and RMSE 7.50 on held-out race data.
Built an agentic AI layer that converts natural language queries into structured
race scenarios.
Tech: Python, LightGBM, XGBoost, FastF1, Monte Carlo, Scikit-learn.
GitHub: https://github.com/malhar-123/f1-race-prediction""",

    # ── PROJECT: Predictive Credit ────────────────────────────────────────────
    """Project: Predictive Credit Limit and Risk Segmentation (Financial ML).
Malhar forecasted Q4 customer spend using LightGBM to recommend personalised
credit line adjustments.
He combined regression and risk classification for end-to-end credit lifecycle
modelling.
Tech: Python, LightGBM, Risk Modelling.
Link: https://www.kaggle.com/code/malharravigudekar/notebookebd4dc2b02""",

    # ── PROJECT: FMCG Forecasting ─────────────────────────────────────────────
    """Project: FMCG Sales Demand Forecasting (Forecasting / Time Series).
Malhar built a multi-model pipeline using SARIMA, ARIMA, Exponential Smoothing,
and Random Forest across 5 product categories in R.
95%+ of actual values fell within forecast confidence intervals.
Surfaced promotion impact and seasonality drivers to reduce stockouts and overstock.
Tech: R, SARIMA, ARIMA, Random Forest, ggplot2.
GitHub: https://github.com/malhar-123/fmcg-demand-forecasting""",

    # ── PROJECT: Environmental Analytics ──────────────────────────────────────
    """Project: Environmental Analytics and Visualization (Data Visualization).
Malhar analyzed 7 years of environmental data using Power BI heat maps and
tree maps.
Identified regional toxin concentration patterns and pollution hotspots across
geographic dimensions.
Tech: Power BI, DAX, Data Modelling.""",

    # ── PROJECT: BASILISK ─────────────────────────────────────────────────────
    """Project: BASILISK Security Hub (Security - Peer-Reviewed Publication).
Malhar implemented AES, DES3, MD5, and onion routing for secure communication
and data integrity.
Supports non-repudiation across hybrid cryptography workflows.
Published in a UGC Care Group 1 peer-reviewed journal.
Tech: Python, AES/DES3, Onion Routing, Cryptography.
GitHub: https://github.com/malhar-123/Basilisk""",

    # ── PROJECT: Facial Analysis ──────────────────────────────────────────────
    """Project: Advanced Facial Analysis System (Computer Vision).
Malhar built a real-time computer vision pipeline using Python and OpenCV
for live video stream processing.
Applied CNNs for emotion and facial feature classification, achieving 98% accuracy.
Tech: Python, OpenCV, CNN, Deep Learning.
GitHub: https://github.com/malhar-123/python_face_detection""",

    # ── PROJECT: Database NRA ─────────────────────────────────────────────────
    """Project: Database Design for Nonresident Alien Payments (Data Modelling).
Malhar designed SQL and Neo4j systems for tax-compliant international payment
workflows.
Modeled visa status, tax treaty rules, and compliance forms (W-8BEN, 8233)
across EER and relational schemas.
Supports automated withholding decisions and audit-ready payment records.
Tech: SQL, Neo4j, EER Modelling, Data Architecture.
Link: https://malhar-123.github.io/tax-payment-data-model/""",

    # ── PROJECT: Mobile Expense Tracker ───────────────────────────────────────
    """Project: Mobile Expense Tracker App (Cross-Platform Mobile).
Malhar built a cross-platform Flutter app with Provider state management and
interactive spending charts.
Deployed across Android, iOS, Web, Windows, macOS, and Linux from a single codebase.
Tech: Flutter, Dart, Provider, Cross-Platform.
GitHub: https://github.com/malhar-123/Mobile-Expense-Tracking-and-PA""",

    # ── SKILLS ────────────────────────────────────────────────────────────────
    """Malhar Gudekar's technical skills:
Data Engineering: PySpark, Apache Kafka, Apache Airflow, Apache Flink, dbt,
  ETL pipelines, Apache Iceberg, AWS S3.
Machine Learning and AI: PyTorch, Scikit-learn, LightGBM, XGBoost, RAG pipelines,
  LLMs, Hugging Face Transformers, sentence-transformers, RAGAS evaluation.
Backend: FastAPI, Python, REST APIs, Docker, Microservices.
Databases: PostgreSQL, Neo4j, ChromaDB, pgVector, vector databases.
Cloud: AWS (S3, EKS), Render.
Analytics and BI: Power BI, Tableau, SQL, DAX, Excel, VBA.
Mobile: Flutter, Dart.
Languages: Python, R, SQL, Dart, JavaScript.""",

    # ── LEADERSHIP ────────────────────────────────────────────────────────────
    """Malhar's leadership and campus roles:
Project Manager at StarDis at Illinois (Aug 2025 to Present): Led a cross-functional
team of 6 engineers and designers delivering product updates for DeepCover.
Drove sprint planning, backlog grooming, and QA issue tracking through JIRA.
Drove 25% user growth and improved app ratings to 4.0 stars.

Student Career Navigator at UIUC Career Center (Aug 2025 to Present): Analyzed
17,000+ student records for the Illinois Success Report. Mentored 10+ students
on career strategy, improving job-search confidence by 35%.

Data Quality and Accessibility Assistant at University of Illinois System
(Jun 2025 to Present, Remote): Standardized 50+ institutional documents.
Validated screen-reader compatibility through manual QA.

Team Lead at National Service Scheme (Jun 2020 to Jun 2022, India): Led community
drives and rural outreach camps directly impacting 1,000+ individuals.""",

    # ── ACHIEVEMENTS ──────────────────────────────────────────────────────────
    """Malhar Gudekar's key metrics and achievements:
- 10M+ records processed through PySpark pipelines in production.
- 64% peak performance lift at Business Intelligence Group.
- 43% improvement in multi-turn LLM response accuracy via RAG pipelines.
- 41% reduction in NLP pipeline processing latency.
- 38% improvement in PostgreSQL query performance.
- 40% reduction in Power BI reporting time at Swift Mobil.
- 42% reduction in report preparation time at PScope (VBA automation).
- 100+ users on the UIUC mHealth wearable data platform.
- 20+ Power BI dashboards built across multiple roles.
- 9 projects shipped spanning ML, Data Engineering, CV, and AI.
- 5+ data and ML roles across research and industry.""",

    # ── CURRENTLY EXPLORING ───────────────────────────────────────────────────
    """Malhar is currently learning and exploring:
- Apache Flink: stateful stream processing at scale, building on existing Kafka work.
- dbt: SQL transformation layer with software engineering best practices (testing,
  versioning, documentation).
- RAGAS: LLM evaluation framework for RAG systems - faithfulness, answer relevancy,
  context precision metrics.
- Apache Iceberg: open table format for lakehouse architectures, time-travel queries,
  and schema evolution on object storage.""",

    # ── PERSONAL / BEYOND CODE ────────────────────────────────────────────────
    """Malhar's interests and hobbies beyond engineering:
- Mountaineering: 40+ mountain peaks climbed.
- Travel: 10+ countries explored.
- Formula 1: avid racing enthusiast, interested in performance optimization and
  data-driven strategy (which also inspired the F1 ML project).
- Art: painter.
- Endurance sports: triathlete (running, cycling, swimming).
- Motorcycling: completed the Ladakh circuit and canyon road trips.""",

    # ── CONTACT ───────────────────────────────────────────────────────────────
    """Malhar Gudekar contact information and links:
Email: gudekar2@illinois.edu
LinkedIn: https://linkedin.com/in/malhar-gudekar
GitHub: https://github.com/malhar-123
Kaggle: https://www.kaggle.com/malharravigudekar
He is actively seeking full-time roles in Data Engineering, ML Engineering,
or Analytics Engineering.""",
]

# Unique IDs for ChromaDB
IDS = [f"doc_{i}" for i in range(len(DOCUMENTS))

    # ── AUTO-GENERATED RESUME DOCUMENTS ─────────────────────────────────────────

     

]
