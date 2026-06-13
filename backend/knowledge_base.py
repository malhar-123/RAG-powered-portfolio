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

    """TAILORED RESUME — Gudekar_Malhar_Deloitte_fde
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed production agentic AI system on Amazon Bedrock and Bedrock Agents using LangChain orchestration, FastAPI, and
pgVector, delivering enterprise-scale document intelligence with measurable 64% efficiency gain
•Designed fault-tolerant ETL and async ingestion pipelines with CI/CD automation, structured prompt management, and LLM evaluation hooks
for low-latency production-grade retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed AI serving layer integrating Bedrock Guardrails and human-in-the-loop review controls for real-time safety enforcement and
high-performance LLM inference across enterprise distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production GenAI pipeline using Amazon Bedrock Knowledge Bases and structured prompt engineering to enable RAG-based contextual
summarization, improving multi-turn response accuracy by 43%
•Developed async backend workflows with MLflow-based LLM evaluation tracking for real-time, fault-tolerant processing of longitudinal data,
ensuring model reliability and observability at scale
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed scalable GenAI pipelines using LlamaIndex and Hugging Face Transformers in Python, reducing inference latency by 41% through
optimized prompt evaluation and embedding retrieval workflows
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed production REST APIs using FastAPI to serve LLM-powered models, implementing prompt versioning, A/B evaluation, CI/CD
deployment automation, and monitoring to ensure reliable LLMOps delivery across distributed enterprise systems
•Partnered with cross-functional research stakeholders to translate analytical requirements into scalable GenAI data processing workflows across
high-volume social media corpora
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•AutomatedExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing time by42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudedkar Quant Dev
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
Coursework:Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
Coursework:DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
Quantitative & Statistical:Time Series Analysis, Statistical Modeling, Predictive Analytics, Feature Engineering, Backtesting, ARIMA,
Regression, Classification, Model Evaluation, Hypothesis Testing, Monte Carlo Simulation
Programming & OOP:Python (OOP, NumPy, Pandas, Scikit-learn, LightGBM), SQL, R, C++ (basic)
Systems & Data:PostgreSQL, Linux, ETL Pipelines, FastAPI, Kafka, PySpark, AWS, Docker, Git
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Designed and implemented end-to-endstatistical modeling pipelinein Python to ingest and analyze time-series wearable sensor data from
100+ users, applying feature engineering and temporal pattern extraction to surface longitudinal behavioral signals for downstream predictive
analytics
•Optimized PostgreSQL schema, indexing strategies, and query execution plans for high-volume time-series datasets, improving query throughput
by38%and enabling low-latency access to model-ready features in production Linux environments
•Built embedding-based retrieval and summarization pipeline to enhance contextual understanding of user interactions, improving multi-turn
response accuracy by 43% and supporting more reliable behavioral analysis
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Conducted full statistical research cycle in Python — dataset evaluation, feature selection, model prototyping, and performance monitoring —
on large-scale social media corpora, reducing inference latency by41%and improving classification precision through iterative model tuning
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade REST APIs in FastAPI to serve trained statistical models, implementing input validation, performance monitoring,
and automated deployment workflows ensuring reproducible, low-latency inference across distributed Linux infrastructure
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Designed and deployed end-to-endquantitative data pipelinecombining ETL, feature engineering, and vector-based retrieval to improve
document scoring precision by64%, maintaining fault-tolerant operation under production load
•Designed scalableETLand feature pipelines usingFastAPIandPostgreSQLto transform unstructured data into structured formats suitable
for analytics and machine learning use cases
•Profiled and optimized indexing strategies and query execution plans to achieve low-latency model inference, reducing system response time
by64%and enabling real-time analytical serving in a production environment
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Analyzed large-scale operational datasets usingPythonandPySparkto identify trends, anomalies, and performance issues, combining
exploratory analysis and root cause investigation to support data-driven decision-making
•BuiltPower BIdashboards to track key performance indicators and improve visibility into operational performance, reducing reporting time
by 40%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst
•Developed and maintained Power BI dashboards usingSQLandDAX, transforming raw data into actionable insights for business decision-
making across multiple domains.
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Led across-functionalteam of six to deliver and scale Deepcover game enhancements by leveraging user data, performance metrics, and
feedback analysis to drive feature prioritization and improve games outcomes
Projects
Scalable ML System for Customer Risk Prediction
•Built end-to-end quantitative modeling system in Python using Pandas and LightGBM to forecast customer spending from large-scaletime-
series transaction data, applying feature engineering on behavioral trends and temporal patterns to improve prediction precision by20%
•Designed and implementedbacktesting frameworkto validate model performance across rolling historical time windows, stress-testing
predictions under distribution shift and varying market conditions
•Developed OOP-structured decision framework for risk-aware credit line classification, encapsulating feature pipelines, model inference, and
threshold logic in a maintainable, modular Python codebase""",

    """TAILORED RESUME — Malhar Gudekar AI & IT Solution Analyst
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-basedRAG and agentic AI systemusingFastAPI,PostgreSQL, and vector embeddings for
production applications
•Designed fault-tolerant ETL and async pipelines integrating structured and unstructured enterprise document sources, enabling low-latency AI
retrieval with data classification and access-controlled indexing
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Designed and integrated enterprise AI backend ingesting cross-platform data sources for 100+ users, establishing governance-aligned data
pipelines and secure access controls for scalable downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python RAG pipeline retrieving and summarizing enterprise policy and operational documents, improving AI response
accuracy by 43% for internal decision-support workflows
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed production-grade REST APIs using FastAPI to serve AI models, implementing input validation, audit logging, performance
monitoring, and automated deployment for compliant enterprise AI integration
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure patterns and performance issues in distributed
systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 engineers and designers to deliver AI-driven product features, gathering multi-stakeholder feedback and
performance insights to prioritize and deploy capabilities iteratively
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Eng Python Beacon Fire
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed production RAG and agentic AI system in Python using FastAPI, PostgreSQL, and vector embeddings, implementing
agentic workflows with tool use, prompt engineering, and iterative retrieval evaluation to improve output accuracy
•Designed fault-tolerant document ingestion pipelines implementing chunking strategies, embedding generation, and vector indexing to support
low-latency RAG retrieval and reranking workflows
•Improved RAG retrieval efficiency by 64% through optimized indexing, reranking strategies, and iterative evaluation of retrieval quality and
answer grounding in production
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built robust, production-readyPython generative AI pipelinewith retrieval and context summarization, improving response accuracy by43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed ingestion and knowledge graph pipelines using Kafka and Neo4j, enabling graph-based entity linking, retrieval fusion, and
real-time high-throughput processing for AI-powered search workflows
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Engineer AdAgency
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed multi-agent AI orchestration system using LangChain, AutoGen, FastAPI, and PostgreSQL with Weaviate vector search,
enabling agent communication, memory, and automated decision-making in production
•Designed fault-tolerant async data pipelines for campaign performance tracking, budget optimization logging, and low-latency analytics across
high-volume advertising data streams
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services enabling real-time AI model serving and external advertising API integrations, supporting automated campaign
launch, optimization, and reporting workflows across multiple platforms
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python multi-agent pipeline using CrewAI and LangGraph for agent orchestration, retrieval, and context management,
improving automated decision-making accuracy by 43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data pipelines using Kafka and Redis for real-time high-throughput processing, enabling agent execution tracking, performance
monitoring, and reliable data availability across systems
•Designed and developed production-grade REST APIs using FastAPI, building React and Next.js TypeScript dashboards for monitoring and
workflow control, with Sentry observability and automated deployment across distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation, scheduling logic, reducing report preparation time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Engineer Cornerstone
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git, NoSQL, Agile/Scrum
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-basedRAG and agentic AI systemusingFastAPI,PostgreSQL, and vector embeddings for
production applications
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed and deployed backend AI services in AWS cloud environments, enabling real-time high-performance model serving of unstructured
data across scalable systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python pipeline integrating generative AI and LLM capabilities into backend services, improving accuracy by 43%
•Developed backend features following established coding standards, conducting testing and validation to ensure reliable, fault-tolerant processing
for high-volume health data
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines using Kafka and Neo4j NoSQL graph databases for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Documented AI system architecture, data flows, and API design patterns to support team knowledge-sharing and reproducible deployment
across environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Collaborated with engineers and UX designers to deliver AI-driven product features for DeepCover, translating design requirements and user
feedback into technical implementation decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Engineer Manulife
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based RAG and agentic AI system using FastAPI, PostgreSQL, and vector embeddings, following
MLOps/LLMOps practices for production
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by 64% through optimized indexing, pipeline tuning, and observability tooling including logging and alerting
in production
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built robust, production-ready Python generative AI pipeline using prompt engineering, retrieval, and context summarization, improving
response accuracy by 43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highly scalable NLP and generative AI pipelines in Python with model monitoring and drift tracking, reducing
processing latency by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Engineer Motion Recruitment
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, AWS (S3, EC2, EKS), GCP, Docker, Git, React, LangChain, Prompt Engineering, OpenAI API
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable agentic AI system with LLM integration and RAG using FastAPI, PostgreSQL, and vector embeddings to automate
internal workflows and improve data accessibility
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services and internal tooling enabling real-time AI model serving and automated data access for operational teams across
distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python pipeline integrating LLMs for automated retrieval, summarization, and internal knowledge access, improving
accuracy by 43%
•Developed backend services and lightweight React components to enable real-time data access and internal team tooling with focus on reliability
and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable LLM-based automation pipelines in Python to process and analyze datasets, reducing latency by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Built Python automation tools to eliminate manual data workflows and improve operational efficiency across data-intensive team processes
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Collaborated with engineers and designers to build AI-driven software product features in Python and React, using engagement metrics and
user feedback to guide development decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Engineer Tech Consulting
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-basedRAG and agentic AI systemusingFastAPI,PostgreSQL, and vector embeddings for
production applications
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built robust, production-readyPython generative AI pipelinewith retrieval and context summarization, improving response accuracy by43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure patterns and performance issues in distributed
systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Scientist Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Leveraged AI-assisted analysis of 10000+ player feedback points and gameplay telemetry to identify product opportunities, accelerating feature
prioritization by 35% and informing roadmap decisions
•Collaborated with engineering teams to integrate AI-driven insights into product planning, enabling data-backed feature development and
iterative user experience improvements
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Engineer VC5
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based RAG and agentic AI system using FastAPI, PostgreSQL, and vector embeddings, following
MLOps/LLMOps practices for production
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by 64% through optimized indexing, pipeline tuning, and observability tooling including logging and alerting
in production
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built robust, production-ready Python generative AI pipeline using prompt engineering, retrieval, and context summarization, improving
response accuracy by 43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highly scalable NLP and generative AI pipelines in Python with model monitoring and drift tracking, reducing
processing latency by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Engineer Wabash Valley
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, KPI Reporting, Data Validation, Data Cleaning, Anomaly Detection,
ETL, Predictive Analytics, Natural Language Processing, Generative AI, Machine Learning, Time Series Forecasting, ARIMA/SARIMA
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development of cross-platform system integrating IoT sensor data for 100+ users, enabling scalable data ingestion
and predictive analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developed backend workflows for real-time, fault-tolerant processing of time-series sensor data, enabling reliable monitoring and predictive
analytics at scale
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highly scalable natural language processing pipelines in Python to analyze and classify high-volume text datasets,
reducing latency by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Developed technical documentation and reports to communicate AI system findings and workflows to both technical and non-technical
stakeholders
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable Generative AI and RAG system using FastAPI, PostgreSQL, and vector embeddings for production AI-driven
knowledge retrieval
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure, trends, and performance issues
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, applyingSQL,DAX, and
statistical analysisto surface KPI trends and support cross-functional business decision-making
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed time-series demand data across categories and locations to identify trends, seasonal patterns, and key variables driving consumption
forecasting decisions
•Built and evaluated time-series forecasting models including ARIMA, SARIMA, and regression to predict demand patterns and improve load
forecast accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts""",

    """TAILORED RESUME — Malhar Gudekar AI Engineer Whale rock capital management
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed production RAG and agentic AI systems using FastAPI, PostgreSQL, and vector embeddings, designing multi-step prompt
chains and configuring LLM assistants for end-user-facing AI applications
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved AI system performance by 64% through structured model evaluation, prompt optimization, and pipeline-level tuning, delivering
evidence-based recommendations for production deployment decisions
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design, development, and integration of AI backend system ingesting multi-source data for 100+ users, normalizing and
serving clean data to internal AI tools and downstream analytics pipelines
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python LLM pipeline with retrieval, context summarization, and automated workflow integration, improving response
accuracy by 43% and reducing manual processing steps
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developed production-grade REST APIs using FastAPI to serve AI models, implementing prompt engineering workflows,
security-aware data handling, monitoring, and deployment automation across distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure patterns and performance issues in distributed
systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 to scope and prioritize AI-driven product features, translating business requirements from non-technical
stakeholders into technical solutions and iterating based on performance insights
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution to ensure
on-time delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Engineer
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Machine Learning / Statistics:Classification, Regression, Feature Engineering, Model Evaluation, Precision, Recall, Accuracy, Statistical
Analysis, Predictive Analytics, Data Validation
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, Scikit-learn, LightGBM
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Designed and implemented end-to-end machine learning pipeline to analyze multi-dimensional behavioral data from 100+ users in a healthcare
context, applying feature engineering, statistical modeling, and model-ready transformations to surface actionable insights for downstream
product and research stakeholders
•Developed and optimizedPostgreSQLdata models, indexing strategies, and query execution plans for high-volume datasets, improving query
performance by38%while enabling efficient feature extraction for machine learning workflows
•Developed and implemented state-of-the-art AI retrieval and summarization model using embedding techniques, improving response accuracy
by 43% and enabling scalable, context-aware analysis of complex multi-dimensional datasets
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Developed, documented, and deployed NLP-based machine learning models in Python to classify and analyze large-scale text datasets in
healthcare research contexts, applying advanced statistical preprocessing and feature extraction to reduce processing latency by 41% and
improve classification accuracy
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade inferenceAPIsand deployment workflows to support reproducibility, monitoring, and consistent evaluation of
machine learning outputs
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Built and deployed production Retrieval-Augmented Generation (RAG) system using state-of-the-art embedding techniques and vector search,
combining data pipeline design, feature engineering, and retrieval optimization, then presented findings and system performance to stakeholders
to inform product development decisions, improving retrieval efficiency by 64%
•Maintained technical documentation for data models, ML pipeline architecture, and algorithm logic, establishing clear standards for repro-
ducibility and enabling cross-functional engineering and product teams to build on existing work
•Optimized indexing strategies and data processing workflows to enable low-latency querying and scalable deployment of AI-driven systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Analyzed large-scale operational datasets usingPythonandPySparkto identify trends, anomalies, and performance issues, combining
exploratory analysis and root cause investigation to support data-driven decision-making
•BuiltPower BIdashboards to track key performance indicators in operational performance, reducing reporting time by 40%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst
•Developed and maintained data models and visualizations for enterprise clients across Sales, Finance, and Operations using SQL, DAX,
and Tableau, translating complex multi-dimensional datasets into clear, actionable insights and presenting findings to stakeholders across
organizational levels
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Led across-functionalteam of six to deliver and scale Deepcover game enhancements by leveraging user data, performance metrics, and
feedback analysis to drive feature prioritization and improve games outcomes
Projects
Scalable ML System for Customer Risk Prediction
•BuiltLightGBM-based machine learning model topredict customer credit riskfromtime-series transaction data, combining feature
engineering, classification modeling, and evaluation techniques to identify high-risk and low-risk segments
•Evaluated model performance using precision, recall, and accuracy metrics, designed a decision framework translating predictions into
actionable credit limit recommendations, and produced clear documentation and stakeholder-ready reports, findings and model logic""",

    """TAILORED RESUME — Malhar Gudekar AI Engineering ULTA Beauty
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, ETL Pipelines, Kafka, PySpark, LangChain, Prompt Engineering, OpenAI API, MLOps
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable multi-step agentic AI system with RAG, tool-use patterns, and LangChain orchestration using FastAPI, PostgreSQL,
and vector embeddings for production applications
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed clean, production-ready backend services enabling real-time AI model serving, participating in code reviews to maintain quality
and consistency across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python LLM pipeline with prompt engineering, retrieval, and context summarization, improving accuracy by 43%
•Developed asynchronous AI backend workflows with monitoring and CI/CD integration for real-time, fault-tolerant data processing with focus
on production reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Researched and evaluated emerging AI frameworks and tools, integrating relevant findings into team engineering workflows and technical
solution design
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Collaborated with cross-functional teams of engineers and designers to deliver AI-driven features for a consumer-facing product, using
engagement metrics and user feedback to guide decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
AI-Powered AR Virtual Try-On (Glossier)
View Project
•Conducted customer segmentation and behavioral analysis on beauty retail users, identifying high engagement trends among users aged 18–44
for AR-based product experiences
•Designed AI-assisted personalization concepts for virtual try-on workflows, mapping recommendation logic and user interaction flows to
improve engagement and conversion potential
•Developed strategic roadmap outlining AR integration, ROI projections, and KPIs including return reduction, session retention, and conversion
improvement across digital commerce channels""",

    """TAILORED RESUME — Malhar Gudekar AI Full Stack Engineer Edelman DXI
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed a full-stack RAG and agentic AI application with a React/TypeScript frontend (Tailwind CSS, shadcn/ui) and a Python/FastAPI
backend integrated with OpenAI APIs, using PostgreSQL via Supabase for authentication, vector storage, and real-time data access
•Designed and deployed serverless backend workflows on AWS Lambda and Vercel to process and index large document datasets for low-latency
AI retrieval, using prompt engineering and OpenAI embedding models to optimize context retrieval accuracy
•Improved system performance by 64% through optimized indexing and pipeline-level tuning, accelerating iteration cycles using AI-assisted
development tools including Cursor and Claude Code for debugging, refactoring, and test generation
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end development of a cross-platform AI application, React frontend, Python/FastAPI backend, PostgreSQL via Supabase,
ingesting wearable sensor data for 100+ users and exposing analytics dashboards and REST APIs for downstream product consumption
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready RAG pipeline using OpenAI APIs for retrieval, embedding, and context summarization, improving multi-turn response
accuracy by 43%, deployed on AWS with context window optimization and prompt engineering strategies for response reliability
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and deployed production-grade REST APIs using FastAPI and Supabase edge functions, serving AI models with JWT-based
authentication, input validation, and monitoring, containerized with Docker and deployed via GitHub Actions CI/CD on AWS
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AI Inter SEKO
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics, NLP, Text Classification, OCR
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, scikit-learn
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built Python pipeline for document parsing, text extraction, and summarization using NLP techniques, improving downstream analytical
accuracy by 43%
•Developed automated data workflows and exception alerting pipelines for real-time processing with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed NLP classification pipelines in Python to process and categorize high-volume text datasets, reducing processing latency
by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Performed anomaly detection and pattern analysis on large-scale data streams to surface exceptions and drive automated reporting workflows
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure, trends, and performance issues
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, applyingSQL,DAX, and
statistical analysisto surface KPI trends and support cross-functional business decision-making
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and benchmarked forecasting models including ARIMA, SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar AI ML Engineer Hashlit
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, ETL Pipelines, Kafka, PySpark, scikit-learn, PyTorch, MLflow, pytest
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git, CI/CD
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based agentic AI system combining LLMs with RAG using FastAPI, PostgreSQL, and vector
embeddings for production applications
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python generative AI pipeline with retrieval, summarization, and MLflow experiment tracking, improving response
accuracy by 43%
•Designed feature engineering and model training workflows for time-series health data, enabling reliable downstream inference and reusable
ML components
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developed production-grade REST APIs using FastAPI to serve AI models, implementing validation, monitoring, and CI/CD
workflows to ensure reproducible, testable, and scalable deployment
•Built reusable ML pipeline components for data ingestion and transformation, enabling shared framework adoption across distributed engi-
neering systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactive dashboards and internal tooling for logistics and mobility KPIs in an industrial engineering environment, reducing reporting
time by 40%
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failures and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built end-to-end ML system using Python, scikit-learn, and LightGBM to train, evaluate, and deploy credit risk models from large-scale
time-series transaction data, covering feature engineering through inference
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision""",

    """TAILORED RESUME — Malhar Gudekar AI Platform Engineer Partstown
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker, GCP, BigQuery, dbt, Terraform
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintained scalable GCP and AWS data pipelines to ingest high-volume data for 100+ users, enabling cloud-based distributed storage
and downstream analytics consumption
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented workflow orchestration using Airflow and AWS Step Functions for streaming pipelines, adding data quality checks, logging,
retries, and failure handling to ensure reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets in distributed environments, reducing
processing latency by41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applied governance standards and data quality frameworks to ensure consistent data availability across distributed systems and downstream
applications
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable data APIs and integration services using FastAPI and PostgreSQL, enabling clean data flow to analytics and
AI-driven downstream applications
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
•Developed backend services and applied infrastructure-as-code practices with CI/CD workflows to enable reliable, repeatable deployment
across distributed and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built data pipelines and semantic layer integrations feeding BI dashboards for logistics KPIs, reducing reporting time by 40% and enabling
data-driven decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 to deliver platform improvements, articulating technical decisions to both technical and non-technical stakeholders
across functions
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar AI application Dev Circle Logistic
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed production RAG and agentic AI application integrating LLM APIs, FastAPI, PostgreSQL, and vector embeddings, shipping
working AI features used in live operational workflows
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed AI application backend with prompt engineering, real-time LLM serving, and iterative output refinement to improve reliability and
accuracy across distributed operational workflows
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built and iteratively refined production Python RAG pipeline with prompt tuning and context summarization — improving AI response
accuracy by 43% through systematic testing and evaluation cycles
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built operational dashboards for logistics and mobility KPIs, reducing reporting time by 40% and improving real-time visibility for carrier and
operations teams
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar AML Transaction Analyst Google
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built Python LLM pipeline with prompt refinement and context summarization for behavioral classification, improving output accuracy
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Deployed scalable NLP pipelines in Python to detect anomalous patterns across financial datasets, reducing processing latency by 41%
•Built distributed real-time ingestion pipelines using Kafka and Neo4j to enable high-throughput processing and detection of suspicious activity
patterns across data streams
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built AI agent using RAG and LLM prompt refinement to identify and classify risk patterns from unstructured datasets for compliance analytics
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactive Tableau and Power BI dashboards to track operational KPIs and compliance metrics, automating reporting workflows and
reducing report preparation time by 40%
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure, trends, and performance issues
•Wrote and optimized SQL queries to extract, clean, and analyze transaction-level data, detecting anomalies and data quality issues to accelerate
root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintained 20+ compliance and operations dashboards using SQL and DAX to support regulatory KPI tracking and data-driven
decision-making across Sales, Finance, and Operations
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
decisionsBuilt end-to-end ML system using Python, Pandas, and LightGBM to detect financial crime risk and monitor suspicious transaction
patterns from large-scale time-series data
•Designed ETL and feature engineering pipelines to capture transactional behavioral trends and temporal spending patterns, improving AML
model performance
•Built risk threshold tuning framework to govern model outputs, improving detection precision by 20% and enabling risk-aware transaction""",

    """TAILORED RESUME — Malhar Gudekar Analytics Engineer OCLC
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, enabling distributed storage in
S3and downstream analytics consumption
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented workflow orchestration and deployment pipelines using AWS Step Functions, applying data quality checks, logging, retries, and
failure handling — supporting reliable, continuous delivery of scalable data solutions
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets in distributed environments, reducing
processing latency by41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable data pipelines and RESTful APIs integrating AI tools and retrieval systems into the software development workflow,
supporting large-scale analytics and downstream applications using FastAPI and PostgreSQL
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
availability
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintained modular SQL-based data pipelines and reusable data warehouse models supporting Power BI dashboards, applying
complex joins, aggregations, and transformation logic to deliver consistent, analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers to deliver data-driven improvements, analytics insights, and system tracking
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Analytics Engineer Together AI
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, enabling distributed storage in
S3and downstream analytics consumption
•Designed and optimized dimensional data models, star schemas and SCD Type 2 slowly changing dimensions in PostgreSQL and Snowflake,
applying partitioning and indexing strategies to improve analytical query performance by 38% across high-volume production workloads
•Orchestrated data transformation workflows using Airflow DAGs and modular dbt models, implementing data quality checks, freshness
assertions, null checks, referential integrity along with retry logic and alerting to ensure pipeline reliability and SLA compliance
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable ELT pipelines in Python and dbt following a bronze/silver/gold medallion architecture, structuring raw,
cleansed, and curated layers for high-volume social media datasets, reducing processing latency by 41% in distributed environments
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalabledata processing pipelinesusingFastAPI,PostgreSQL, and optimized storage layers to support large-scale
analytics and downstream applications
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•Developed SQL-based data quality checks covering null validation, referential integrity, and distribution drift to reconcile multi-source
operational datasets, improving data accuracy and accelerating root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers to deliver data-driven improvements, analytics insights, and system tracking
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built an end-to-end analytics pipeline using Python, Pandas, and dbt-style modular transformations to process large-scale time-series transaction
data, structuring ingestion, transformation, and feature layers to produce analytics-ready datasets with documented lineage and quality checks
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Analytics Terraform powers
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, enabling distributed storage in
S3and downstream analytics consumption
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented workflow orchestration using AWS Step Functions for streaming pipelines, adding automated alerting, data quality checks,
logging, error handling, and retries to ensure reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable ELT pipelines in Python for high-volume datasets, implementing error handling, schema validation, and data
quality monitoring, reducing latency by 41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable data processing pipelines with vendor API integrations using FastAPI, PostgreSQL, and optimized storage,
supporting schema management and downstream analytics
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
availability
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers to deliver data-driven improvements, analytics insights, and system tracking
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Associate Consultant Data Engineer PremiumIQ
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, enabling distributed storage in
S3and downstream analytics consumption
•Designed and optimized SQL-based data models, warehouse tables, and data lake schemas in PostgreSQL, applying indexing and query tuning
to improve performance by 38% for large datasets
•Implementedworkflow orchestration using AWS Step Functionsand monitoring for real-time streaming pipelines, adding data quality
checks, logging, retries, and failure handling to ensure reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets in distributed environments, reducing
processing latency by41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applied distributed data processing and data governance principles to handle large-scale streaming data, ensuring data availability, consistency,
and quality across pipelines using Airflow-based orchestration
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalabledata processing pipelinesusingFastAPI,PostgreSQL, and optimized storage layers to support large-scale
analytics and downstream applications
•Designed fault-tolerant ETL workflows for ingesting and transforming high-volume document datasets from multiple sources, ensuring data
quality, consistency, and documented system and data definitions
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•Developed SQL queries to collect, cleanse, validate, and reconcile operational data from multiple sources, improving data governance and
accuracy while accelerating root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintained SQL-based data pipelines supporting Power BI dashboards, designing data warehouse models and enforcing data
governance standards to ensure consistent, analytics-ready delivery across client business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6, collaborating with stakeholders to deliver data-driven analytics insights and preparing clear visualizations and
presentations to communicate findings and support decisions
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Associate Software Dev Morningstar
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git, Prompt Engineering, AWS Bedrock, AWS Lambda,
AWS API Gateway, GitHub Copilot
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable RAG system with structured content indexing and vector embeddings using FastAPI and PostgreSQL, enabling
AI-assisted content discovery and retrieval in production
•Designed efficient, fault-tolerant ETL and event-driven async pipelines to process and index structured document datasets for low-latency
AI-assisted retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python generative AI pipeline with prompt engineering, retrieval, and context summarization, improving response
accuracy by 43%
•Developed serverless backend workflows using AWS Lambda for real-time, fault-tolerant event-driven data processing with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developed production-grade REST APIs using FastAPI and AWS API Gateway to serve AI models, implementing validation,
monitoring, and deployment automation across distributed systems
•Experimented with AI-assisted development tools and prompt optimization techniques to engineer workflows and improve system efficiency
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built end-to-end ML system using Python, Pandas, and LightGBM to assess credit risk from time-series transaction data, covering data
preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar Business Analyst Oak points partners
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues
•Developed SQL queries to map operational dependencies, analyze business processes, and detect data quality issues, accelerating root-cause
analysis and identifying efficiency improvements by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained 20+ dashboards across Sales, Finance, and Operations using SQL and DAX, documenting processes and surfacing
data-driven insights to identify revenue opportunities for enterprise clients
•Automated recurring Excel and SharePoint reporting workflows using VBA, documenting process improvements and implementing validation
logic, reducing report preparation time by 42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 to deliver product updates, presenting performance insights and actionable recommendations to stakeholders
using data-driven analysis and structured goal-setting
•Tracked sprint milestones and QA issues through Agile JIRA workflows, performing user acceptance testing on new features and maintaining
process documentation to ensure on-time delivery
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable business insights on promotions, pricing, and stock behavior, identifying revenue opportunities and enabling better inventory
planning to reduce operational risk""",

    """TAILORED RESUME — Malhar Gudekar Business Intelligence Engineer Ascot Group
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization, SQL Server, Power BI
Service, Power BI Desktop, Star Schema Modeling, SSMS
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP, Azure Data Factory
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Designed and maintained relational data models and ingestion workflows for a cross-platform system tracking 100+ users, enabling structured
reporting and downstream analytics consumption
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Supported development of Power BI reporting solutions by designing ETL workflows to extract and transform data from multiple enterprise
sources into structured, analytics-ready datasets
•Documented data models, naming conventions, and pipeline logic to align reporting outputs with source system definitions and support
long-term report maintainability
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure, trends, and performance issues
•Wrote and optimized SQL queries against relational databases to extract, validate, and reconcile operational data from enterprise sources,
resolving data quality issues and speeding root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained 20+ Power BI reports and dashboards for enterprise clients across Sales, Finance, and Operations, building semantic
models with DAX measures, calculated columns, and table relationships to enable KPI tracking across business units
•Validated and reconciled reporting data across enterprise datasets using SQL and Excel, standardizing definitions and following documentation
practices that cut report preparation time by 42% and improved consistency across weekly cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts""",

    """TAILORED RESUME — Malhar Gudekar Business Operational Analyst
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developed automated data workflows to validate and process longitudinal health datasets, maintaining data accuracy and supporting reliable
reporting for operational decision-making
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactive Power BI and Looker Studio dashboards for logistics KPIs, reducing reporting time by 40% and improving executive visibility
into operational performance across business units
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained 20+ dashboards across Sales, Finance, and Operations using SQL, DAX, and Google Workspace tools to support
KPI tracking, financial reporting, and cross-functional decision-making
•Automated recurring Excel and Google Sheets workflows using VBA and AI tools, implementing validation and scheduling logic, reducing
report preparation time by 42% and improving financial data consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 to track feature milestones and roadmaps, using AI tools like ChatGPT and GitHub Copilot to accelerate delivery
documentation and performance reporting
•Tracked sprint milestones, delivery metrics, and QA compliance through JIRA and SharePoint workflows, maintaining source-of-truth
documentation and ensuring on-time delivery across releases
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Business Technology Consultants Alined Consulting
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintained AWS data pipelines across EC2, S3, and VPC-secured network environments to ingest high-volume data for 100+ users,
enabling scalable distributed storage and downstream analytics
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented workflow orchestration using AWS Step Functions with CloudWatch monitoring, configuring IAM roles with least-privilege
access and network security controls to ensure reliable and secure pipeline operation
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets in distributed environments, reducing
processing latency by41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalabledata processing pipelinesusingFastAPI,PostgreSQL, and optimized storage layers to support large-scale
analytics and downstream applications
•Designed fault-tolerant ETL workflows with documented runbooks for ingesting and transforming high-volume datasets, ensuring low-latency
data availability and clear operational handoffs
•Developed backend services using Git-based CI/CD workflows, monitoring system health with CloudWatch dashboards and responding to
incidents to maintain uptime and meet SLA requirements
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Wrote Python and Bash scripts to automate data processing, log parsing, and system health checks, reducing manual operational toil and
improving performance monitoring visibility
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers to deliver data-driven improvements, analytics insights, and system tracking
•Managed Agile workflows using JIRA, documenting issues, resolutions, and runbooks clearly to support incident tracking, sprint progress, and
cross-team handoffs during delivery cycles
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Cover Letter GAI
Dear Hiring Team,
I am excited to apply for the Data Analyst Intern position at Gabriel AI. As a Master of Science in
Information Management student at the University of Illinois Urbana-Champaign with professional
experience in data analytics, dashboard development, SQL, and data pipeline validation, I am eager to
contribute to your mission of using data-driven insights to improve customer onboarding and product
growth.
In my recent Data Analyst roles, I built interactive dashboards in Power BI and Looker Studio, segmented
performance metrics by user cohorts and acquisition sources, and developed SQL-based validation
processes to identify tracking gaps and improve data quality. At Swift Mobil Software Solutions, I created
dashboards that improved visibility into operational KPIs while reducing reporting effort by 40%. I also
leveraged Python, SQL, and large-scale datasets to uncover trends, detect anomalies, and support data-
driven decision making.
Beyond analytics, my research work at the University of Illinois has strengthened my ability to work with
complex data pipelines and production systems. I have designed PostgreSQL architectures, developed
scalable Python-based data workflows, and collaborated with cross-functional teams to ensure reliable data
collection and analysis. These experiences have given me a strong understanding of data integrity, event
tracking, API-generated data, and the importance of building trustworthy reporting systems.
What particularly excites me about Gabriel AI is the opportunity to measure and optimize a real-world AI-
powered customer journey. I enjoy asking "why" behind the numbers, translating ambiguous business
questions into structured analyses, and communicating insights that drive action. The chance to work
closely with Growth, Product, and Engineering teams in a startup environment is exactly the kind of high-
impact experience I am seeking.
I am confident that my background in SQL, Python, dashboard development, KPI reporting, and analytical
problem solving would allow me to contribute quickly to Gabriel AI's onboarding analytics initiatives. I
would welcome the opportunity to discuss how my skills and experiences can support your team.
Thank you for your time and consideration. I look forward to hearing from you.
Sincerely,
Malhar Gudekar M.S. Information Management University of Illinois Urbana-Champaign
1""",

    """TAILORED RESUME — Malhar Gudekar Cover Letter bri
Dear Hiring Committee,
I am excited to apply for the Research Assistant position in Signal Processing and Machine Learning at
Brigham and Women's Hospital and Harvard Medical School. I am currently pursuing a Master of Science in
Information Management at the University of Illinois Urbana-Champaign, where I conduct research
involving machine learning, time-series analysis, and large-scale health-related datasets. The opportunity to
develop AI solutions that directly improve maternal health outcomes is particularly motivating to me
because it combines rigorous research with meaningful real-world impact.
In my current role as a Research Assistant at the University of Illinois, I design and implement machine
learning pipelines for wearable sensor data collected from over 100 users. This work requires processing
noisy physiological time-series data, handling missing values and irregular sampling, engineering
meaningful features, and developing models that support longitudinal behavioral analysis. I have built
Python-based workflows using NumPy, SciPy, PyTorch, and related tools to transform complex real-world
datasets into reliable and reproducible analyses.
My research experience has also involved developing scalable data pipelines, performing signal
preprocessing and pattern detection on large time-series datasets, and building production-ready machine
learning systems. Through these projects, I have gained extensive experience working with imperfect data,
identifying artifacts, validating results, and evaluating model performance using rigorous analytical
methods. I am particularly interested in applying these skills to physiological waveform data and clinical
machine learning applications.
Beyond technical expertise, I enjoy working in multidisciplinary environments where researchers,
engineers, and domain experts collaborate to solve challenging problems. My experiences in both academic
research and industry have strengthened my ability to communicate technical findings clearly, take
ownership of projects, and quickly learn new methodologies when needed.
The combination of cutting-edge machine learning research, clinical impact, and close collaboration with
leading researchers across Harvard Medical School, Mass General Brigham, and the Broad Institute makes
this opportunity especially exciting. I would welcome the chance to contribute my experience in machine
learning, time-series modeling, and data-driven research to your team.
Thank you for your time and consideration. I look forward to the opportunity to discuss my background and
learn more about your research initiatives.
Sincerely,
Malhar Gudekar Master of Science in Information Management University of Illinois Urbana-Champaign
1""",

    """TAILORED RESUME — Malhar Gudekar Cover Letter
Malhar Gudekar
malhargudekar@gmail.com  |  University of Illinois Urbana-Champaign
________________________________________________________________
May 11, 2026
Hiring Committee
Data Scientist, Student Affairs Analytics and AI
Virginia Tech
Dear Hiring Committee,
I am writing to apply for the Data Scientist position within Virginia Tech's Student Affairs division. As
a graduate researcher at the University of Illinois Urbana-Champaign, I spent two years building
data pipelines, ML models, and analytics systems in a university research environment, making this
role a natural continuation of the work I care about most.
At UIUC's iSchool, I owned end-to-end design and deployment of a cross-platform system that
collected and analyzed behavioral and health data from 100+ research participants. I built the
ingestion architecture, optimized PostgreSQL data models for a 38% performance improvement,
and developed Python-based ML pipelines that improved analytical accuracy by 43%. At UIUC's
CHI AI Lab, I built NLP pipelines to process large-scale behavioral datasets and developed APIs to
surface insights for non-technical research stakeholders, reducing latency by 41%. These projects
map directly to your need for someone who can build and maintain the University DataCommons
analytics platform, develop predictive models, and translate findings into actionable insights for
Student Affairs teams.
I also bring experience building stakeholder-facing dashboards and visualizations that make
complex findings accessible to non-technical audiences, along with a deep understanding of the
rigor that research involving student behavioral and wellbeing data demands. Virginia Tech's
mission, Ut Prosim, resonates with me. I would welcome the chance to contribute to a team using
data to improve the lives of students.
Sincerely,
Malhar Gudekar
malhargudekar@gmail.com""",

    """TAILORED RESUME — Malhar Gudekar Cover letter whale rocl capital management
While building an advanced RAG system for a consulting client, I hit a retrieval quality 
problem where dense vector search alone was missing structurally important documents 
that keyword overlap would have caught. I implemented a hybrid retrieval layer combining 
pgVector semantic search with BM25 sparse retrieval, added a cross-encoder re-ranking step 
to score candidate chunks before passing context to the LLM, and introduced query 
decomposition to handle multi-part questions that were collapsing into a single ambiguous 
embedding. On the safety side, I built prompt injection detection at the input layer, enforced 
strict data isolation so proprietary client documents never mixed with public context, and 
added output validation guardrails to flag low-confidence or hallucinated responses before 
they reached the user. The system went from failing on roughly 30% of complex queries to 
handling them reliably, and the safety layer caught two injection attempts during internal 
testing.""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst Ascendion
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development of cross-platform data integration system for 100+ users on AWS, enabling scalable data ingestion,
extraction, and automated reporting
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient ETL and data migration pipelines to process, transform, and index large datasets, automating workflows to reduce manual
reporting overhead
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Automated analysis of large-scale operational datasets using Python and PySpark to extract, identify trends, anomalies, and performance issues,
combining root cause investigation with SQL-based reporting to support data-driven decision-making
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Performed data validation, cleaning, and migration across large multi-source datasets using SQL, improving data accuracy by 30% and reducing
reporting inconsistencies across sales, finance, and operations — directly supporting business and financial decision-making processes
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst Awarity
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Built Python-based NLP pipelines to analyze high-volume social media datasets, extracting audience behavioral signals and content trends,
reducing processing latency by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Processed and analyzed large-scale social media data streams to extract audience signals, content trends, and behavioral patterns for downstream
reporting and targeting insights
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) usingFastAPI,PostgreSQL, and vector embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Leveraged AI-driven automation and optimized indexing strategies to improve data processing performance by 64%, accelerating reporting
workflows in production environments
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Intern Mumbai, IN
•Built interactive Power BI dashboards to monitor performance KPIs and operational trends, reducing reporting time by 40% and delivering
actionable insights to stakeholders across business units
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure , trends, and performance issues
•Developed SQL queries to analyze performance data, detect data quality issues, and surface optimization opportunities, improving root-cause
analysis speed by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Intern Mumbai, IN
•Developed and maintained 20+ Power BI dashboards across Sales, Finance, and Operations using SQL and DAX to track campaign and
business KPIs, surface market trends, and support stakeholder decision-making
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Applied statistical forecasting methods including ARIMA, SARIMA, and regression analysis to evaluate market demand patterns and improve
forecast accuracy, validated using RMSE and MAPE
•Synthesized analytical findings into actionable recommendations on promotional strategy and pricing behavior, enabling more informed
planning decisions and reducing operational risk""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst Brillio
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end data pipeline integrating cross-platform wearable data for 100+ users, enabling scalable ingestion and downstream analytics
to surface behavioral health trends and patterns
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built Python data pipeline with automated retrieval and summarization to accelerate research analysis workflows, improving analytical accuracy
by 43% and reducing manual data review overhead
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based (RAG) system usingFastAPI,PostgreSQL, and vector embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets using Python and PySpark to surface failure patterns, trends, and performance insights,
translating findings into actionable recommendations for logistics and operations teams
•Developed SQL queries to map system dependencies, detect data quality issues, and deliver root-cause analysis findings to stakeholders 26%
faster, accelerating operational decision-making
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, applyingSQL,DAX, and
statistical analysisto surface KPI trends and support cross-functional business decision-making
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 engineers and designers, translating user feedback and performance data into prioritized, data-driven feature
decisions communicated clearly across stakeholders
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst Gabriel AI
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactive dashboards in Power BI and Looker Studio, segmenting performance data by user cohort and source, reducing reporting time
by 40% and improving operational visibility into KPIs
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues
•Developed SQL queries to audit data flows, validate data integrity, and detect tracking gaps and quality issues across operational datasets,
accelerating root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained 20+ dashboards in Power BI and Looker Studio across Sales, Finance, and Operations, using SQL to track KPIs,
funnel metrics, and deliver stakeholder performance reports
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6, analyzing user activation metrics, funnel performance, and segmented cohort data to guide A/B testing decisions
and data-driven feature prioritization
•Tracked delivery metrics and QA issues through JIRA workflows, documenting data definitions, metric calculations, and preparing weekly
performance summaries for stakeholder review
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and compared ARIMA, SARIMA, and regression models applying statistical hypothesis testing, confidence intervals, and significance
analysis to evaluate demand patterns and improve forecast accuracy
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst INCOG
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built and iteratively refined AI pipeline with retrieval and summarization, validating outputs for accuracy and improving response quality by
43% through systematic prompt tuning and testing
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Configured and deployed an enterprise AI retrieval system using RAG and vector embeddings, refining prompts, validating AI outputs for
business accuracy, and embedding intelligent data access into analytics workflows
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
•Developed SQL queries to detect data quality issues, validate accuracy and consistency across reporting assets, and resolve upstream data
problems, speeding root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, applyingSQL,DAX, and
statistical analysisto surface KPI trends and support cross-functional business decision-making
•Automated Excel-based reporting workflows using VBA with validation logic and runbook documentation, reducing report preparation time
by 42% and improving consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst Scale Jobs
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics, A/B Testing, Hypothesis Testing, Statistical Significance
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, matplotlib, seaborn
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built Python pipeline using pandas and matplotlib to process, visualize longitudinal behavioral datasets, improving analytical accuracy by 43%
•Conducted exploratory analysis on longitudinal behavioral datasets to surface trends and anomalies, presenting findings to stakeholders in
structured reports
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Built Python automation scripts using pandas to process and clean high-volume behavioral datasets, reducing analysis turnaround time by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Documented data sources, metric definitions, and analytical workflows to support team knowledge-sharing and ensure reproducibility across
reporting cycles
•Applied hypothesis testing and correlation analysis on social media behavioral data to surface statistically supported insights for stakeholders
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based (RAG) system usingFastAPI,PostgreSQL, and vector embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Analyzed large-scale transactional datasets using Python, pandas, and seaborn to identify failure patterns, surface anomalies, and visualize
performance trends
•Wrote SQL using window functions, aggregations, and subqueries to map dependencies, detect data quality issues, and speed root-cause
analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, applyingSQL,DAX, and
statistical analysisto surface KPI trends and support cross-functional business decision-making
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Designed A/B tests and applied hypothesis testing to compare ARIMA, SARIMA, and regression models, improving forecast accuracy measured
by RMSE and MAPE
•Translated findings into structured stakeholder presentations and written reports on promotions, pricing, and stock behavior to support inventory""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst Sunrise Systems
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.9/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built and iteratively refined AI pipeline with retrieval and summarization, validating outputs for accuracy and improving response quality by
43% through systematic prompt tuning and testing
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Configured and deployed an enterprise AI retrieval system using RAG and vector embeddings, refining prompts, validating AI outputs for
business accuracy, and embedding intelligent data access into analytics workflows
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
•Developed SQL queries to detect data quality issues, validate accuracy and consistency across reporting assets, and resolve upstream data
problems, speeding root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, applyingSQL,DAX, and
statistical analysisto surface KPI trends and support cross-functional business decision-making
•Automated Excel-based reporting workflows using VBA with validation logic and runbook documentation, reducing report preparation time
by 42% and improving consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst Supernova
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust Python-based data analysis and validation pipeline, implementing back-testing logic and accuracy benchmarking across multi-
source datasets, improving output accuracy by 43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based (RAG) system usingFastAPI,PostgreSQL, and vector embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
•Developed SQL queries to perform data analysis, comparison, and validation across operational datasets, detecting quality issues and anomalies,
speeding root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, applyingSQL,DAX, and
statistical analysisto surface KPI trends and support cross-functional business decision-making
•Automated and optimized complex Excel-based financial reporting workflows using VBA, implementing validation logic and scheduling,
reducing report preparation time by 42% across weekly cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
View Project
•Performed exploratory data analysis and feature engineering on large-scale financial transaction datasets to identify behavioral patterns,
spending trends, and risk signals for credit assessment
•Built and validated a multivariate regression and LightGBM model on time-series financial transaction data, performing back-testing and
comparative evaluation to improve credit risk prediction precision by 20%
•Developed a risk-based decision framework incorporating model outputs and threshold validation, translating financial data analysis into
actionable credit limit recommendations with measurable precision gains""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst TDI
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Managed end-to-end data collection and analytics pipeline for 100+ users, establishing data quality standards and enabling reliable downstream
reporting and analysis
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Analyzed large-scale data streams using statistical methods to surface behavioral trends, anomalies, and patterns for downstream reporting
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Intern Mumbai, IN
•Built interactive Power BI dashboards tracking operational and compliance KPIs, reducing reporting time by 40% and improving stakeholder
visibility into performance trends across business units
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure , trends, and performance issues
•Developed SQL queries to validate data integrity, analyze operational patterns, and detect data quality issues, improving root-cause analysis
speed by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Intern Mumbai, IN
•Developed and maintained 20+ Power BI dashboards across Sales, Finance, and Operations using SQL and DAX to support KPI reporting,
compliance tracking, and data-driven stakeholder decision-making
•Automated recurring Excel-based reporting workflows using VBA, implementing data validation and scheduling logic, reducing report
preparation time by 42% and improving data accuracy
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
decisions
•Applied statistical forecasting methods including ARIMA, SARIMA, and regression analysis to evaluate demand patterns and improve forecast
accuracy, validated using RMSE and MAPE
•Synthesized data findings into actionable recommendations for stakeholders on pricing, promotions, and stock behavior, reducing stockouts
and improving planning accuracy""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst Tech Consulting
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker, Apache Spark, Hadoop, Hive, NoSQL, Linux
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintained AWS-based scalable data pipelines using Apache Spark and distributed computing to ingest high-volume data for 100+
users, enabling S3 storage and downstream analytics
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented workflow orchestration using Airflow and AWS Step Functions for streaming pipelines, adding data quality checks, logging,
retries, and failure handling to ensure reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets in distributed environments, reducing
processing latency by41%
•Built distributed real-time ingestion pipelines using Kafka and Neo4j NoSQL graph database, enabling streaming data processing, transforma-
tion, and graph-based analytics at scale
•Applied Hadoop-based distributed processing and big data principles to monitor data quality, integrity, and system performance across
large-scale streaming environments
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalabledata processing pipelinesusingFastAPI,PostgreSQL, and optimized storage layers to support large-scale
analytics and downstream applications
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets using Python and Apache Spark distributed processing, implementing transformations and aggregations for
system performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Documented data workflows, pipeline architecture, and technical solutions to support cross-functional collaboration across engineering and
analytics teams
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst ccs
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactive Power BI and Tableau dashboards for logistics KPIs, reducing reporting time by 40% and improving stakeholder visibility into
operational performance across business units
•Collected, cleaned, and transformed large-scale operational datasets using Python and PySpark to identify failure patterns, trends, and
performance issues across business operations
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, applyingSQL,DAX, and
statistical analysisto surface KPI trends and support cross-functional business decision-making
•Developed automated data pipelines and reporting workflows using Excel and VBA, implementing validation and scheduling logic, reducing
report preparation time by 42% and improving data consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCG sales data across categories to identify trends, seasonal patterns, and key performance indicators, documenting analytical
methodologies and findings for stakeholder reference
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Data Analyst
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Intern Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure , trends, and performance issues
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Intern Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, applyingSQL,DAX, and
statistical analysisto surface KPI trends and support cross-functional business decision-making
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
decisions
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Data Engineer Bakertilly
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:Azure (ADF, Synapse, Data Lake), Databricks, Delta Lake, Microsoft Fabric, T-SQL, Azure DevOps, Terraform
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintained scalable data pipelines across Azure and AWS cloud environments, enabling distributed data storage and downstream
analytics consumption at scale
•Designed and optimized T-SQL data models and medallion-style warehouse layers in PostgreSQL, applying indexing and query tuning
techniques to improve performance by 38%
•Implemented ETL workflow orchestration using Azure Data Factory and AWS Step Functions, adding data quality checks, logging, retries, and
failure handling to ensure pipeline reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets in distributed environments, reducing
processing latency by41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applied Delta Lake and distributed data processing principles to manage large-scale streaming data, ensuring consistent data availability and
analytics-ready quality across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Designed and delivered scalable data engineering solutions for consulting clients, building pipelines using FastAPI, PostgreSQL, and optimized
storage layers for analytics and reporting
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
•Implemented CI/CD workflows using Azure DevOps and Git to enable reliable, automated deployment and real-time data querying across
distributed high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintained T-SQL data pipelines supporting Power BI dashboards and semantic models, designing dimensional warehouse models
and ensuring analytics-ready data delivery across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 to deliver data engineering solutions, documenting technical designs and communicating findings to both
technical and non-technical stakeholders
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Data Engineer Lightcast
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, enabling distributed storage in
S3and downstream analytics consumption
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented workflow orchestration using AWS Step Functions with data quality checks, logging, retries, and failure handling — continuously
monitoring pipeline health and resolving root causes of data issues to ensure reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets in distributed environments, reducing
processing latency by41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalabledata processing pipelinesusingFastAPI,PostgreSQL, and optimized storage layers to support large-scale
analytics and downstream applications
•Designed fault-tolerant ETL workflows for ingesting and transforming high-volume document datasets, implementing data validation checks
and error handling to ensure accuracy, consistency, and availability across systems
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers to deliver data-driven improvements, analytics insights, and system tracking
•Contributed to Agile Scrum workflows using JIRA, participating in sprint planning, development tasks, QA, and sprint reviews to ensure timely
delivery of reliable data solutions
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Data Engineer Qode
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintained AWS-based scalable data pipelines to ingest and combine high-volume data from multiple sources for 100+ users, enabling
distributed S3 storage and downstream analytics consumption
•Designed and optimized SQL-based data models and warehouse tables in PostgreSQL, applying indexing and query tuning to improve
performance by 38% and ensure data quality and reliability across large-scale datasets
•Implemented workflow orchestration using AWS Step Functions for real-time data acquisition and streaming pipelines, integrating data quality
checks, logging, retries, and failure handling to ensure reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable ELT pipelines in Python for high-volume datasets in distributed environments, applying data mining and
segmentation techniques to reduce processing latency by 41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalabledata processing pipelinesusingFastAPI,PostgreSQL, and optimized storage layers to support large-scale
analytics and downstream applications
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built and maintained SQL-based data pipelines supporting enterprise BI dashboards, designing data warehouse models and applying data
mining techniques to ensure delivery of analytics-ready datasets for Fortune 500 stakeholders
•Processed large-scale datasets using Python and PySpark, implementing transformations, aggregations, and statistical analysis to interpret
trends and patterns in operational performance data
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Scientist Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Consolidated and analyzed 500+ user feedback signals and gameplay telemetry records, creating structured datasets that accelerated feature
prioritization by 35%
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built an end-to-end data pipeline using Python, Pandas, and LightGBM to prepare large-scale time-series transaction data for prescriptive and
predictive modeling, including ingestion, transformation, and feature engineering
•Designed and implemented scalable ETL pipelines and prototype algorithms for large datasets, capturing behavioral trends and temporal
patterns such as rolling averages and spending frequency to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Data Engineer Revature
Malhar Gudekar
(217) 766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana-ChampaignAug 2024 – May 2026
M.S., Information Management GPA: 3.8/4.0
Coursework: Web Programming, Machine Learning & Cloud, Information Management, Methods of Data Science
University of Mumbai Jun 2019 – May 2023
B.E., Computer Science GPA: 9.25/10
Coursework: Data Structures & Algorithms, Machine Learning, NLP , Operating Systems, OOP
Skills
Languages:Python, SQL, Java, C++
Data Engineering & MDM:ETL/ELT Pipelines, Data Modeling, Semantic Layers, Batch and Streaming Pipelines, Data Quality Rules,
Snowflake, PySpark, Airflow, AWS Glue, Step Functions
Analytics & Reporting:Power BI, Dashboards and Scorecards, KPI Monitoring, Self-Serve Analytics, Automated Reporting
Cloud & DevOps:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD Pipelines, Docker, Automated Testing
Work Experience
University of Illinois Urbana-ChampaignMay 2025 – Present
Research Assistant – iSchool Champaign, IL
•Developed and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, implementingETL
workflowswith data quality checks, validation rules, and monitoring to ensure reliable downstream analytics
•Designed and optimizedSQL-based data models and warehouse schemasin PostgreSQL, applying indexing, query tuning, and data
modeling best practices, improving analytical query performance by38%across large datasets
•Implementedworkflow orchestration using AWS Step Functionsfor real-time and batch pipelines; integrated logging, retries, and observ-
ability signals to support consistent data availability and platform reliability
Research Assistant – CHI AI in Infodemic ManagementJan 2025 – May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets, reducing processing latency by41%;
appliedautomated testingand CI/CD practices to ensure data integrity across pipeline stages
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data transformation and graph-based analytics to
support unified views of large-scale datasets
•Identified and resolved data quality issues using targeted validation rules, process controls, and analytical reporting on pipeline health and
data consistency
Business Intelligence Group Aug 2025 – Dec 2025
Technical Consultant Champaign, IL
•Built and deployedscalable ETL/ELT data pipelinesusingPython, FastAPI, and PostgreSQL to ingest, transform, and structure high-volume
datasets for analytics and business decision-making
•Developeddashboards and KPI monitoring systemsto define and track product and operational metrics, enabling teams to understand
performance and usage trends
•ImplementedCI/CD pipelinesand automated testing frameworks to validate data pipelines and ensure reliability, consistency, and maintain-
ability across environments
Swift Mobil Software Solutions ProviderJul 2023 – Oct 2023
Data Analyst Mumbai, IN
•Builtdata pipelines feeding Power BI dashboardsfor logistics KPIs and scorecards, reducing reporting time by40%and improving visibility
into operational performance
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations aligned with performance
monitoring and analytics requirements
•Developed complexSQL queriesto validate, reconcile, and analyze operational data, improving data quality and supporting faster root-cause
analysis by26%
Pscope Technologies Pvt. Ltd. Jan 2023 – Jun 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelines supporting Power BI dashboards, designing warehouse models and delivering analytics-
ready datasets with enforceddata quality rules
•Automateddata transformation workflowsusing VBA with validation checks, error handling, and scheduling logic, improving processing
efficiency and reducing reporting time by42%
Stu/Dio at Illinois Aug 2025 – Present
Project Manager Champaign, IL
•Led cross-functional team of 6 engineers delivering data-driven improvements and system tracking; managedAgile workflowsand ensured
timely delivery of analytics and platform features
Projects
Scalable ML System for Customer Risk PredictionMar 2025|UIUC Hackathon
•Built anend-to-end ETL data pipelineusing Python, Pandas, and LightGBM to ingest, transform, and enrich large-scale time-series
transaction data—incorporatingdata quality checksand feature engineering for model integration
•Designedscalable feature engineering pipelinescapturing behavioral trends and temporal patterns, producing consistent and accurate
analysis of key risk metrics and performance indicators
•Developed adata-driven decision frameworkwith automated risk thresholds and pipeline outputs, improving prediction precision by20%
and enabling scalable analytics workflows with low-touch reporting""",

    """TAILORED RESUME — Malhar Gudekar Data Engineer Target
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintained cloud-based scalable data pipelines on AWS and GCP to ingest high-volume data for 100+ users, enabling distributed
cloud storage and downstream analytics consumption in BigQuery-compatible formats
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented pipeline workflow orchestration using Airflow-compatible patterns and AWS Step Functions, adding data quality checks, moni-
toring, and failure handling to ensure streaming and batch pipeline reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable ELT pipelines in Python and PySpark for high-volume datasets across distributed cloud environments,
supporting both batch and real-time processing with 41% latency reduction
•Built distributed real-time ingestion pipelines using Kafka and event streaming technologies for high-throughput data processing, transformation,
and enterprise-scale analytics
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable data processing pipelines using Python, PostgreSQL, and optimized data lake storage layers to support large-scale
analytics, reporting, and downstream machine learning applications
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
•Developed data platform services and implemented Git-based CI/CD workflows with infrastructure-as-code patterns to enable automated,
reliable deployment across distributed, high-availability data environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Scientist Mumbai, IN
•Built and maintained SQL-based data pipelines and data warehouse models, implementing data quality checks and governance controls to
ensure delivery of accurate, analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Consolidated and analyzed 500+ user feedback signals and gameplay telemetry records, creating structured datasets that accelerated feature
prioritization by 35%
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built an end-to-end data pipeline using Python, PySpark, and LightGBM to process large-scale time-series transaction data, supporting machine
learning workflows through scalable ingestion, transformation, and feature engineering
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Data Engineer UST
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintained scalable data pipelines across AWS and Azure Data Lake to ingest high-volume wearable data for 100+ users, enabling
distributed storage and downstream analytics consumption
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented workflow orchestration and pipeline monitoring using AWS Step Functions, supporting data quality checks, incident triage,
logging, retries, and failure handling to ensure production reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable ELT pipelines in Python and Databricks with dbt-based transformation logic for high-volume social media
datasets, reducing processing latency by 41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalabledata processing pipelinesusingFastAPI,PostgreSQL, and optimized storage layers to support large-scale
analytics and downstream applications
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
availability
•Developed backend services using Git-based CI/CD workflows, leveraging AI-assisted development tools including Claude and GitHub Copilot
to accelerate coding, debugging, and deployment across distributed environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets using Python, PySpark, and Databricks, implementing transformations and aggregations within Agile sprint
cycles to deliver reliable performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintained SQL-based data pipelines in Snowflake supporting Power BI dashboards, designing data warehouse models with complex
joins and aggregations to ensure analytics-ready delivery across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers to deliver data-driven improvements, analytics insights, and system tracking
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Data Science Machine Learning Hackajob
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Machine Learning / Statistics:Classification, Regression, Feature Engineering, Model Evaluation, Precision, Recall, Accuracy, Statistical
Analysis, Predictive Analytics, Data Validation
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, Scikit-learn, LightGBM
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Designed and implemented end-to-end ML pipeline to collect, process, and analyze sensor and wearable data from 100+ users, applying
signal-level feature engineering and behavioral pattern extraction to enable longitudinal predictive analytics and data-driven insights
•Developed and optimizedPostgreSQLdata models, indexing strategies, and query execution plans for high-volume datasets, improving query
performance by38%while enabling efficient feature extraction for machine learning workflows
•Built embedding-based retrieval and summarization pipeline to enhance contextual understanding of user interactions, improving multi-turn
response accuracy by 43% and supporting more reliable behavioral analysis
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Developed and validated NLP-based supervised ML pipelines to classify behavioral patterns from large-scale unstructured data, applying text
preprocessing and feature extraction to reduce processing latency by 41% and improve model reliability for production use
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade inferenceAPIsand deployment workflows to support reproducibility, monitoring, and consistent evaluation of
machine learning outputs
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Built and deployedRetrieval-Augmented Generation(RAG) system using embeddings andvector search, combining data pipelines, feature
engineering, and retrieval optimization to improve document retrieval efficiency by 64%
•Designed scalableETLand feature pipelines usingFastAPIandPostgreSQLto transform unstructured data into structured formats suitable
for analytics and machine learning use cases
•Optimized indexing strategies and data processing workflows to enable low-latency querying and scalable deployment of AI-driven systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Analyzed large-scale transportation and mobility datasets using Python and PySpark, applying EDA and anomaly detection to identify
operational trends and performance issues, translating findings into data-driven recommendations for business decision-making
•BuiltPower BIdashboards to track key performance indicators and improve visibility into operational performance, reducing reporting time
by 40%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst
•Developed and maintained Power BI dashboards usingSQLandDAX, transforming raw data into actionable insights for business decision-
making across multiple domains.
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Led across-functionalteam of six to deliver and scale Deepcover game enhancements by leveraging user data, performance metrics, and
feedback analysis to drive feature prioritization and improve games outcomes
Projects
Scalable ML System for Customer Risk Prediction
•Built and validated a supervised LightGBM classification model on large-scale real-world tabular data to predict customer credit risk, applying
feature engineering, cross-validation, and precision/recall evaluation to identify risk segments and drive actionable business decisions
•Performed feature engineering on behavioral patterns such as transaction frequency and spending trends, improvingmodel precisionby 20%
while enhancing robustness and interpretability.
•Evaluatedmodel performanceusing precision, recall, and accuracy, and designed a decision framework to translate predictions into actionable
credit limit recommendations.""",

    """TAILORED RESUME — Malhar Gudekar Data Scientist Caterpillar
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Machine Learning / Statistics:Classification, Regression, Feature Engineering, Model Evaluation, Precision, Recall, Accuracy, Statistical
Analysis, Predictive Analytics, Data Validation
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, Scikit-learn, LightGBM
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Designed and implemented end-to-end machine learning pipeline to ingest, process, and analyze sensor data from 100+ connected assets, com-
bining scalable data ingestion, feature engineering, and model-ready transformations to enable predictive operational insights and downstream
analytics
•Developed and optimized scalable data models and query execution plans across cloud and relational database environments, improving query
performance by 38% while enabling efficient feature extraction for machine learning workflows
•Built embedding-based retrieval and summarization pipeline to enhance contextual understanding of user interactions, improving multi-turn
response accuracy by 43% and supporting more reliable behavioral analysis
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Developed NLP and text analytics pipelines in Python to extract structured signals from large-scale unstructured data, applying text prepro-
cessing, feature extraction, and model optimization to reduce processing latency by 41%
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade inferenceAPIsand deployment workflows to support reproducibility, monitoring, and consistent evaluation of
machine learning outputs
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Built and deployedRetrieval-Augmented Generation(RAG) system using embeddings andvector search, combining data pipelines, feature
engineering, and retrieval optimization to improve document retrieval efficiency by 64%
•Designed scalableETLand feature pipelines usingFastAPIandPostgreSQLto transform unstructured data into structured formats suitable
for analytics and machine learning use cases
•Optimized indexing strategies and data processing workflows to enable low-latency querying and scalable deployment of AI-driven systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Analyzed large-scale logistics and operational datasets using Python and PySpark to identify trends, anomalies, and performance issues,
applying exploratory analysis and root cause investigation to support supply chain decision-making
•Built Power BI dashboards to track key performance indicators and present operational insights to leadership, reducing reporting time by 40%
and enabling data-driven business decisions
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Scientist
•Developed and maintained Power BI dashboards usingSQLandDAX, transforming raw data into actionable insights for business decision-
making across multiple domains.
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Applied AI-assisted analysis to 10000+ player feedback records and behavioral datasets, identifying patterns that accelerated feature prioriti-
zation by 35%
Projects
Scalable ML System for Customer Risk Prediction
•Built LightGBM-based machine learning model to forecast outcomes from time-series transaction data, combining feature engineering,
classification modeling, and business statistics techniques to identify and segment high-risk and low-risk patterns
•Performed feature engineering on behavioral patterns such as transaction frequency and spending trends, improvingmodel precisionby 20%
while enhancing robustness and interpretability
•Evaluated model performance using precision, recall, and accuracy, and designed a decision framework to translate analytical predictions into
actionable business recommendations for stakeholders""",

    """TAILORED RESUME — Malhar Gudekar Data Scientist Consultant Delloite
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Machine Learning / Statistics:Classification, Logistic Regression, Clustering, Unsupervised Learning, Feature Engineering, Model Evalua-
tion, Exploratory Data Analysis, Predictive Analytics, Data Validation
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, Scikit-learn, LightGBM
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Translated longitudinal behavioral research goals into end-to-end ML pipeline design for 100+ users, combining exploratory data analysis,
feature engineering, and model-ready transformations to enable actionable insights and downstream analytics
•Developed and optimizedPostgreSQLdata models, indexing strategies, and query execution plans for high-volume datasets, improving query
performance by38%while enabling efficient feature extraction for machine learning workflows
•Built embedding-based retrieval and summarization pipeline to enhance contextual understanding of user interactions, improving multi-turn
response accuracy by 43% and supporting more reliable behavioral analysis
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Developed NLP classification and clustering pipelines to detect health misinformation from large-scale social media data, applying feature
extraction, sampling techniques, and optimization to reduce processing latency by 41%
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade inferenceAPIsand deployment workflows to support reproducibility, monitoring, and consistent evaluation of
machine learning outputs
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Developed proof-of-concept and deployed LLM-based Retrieval-Augmented Generation (RAG) system using embeddings and vector search,
combining feature pipelines and retrieval optimization to improve document retrieval efficiency by 64%
•Designed scalableETLand feature pipelines usingFastAPIandPostgreSQLto transform unstructured data into structured formats suitable
for analytics and machine learning use cases
•Optimized indexing strategies and data processing workflows to enable low-latency querying and scalable deployment of AI-driven systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Analyzed large-scale operational datasets usingPythonandPySparkto identify trends, anomalies, and performance issues, combining
exploratory analysis and root cause investigation to support data-driven decision-making
•BuiltPower BIdashboards to track key performance indicators and improve visibility into operational performance, reducing reporting time
by 40%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst
•Developed and maintained Power BI dashboards usingSQLandDAX, transforming raw data into actionable insights for business decision-
making across multiple domains.
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Led across-functionalteam of six to deliver and scale Deepcover game enhancements by leveraging user data, performance metrics, and
feedback analysis to drive feature prioritization and improve games outcomes
Projects
Scalable ML System for Customer Risk Prediction
•Translated customer credit business objective into a LightGBM boosted tree classification model on time-series data, combining feature
engineering and unsupervised segmentation to identify high-risk and low-risk customer segments
•Performed feature engineering on behavioral patterns such as transaction frequency and spending trends, improvingmodel precisionby 20%
while enhancing robustness and interpretability.
•Interpreted model outputs using precision, recall, and accuracy metrics, and built a client-facing decision framework to translate predictions
into actionable, business-ready recommendations""",

    """TAILORED RESUME — Malhar Gudekar Data Scientist Do it Best
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Machine Learning / Statistics:Classification, Regression, Feature Engineering, Model Evaluation, Precision, Recall, Accuracy, Statistical
Analysis, Predictive Analytics, Data Validation
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, Scikit-learn, LightGBM
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Designed and implemented end-to-endmachine learningpipeline to ingest, process, and analyze wearable data from 100+ users, combining
scalabledata ingestion,feature engineering, and model-ready transformations to enable longitudinal behavioral insights and downstream
analytics
•Developed and optimizedPostgreSQLdata models, indexing strategies, and query execution plans for high-volume datasets, improving query
performance by38%while enabling efficient feature extraction for machine learning workflows
•Developed, validated, and deployed ML-based retrieval pipeline with performance benchmarking and monitoring, improving multi-turn
response accuracy by 43% across longitudinal behavioral datasets
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Developed NLP and statistical modeling pipelines to classify health misinformation from large-scale social media data, applying feature
extraction, model validation, and iterative optimization to reduce latency by 41%
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade inferenceAPIsand deployment workflows to support reproducibility, monitoring, and consistent evaluation of
machine learning outputs
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Built and deployedRetrieval-Augmented Generation(RAG) system using embeddings andvector search, combining data pipelines, feature
engineering, and retrieval optimization to improve document retrieval efficiency by 64%
•Designed scalableETLand feature pipelines usingFastAPIandPostgreSQLto transform unstructured data into structured formats suitable
for analytics and machine learning use cases
•Optimized indexing strategies and data processing workflows to enable low-latency querying and scalable deployment of AI-driven systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Analyzed large-scale operational datasets usingPythonandPySparkto identify trends, anomalies, and performance issues, combining
exploratory analysis and root cause investigation to support data-driven decision-making
•BuiltPower BIdashboards to track key performance indicators and improve visibility into operational performance, reducing reporting time
by 40%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst
•Developed and maintained Power BI dashboards usingSQLandDAX, transforming raw data into actionable insights for business decision-
making across multiple domains.
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Led across-functionalteam of six to deliver and scale Deepcover game enhancements by leveraging user data, performance metrics, and
feedback analysis to drive feature prioritization and improve games outcomes
Projects
Scalable ML System for Customer Risk Prediction
•BuiltLightGBM-based machine learning model topredict customer credit riskfromtime-series transaction data, combining feature
engineering, classification modeling, and evaluation techniques to identify high-risk and low-risk segments.
•Designed and ran controlled model experiments, engineering behavioral features and iterating on classification thresholds through systematic
validation — improving credit risk prediction precision by 20%
•Evaluatedmodel performanceusing precision, recall, and accuracy, and designed a decision framework to translate predictions into actionable
credit limit recommendations.""",

    """TAILORED RESUME — Malhar Gudekar Data Scientist Echostar
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Machine Learning / Statistics:Classification, Regression, Feature Engineering, Model Evaluation, Anomaly Detection, Precision, Recall,
Accuracy, Statistical Analysis, Predictive Analytics, Data Validation
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, Scikit-learn, LightGBM
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Designed and implemented end-to-endmachine learningpipeline to ingest, process, and analyze wearable data from 100+ users, combining
scalabledata ingestion,feature engineering, and model-ready transformations to enable longitudinal behavioral insights and downstream
analytics
•Developed and optimizedPostgreSQLdata models, indexing strategies, and query execution plans for high-volume datasets, improving query
performance by38%while enabling efficient feature extraction for machine learning workflows
•Built embedding-based retrieval and summarization pipeline to enhance contextual understanding of user interactions, improving multi-turn
response accuracy by 43% and supporting more reliable behavioral analysis
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•DevelopedNLP-based machine learning pipelines to detect health misinformation from large-scale social media data, applying text prepro-
cessing,feature extraction, andoptimizationtechniques to reduce processing latency by41%
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade inference APIs and deployment workflows to support observability, predictive health monitoring, and consistent
evaluation of AI/ML model performance outputs
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Built and deployedRetrieval-Augmented Generation(RAG) system using embeddings andvector search, combining data pipelines, feature
engineering, and retrieval optimization to improve document retrieval efficiency by 64%
•Designed scalable ETL and log aggregation pipelines using FastAPI and PostgreSQL to transform unstructured system data into structured
formats for predictive analytics and machine learning
•Optimized indexing strategies and data processing workflows to enable low-latency querying and scalable deployment of AI-driven systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Applied anomaly detection techniques to large-scale operational system logs using Python and PySpark to identify trends and performance
issues, combining exploratory analysis and root cause investigation to surface actionable insights
•Built Tableau and Power BI dashboards to visualize key performance indicators and translate operational metrics into clear data narratives for
stakeholders, reducing reporting time by 40%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst
•Developed and maintained Power BI dashboards usingSQLandDAX, transforming raw data into actionable insights for business decision-
making across multiple domains.
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Led across-functionalteam of six to deliver and scale Deepcover game enhancements by leveraging user data, performance metrics, and
feedback analysis to drive feature prioritization and improve games outcomes
Projects
Scalable ML System for Customer Risk Prediction
•BuiltLightGBM-based machine learning model topredict customer credit riskfromtime-series transaction data, combining feature
engineering, classification modeling, and evaluation techniques to identify high-risk and low-risk segments.
•Performed feature engineering on behavioral patterns such as transaction frequency and spending trends, improvingmodel precisionby 20%
while enhancing robustness and interpretability.
•Evaluatedmodel performanceusing precision, recall, and accuracy, and designed a decision framework to translate predictions into actionable
credit limit recommendations.""",

    """TAILORED RESUME — Malhar Gudekar Data Scientist Sandhills Global
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Machine Learning / Statistics:Classification, Regression, Feature Engineering, Model Evaluation, Precision, Recall, Accuracy, Statistical
Analysis, Predictive Analytics, Data Validation
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, Scikit-learn, LightGBM, R, Scipy, Statsmodels,
Scikit-learn
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP, Jenkins, Apache Spark
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Designed and implemented end-to-end machine learning pipeline to analyze behavioral data from 100+ users, applying feature engineering,
segmentation techniques, and statistical transformations to generate actionable insights for downstream product and operations teams
•Designed relational data models and database schema for high-volume datasets, applying segmentation and indexing strategies that improved
query performance by 38% and enabled faster feature extraction for machine learning workflows
•Built embedding-based retrieval and summarization pipeline to enhance contextual understanding of user interactions, improving multi-turn
response accuracy by 43% and supporting more reliable behavioral analysis
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Developed NLP-based machine learning models in Python to classify and analyze large-scale text datasets, applying statistical preprocessing,
feature extraction, and model optimization to reduce processing latency by 41% and improve classification accuracy
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade inferenceAPIsand deployment workflows to support reproducibility, monitoring, and consistent evaluation of
machine learning outputs
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Built AI-driven document analysis system using Python, embeddings, and statistical retrieval techniques, combining feature engineering and
optimization to improve information extraction efficiency by 64%
•Designed scalableETLand feature pipelines usingFastAPIandPostgreSQLto transform unstructured data into structured formats suitable
for analytics and machine learning use cases
•Optimized indexing strategies and data processing workflows to enable low-latency querying and scalable deployment of AI-driven systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Analyzed large-scale operational datasets using Python, PySpark, and Spark distributed processing to identify trends, anomalies, and perfor-
mance issues, applying statistical analysis to surface actionable insights for operations and business stakeholders
•Visualized statistical findings and KPIs in Power BI and Tableau dashboards, translating model outputs into clear, actionable reports for
operations and executive stakeholders, reducing reporting time by 40%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst
•Developed and maintained Power BI dashboards usingSQLandDAX, transforming raw data into actionable insights for business decision-
making across multiple domains.
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Led across-functionalteam of six to deliver and scale Deepcover game enhancements by leveraging user data, performance metrics, and
feedback analysis to drive feature prioritization and improve games outcomes
Projects
Scalable ML System for Customer Risk Prediction
•BuiltLightGBM-based machine learning model topredict customer credit riskfromtime-series transaction data, combining feature
engineering, classification modeling, and evaluation techniques to identify high-risk and low-risk segments.
•Performed statistical feature engineering on behavioral patterns including transaction frequency and spending trends, using cross-validation
and statistical evaluation to improve model precision by 20% and support interpretable, results-oriented recommendations
•Derived actionable insights on pricing, promotions, and stock behavior using R and Python, enabling inventory planning decisions that reduced
stockout and overstock risks across five categories""",

    """TAILORED RESUME — Malhar Gudekar Data Scientist Virginia Tech
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Machine Learning / Statistics:Classification, Regression, Feature Engineering, Model Evaluation, Precision, Recall, Accuracy, Statistical
Analysis, Predictive Analytics, Data Validation
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, Scikit-learn, LightGBM
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Designed and implemented end-to-end ML pipeline to collect, process, and analyze behavioral and health data from 100+ university research
participants, enabling longitudinal student outcome insights, downstream analytics, and data-informed decision-making in an academic research
setting
•Developed and optimized PostgreSQL data models and query execution plans for high-volume research datasets, ensuring data integrity,
accuracy, and accessibility for analytics and decision-support workflows, improving performance by 38%
•Built embedding-based retrieval and summarization pipeline to enhance contextual understanding of user interactions, improving multi-turn
response accuracy by 43% and supporting more reliable behavioral analysis
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Developed and validated NLP-based ML models to classify behavioral patterns from large-scale unstructured data, applying text preprocessing,
feature extraction, and iterative model validation, reducing latency by 41% while improving classification accuracy
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade inferenceAPIsand deployment workflows to support reproducibility, monitoring, and consistent evaluation of
machine learning outputs
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Built and deployedRetrieval-Augmented Generation(RAG) system using embeddings andvector search, combining data pipelines, feature
engineering, and retrieval optimization to improve document retrieval efficiency by 64%
•Designed scalableETLand feature pipelines usingFastAPIandPostgreSQLto transform unstructured data into structured formats suitable
for analytics and machine learning use cases
•Optimized indexing strategies and data processing workflows to enable low-latency querying and scalable deployment of AI-driven systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Analyzed large-scale operational datasets usingPythonandPySparkto identify trends, anomalies, and performance issues, combining
exploratory analysis and root cause investigation to support data-driven decision-making
•BuiltPower BIdashboards to track key performance indicators and improve visibility into operational performance, reducing reporting time
by 40%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst
•Developed and maintained Power BI dashboards using SQL and DAX, translating complex datasets into clear visual insights and actionable
recommendations for both technical and non-technical stakeholders across multiple functional areas
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Led across-functionalteam of six to deliver and scale Deepcover game enhancements by leveraging user data, performance metrics, and
feedback analysis to drive feature prioritization and improve games outcomes
Projects
Scalable ML System for Customer Risk Prediction
•BuiltLightGBM-based machine learning model topredict customer credit riskfromtime-series transaction data, combining feature
engineering, classification modeling, and evaluation techniques to identify high-risk and low-risk segments.
•Performed feature engineering on behavioral patterns such as transaction frequency and spending trends, improvingmodel precisionby 20%
while enhancing robustness and interpretability.
•Evaluatedmodel performanceusing precision, recall, and accuracy, and designed a decision framework to translate predictions into actionable
credit limit recommendations.""",

    """TAILORED RESUME — Malhar Gudekar Data and AI Eng Westrock coffee
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable RAG and agentic AI system using FastAPI, PostgreSQL, and vector embeddings, designing agent architecture with
observability, context control, and human-in-the-loop verification
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimized data models, object relationships, and PostgreSQL schemas for high-volume datasets, improving query performance
by 38% across production workloads
•Built production-ready Python LLM pipeline integrating retrieval and context summarization, applying model validation and performance
tuning to improve response accuracy by 43%
•Developed asynchronous data transformation workflows with fault-tolerant design, focusing on data health, pipeline sustainability, and reliable
integration across complex data systems
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Engineered large-scale data transformation pipelines across social media streams, rapidly adopting distributed platform tooling to deliver
production-ready analytics and ensure data health at scale
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed scalable ETL and feature engineering pipelines capturing behavioral trends and temporal patterns, applying model validation and
performance tuning to optimize prediction accuracy
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar Databricks Data Engineer
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintained AWS-based scalable data pipelines to ingest high-volume data for 100+ users, enabling distributed S3 storage with Delta
Lake-structured layers for downstream analytics and AI consumption
•Designed and optimized SQL-based data models and lakehouse tables, applying indexing and query tuning techniques to improve platform
performance by 38%, enabling reliable data access for analytics and AI use cases
•Implemented pipeline workflow orchestration using AWS Step Functions and Databricks-compatible workflow patterns, adding data quality
checks, logging, retries, and failure handling to ensure data platform reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable ELT pipelines in Python and PySpark on Databricks for high-volume datasets in distributed environments,
reducing processing latency by 41% across batch and streaming workflows
•Built distributed batch and streaming ingestion pipelines using Kafka and PySpark Structured Streaming, enabling real-time data transformation
and large-scale analytics in distributed data environments
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalabledata processing pipelinesusingFastAPI,PostgreSQL, and optimized storage layers to support large-scale
analytics and downstream applications
•Designed fault-tolerant ETL workflows for ingesting and transforming high-volume enterprise datasets, implementing data governance controls
and monitoring to ensure reliable, compliant data availability at scale
•Developed data platform services and implemented Git-based CI/CD pipelines to enable automated, reliable deployment and real-time querying
across distributed, high-availability data environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Scientist Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Consolidated and analyzed 500+ user feedback signals and gameplay telemetry records, creating structured datasets that accelerated feature
prioritization by 35%
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built an end-to-end analytics data pipeline using Python, PySpark, and LightGBM to process large-scale time-series transaction data, including
ingestion, transformation, feature engineering, and machine learning model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar FDE UMATR
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, ETL Pipelines, Kafka, PySpark, gRPC, Protocol Buffers, Grafana, InfluxDB, Kubernetes
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and deployment of a cross-platform data integration system ingesting high-frequency sensor data from 100+ users,
enabling real-time operational data collection and downstream insight generation for engineering and research teams
•Designed and optimizedPostgreSQL schema, indexing strategies, and query execution plansfor high-volume datasets, improving query
performance by 38% under production workloads
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed real-time data ingestion pipelines using Kafka and Neo4j Streams to capture, route, and process high-throughput operational
data streams from external systems, enabling downstream pattern detection and engineering insights
•Designed and shipped production-grade REST APIs using FastAPI to integrate data systems across distributed environments, implementing
validation, error handling, monitoring, and automated CI/CD deployment workflows enabling reliable cross-system integration at scale
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed production data integration platform using FastAPI and PostgreSQL, connecting disparate data sources and custom ingestion
pipelines to enable real-time querying and operational insight generation across distributed system architectures
•Designed fault-tolerant data pipelines connecting external systems and customer infrastructure, enabling low-latency, reliable data availability
for downstream engineering workflows and analytics
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements in production environments
•Developed backend services enabling real-time, high-performance querying of unstructured data across distributed system architectures
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services and decision-making insights
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues in distributed systems environments
•Built custom Python scripts and SQL tooling to integrate, validate, and analyze operational data across customer systems, mapping dependencies
and surfacing data quality issues that accelerated root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Deployed and maintained 20+ custom reporting and analytics solutions across enterprise client environments in Sales, Finance, and Operations,
integrating data from customer systems using SQL and DAX to enable operational visibility and business decision-making
•Automated recurringExcel-based reporting workflows usingVBA, implementing data validation, transformation, and scheduling logic,
reducing report preparation time by42%and improving data consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 engineers and designers to ship product updates for DeepCover, using telemetry data, user feedback, and
performance analysis to prioritize engineering decisions and guide development
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog grooming, sprint planning, and
issue resolution to improve cross-team visibility and ensure on-time milestone delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends""",

    """TAILORED RESUME — Malhar Gudekar Fastenal Data Integeration Engineer
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, enabling distributed storage in
S3and downstream analytics consumption
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implementedworkflow orchestration using AWS Step Functionsand monitoring for real-time streaming pipelines, adding data quality
checks, logging, retries, and failure handling to ensure reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets in distributed environments, reducing
processing latency by41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalabledata processing pipelinesusingFastAPI,PostgreSQL, and optimized storage layers to support large-scale
analytics and downstream applications
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Consolidated and analyzed 500+ user feedback signals and gameplay telemetry records, creating structured datasets that accelerated feature
prioritization by 35%
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Full Stack Dev UST
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed full stack RAG and agentic AI application using React, FastAPI, and PostgreSQL, integrating LLM-based agents and vector
embeddings for production AI-powered features
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed full stack backend services and REST API integrations enabling real-time AI model serving, supporting responsive web application
features across distributed system architectures
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python generative AI pipeline using PyTorch and scikit-learn for model training and retrieval, improving multi-turn
response accuracy by 43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable NLP and generative AI pipelines in Python using TensorFlow and Pandas, applying model evaluation and
optimization techniques to reduce processing latency by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developed production-grade REST APIs using FastAPI to serve AI models, implementing prompt engineering workflows,
validation, monitoring, and CI/CD deployment for scalable AI integrations
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built end-to-end machine learning system using Python, Pandas, scikit-learn, and LightGBM to forecast customer spending and assess credit
risk from large-scale time-series data
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar Github
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Master Achievements Bank
University of Illinois Urbana-Champaign — Research Assistant (iSchool)
•Owned end-to-end design, development, and integration of cross-platform system ingesting wearable data for 100+ users, enabling scalable
data collection and downstream analytics
•Designed and optimized PostgreSQL schema, indexing strategies, and query execution plans for high-volume datasets, improving query
performance by 38% under production workloads
•Built robust, production-ready Python pipeline with retrieval and context summarization, improving multi-turn response accuracy by 43%
•Developed backend workflows for real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
CHI AI in Infodemic Management — Research Assistant
•Designed and deployed highly scalable NLP pipelines in Python to process high-volume datasets, reducing processing latency by 41%
•Built distributed data ingestion pipelines using Kafka and Neo4j Streams for real-time, high-throughput processing and pattern detection
•Designed and developed production-grade REST APIs using FastAPI, implementing validation, monitoring, and deployment workflows for
scalable integration
•Enabled large-scale data processing across social media streams using distributed system architecture principles
Business Intelligence Group — Technical Consultant
•Built and deployed scalable microservices-based Retrieval-Augmented Generation (RAG) system using FastAPI, PostgreSQL, and vector
embeddings for production applications
•Designed efficient, fault-tolerant ETL pipelines to process and index large document datasets for low-latency retrieval systems
•Improved system performance by 64% through optimized indexing strategies and pipeline efficiency improvements in production environments
•Developed backend services enabling real-time, high-performance querying of unstructured data across distributed system architectures
Swift Mobil Software Solutions — Data Analyst
•Built interactive Power BI dashboards for logistics and mobility KPIs, reducing reporting time by 40% and improving visibility into operational
performance
•Processed and optimized large-scale datasets using Python and PySpark to identify failure patterns, trends, and performance issues in distributed
environments
•Developed SQL and graph queries to map dependencies, analyze operations, detect data quality issues, accelerating root-cause analysis by 26%
Pscope Technologies — Data Analyst
•Developed and maintained 20+ Power BI dashboards across Sales, Finance, and Operations using SQL and DAX, enabling KPI tracking and
data-driven decision-making
•Automated recurring Excel-based reporting workflows using VBA, implementing validation and scheduling logic, reducing report preparation
time by 42%
Stu/Dio at Illinois — Project Manager
•Led cross-functional team of 6 engineers and designers to deliver product updates using user feedback, telemetry data, and performance insights
for feature prioritization
•Tracked sprint progress, delivery metrics, and QA issues through JIRA-based workflows, managing backlog grooming and ensuring on-time
delivery
Scalable ML System for Customer Risk Prediction
•Built end-to-end machine learning system using Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scale time-series data
•Designed scalable ETL and feature engineering pipelines capturing behavioral trends and temporal patterns to improve model performance
•Developed decision framework for credit line adjustments, improving prediction precision by 20% and enabling risk-aware classification
FMCG Sales Demand Forecasting and Optimization
•Developed ARIMA-based sales forecasting model in R achieving 80% accuracy with 95% predictions within confidence intervals across five
FMCG categories
•Used ggplot2 and dplyr to analyze daily sales trends, improving inventory planning and reducing stockouts and overstock scenarios
FMCG Product Sales Analysis
•Engineered Tableau dashboard analyzing 12+ product categories across 100+ countries, identifying key markets with revenue peaks of $200M
•Built multi-view performance tracking system identifying 30% sales volatility and enabling early detection of major dips and recoveries
•Developed geographic heat maps and filters revealing underperforming categories and supporting targeted improvement strategies
Advanced Facial Analysis System
•Built real-time facial recognition system using Python, OpenCV, and CNN achieving 98% emotion classification accuracy
•Processed 10,000+ images to train supervised learning model achieving 95% accuracy across varying lighting and orientations
Basilisk Cryptography System
•Developed terminal-based encrypted communication system integrating multiple cryptographic algorithms for secure key exchange
•Designed layered encryption mechanism combining up to six algorithms under unified key architecture
•Published research paper titled BASILISK Security Hub in UGC Care Journal Volume 13
Environmental Data Analytics and Visualization
•Analyzed environmental datasets to uncover 20% rise in acetaldehyde levels over seven years using trend visualization techniques
•Built heat maps and tree maps across six states identifying high toxin concentrations and regional risk patterns
Database Design for Nonresident Alien Payments
•Designed relational database with 15+ entities and implemented EER model with SQL and XML schema validation for IRS compliance
•Built Neo4j graph database with automated Cypher query generation using Python and SQLAlchemy for cross-system insights
Mobile Expense Tracker Application
•Developed Flutter application with Provider state management to track and visualize personal expenses
•Integrated dynamic charts and responsive UI enabling weekly spending analysis and improved user experience
AI-Powered AR Virtual Try-On (Glossier)
•Conducted customer segmentation and behavioral analysis identifying high engagement among users aged 18–44 for AR adoption
•Developed strategic roadmap outlining AR integration, ROI projections, and KPIs including return reduction and conversion improvement
Predictive Credit Limit Adjustment
•Built LightGBM-based model forecasting customer spending and enabling personalized credit line adjustments
•Segmented customers into risk groups improving fraud detection and financial decision-making accuracy
F1 Race Prediction System
•Engineered dataset from FastF1 API (2022–2025) to build lap-level and race-level predictive models
•Applied GBM and Monte Carlo simulations to predict race outcomes achieving 90% accuracy for final grid positions""",

    """TAILORED RESUME — Malhar Gudekar Grad SWE Enigma
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned theend-to-end design, development, and integrationof cross-platform system ingesting wearable data for 100+ users, enabling
scalable, continuous data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and query execution plansfor high-volume datasets, improving query
performance by 38% under production workloads
•Built production-ready Python LLM integration pipeline with data ingestion, retrieval, summarization, improving response accuracy by 43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Designed and developedproduction-grade REST APIs using FastAPI, implementing validation, error handling, and monitoring, and built
automated deployment workflows to ensurehigh reliability, reproducibility, and scalable integrationacross distributed systems
•Built data validation and quality checks across streaming pipelines to ensure reliable, consistent data availability across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based LLM-powered RAG system using FastAPI, PostgreSQL, and vector embeddings, integrating
third-party AI APIs for production-grade applications
•Designed fault-tolerant ETL pipelines to ingest, clean, and structure multi-format datasets from third-party sources for low-latency, reliable
retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements in production environments
•Developed backend services enabling real-time, high-performance querying of unstructured data across distributed system architectures
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services and decision-making insights
•Built and maintained Python data pipelines integrating with operational data sources to identify failure and performance across systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLfor data
extraction andDAXfor advanced calculations, enabling KPI tracking and data-driven decision-making
•Automated recurringExcel-based reporting workflows usingVBA, implementing data validation, transformation, and scheduling logic,
reducing report preparation time by42%and improving data consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliver product updates for DeepCover game, leveraging user feedback, telemetry
data, and performance insights to drive data-driven feature prioritization and improvements
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog grooming, sprint planning, and
issue resolution to improve cross-team visibility and ensure on-time milestone delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built end-to-end Python backend system to ingest, transform, and analyze large-scale time-series transaction data, integrating LightGBM
modeling and feature engineering to predict credit risk
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar Graduate Integeration Engineer Incture LLC
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and deployment of cross-platform cloud integration system connecting multiple application sources for 100+ users,
enabling secure scalable data flows and downstream analytics consumption
•Designed and optimizedPostgreSQL schema, indexing strategies, and query execution plansfor high-volume datasets, improving query
performance by 38% under production workloads
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built event-driven integration pipelines using Kafka with AMQP and MQTT messaging protocols for real-time asynchronous high-throughput
data processing across distributed systems
•Designed and developed production-grade REST, SOAP, and OData APIs using FastAPI and Node.js, handling XML and JSON payload
processing and building CI/CD deployment workflows for reliable and scalable enterprise system integrations
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable microservices-based integration system using FastAPI, PostgreSQL, Docker, and Kubernetes, implementing
cloud-native API gateway patterns for production-grade enterprise application connectivity
•Designed fault-tolerant ETL integration flows with XML and JSON payload transformation, troubleshooting integration errors and optimizing
processing performance for low-latency high-throughput system connectivity
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements in production environments
•Developed backend services enabling real-time, high-performance querying of unstructured data across distributed system architectures
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services and decision-making insights
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues in distributed systems environments
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLfor data
extraction andDAXfor advanced calculations, enabling KPI tracking and data-driven decision-making
•Automated recurringExcel-based reporting workflows usingVBA, implementing data validation, transformation, and scheduling logic,
reducing report preparation time by42%and improving data consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliver product updates for DeepCover game, leveraging user feedback, telemetry
data, and performance insights to drive data-driven feature prioritization and improvements
•Tracked sprint delivery and QA issues through JIRA Agile workflows, documenting integration landscapes and technical mappings to support
cross-team visibility and ensure on-time milestone delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar Jr. BI Analyst Swivel Payment Solutions LLC
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built production-ready Python pipeline for automated report generation and scheduled distribution, improving data processing accuracy by
43% and reducing manual reporting overhead
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure, trends, and performance issues
•Wrote and troubleshot SQL queries to map operational dependencies, prep data for reporting, and detect quality issues, translating findings
clearly for business stakeholders and accelerating root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained 20+ Power BI and Tableau dashboards across Sales, Finance, and Operations using SQL and DAX, supporting KPI
reporting, data warehouse queries, and stakeholder decision-making
•Automated recurring report workflows and distributions using VBA and Python, implementing validation and scheduling logic, reducing report
preparation time by 42% and improving data consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Tracked sprint delivery and QA issues through JIRA workflows, peer reviewing team work and supporting report promotion from development
through testing to production
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
•Built and compared forecasting models in R including ARIMA, SARIMA, and regression, using ggplot2 for visualization and evaluating
demand patterns with RMSE and MAPE metrics
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Jr. Quant Dev Harbour capital
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, enabling distributed storage in
S3and downstream analytics consumption
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented production workflow orchestration using AWS Step Functions with automated monitoring, logging, data validation frameworks,
and failure handling to ensure pipeline auditability and reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable ELT pipelines in Python with modular, testable code, schema validation, and data quality monitoring, reducing
processing latency by 41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
across systems
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, production-grade data processing pipelines using FastAPI and PostgreSQL, with validation frameworks ensuring
data integrity and correctness for downstream analytics
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
availability
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers to deliver data-driven improvements, analytics insights, and system tracking
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
decisions
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar Junior AI Engineer Nova Staff
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, ETL Pipelines, Kafka, PySpark, scikit-learn, PyTorch, TensorFlow
•Stack:LangChain, LlamaIndex, Hugging Face, OpenAI API, FAISS, Pinecone, Prompt Engineering, Streamlit, MLOps
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable RAG and agentic AI system using LangChain, FastAPI, PostgreSQL, and vector embeddings with semantic search
for production applications
•Designed efficient, fault-tolerant ETL pipelines with MLOps monitoring to process and index large document datasets for low-latency vector
search and retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python generative AI pipeline with prompt engineering and Hugging Face transformer models, improving response
accuracy by 43%
•Developed asynchronous AI pipelines integrating FAISS vector databases for real-time, fault-tolerant semantic retrieval workflows with focus
on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable NLP and generative AI pipelines using OpenAI APIs and Python, reducing processing latency by 41% and
improving output quality
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Implemented AI agent workflows and patterns using LangChain to automate large-scale data processing and enable autonomous task execution
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built end-to-end ML system using Python, scikit-learn, and LightGBM to predict credit risk from time-series transaction data, covering feature
engineering, model training, evaluation, and deployment
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar ML Eng RK Infotech
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, C++ (basic), Data Structures & Algorithms (Arrays, Trees, Graphs, DP), LeetCode
•Machine Learning & AI:PyTorch, Scikit-learn, Neural Networks, NLP, Supervised & Unsupervised Learning, Feature Engineering, Generative
AI, Model Optimization, Inference
•Systems & Tools:FastAPI, Distributed Systems, ETL Pipelines, Kafka, PySpark, PostgreSQL, Neo4j, AWS, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-basedRAG and agentic AI systemusingFastAPI,PostgreSQL, and vector embeddings for
high-performance production applications
•Designed efficient, fault-tolerantETL, async pipelinesto process, index large document datasets for optimized low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline-level tuning in distributed production environments
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across scalable distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data pipelines and analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built robust, production-readyPython generative AI pipelinewith retrieval and context summarization, improving response accuracy by43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability and
system reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable NLP pipelines in Python, implementing supervised classification models for data preprocessing, training, and
validation, reducing processing latency by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing across scalable systems
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows for reliable integration
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples for optimized
performance and scalability
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets using Python, NumPy, and PySpark to identify failure patterns and bottlenecks, creating visual
reports to communicate insights
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, accelerating root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and insights
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and resolution for timely delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built an end-to-end supervised ML system using Python, Pandas, NumPy, Scikit-learn, and LightGBM to train, validate, and evaluate credit
risk models on large-scale time-series datasets
•Designed scalable data preprocessing and feature engineering pipelines capturing behavioral patterns, applying model validation techniques to
reduce overfitting and improve generalization""",

    """TAILORED RESUME — Malhar Gudekar ML Eng Tesla
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, C++ (basic), Data Structures & Algorithms (Arrays, Trees, Graphs, DP), LeetCode
•Machine Learning & AI:PyTorch, Neural Networks, Generative AI, Model Optimization, Inference, NLP, Computer Vision,TensorFlow,
scikit-learn, Anomaly Detection, Model Monitoring
•Systems & Tools:FastAPI, Distributed Systems, ETL Pipelines, Kafka, PySpark, PostgreSQL, Neo4j, AWS, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable ML system using PyTorch, FastAPI, PostgreSQL, and vector embeddings for multi-modal data processing and
high-performance production inference
•Designed efficient, fault-tolerantETL, async pipelinesto process, index large document datasets for optimized low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline-level tuning in distributed production environments
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across scalable distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design, development, and deployment of cross-platform ML backend system ingesting wearable sensor data for 100+ users,
enabling scalable collection and real-time analytics
•Designed and optimized PostgreSQL schema and ML inference pipeline architecture for high-volume sensor datasets, improving query
performance by 38% in production workloads
•Built production-ready Python generative AI pipeline using PyTorch and transformer models with retrieval and context summarization,
improving response accuracy by 43%
•Developed asynchronous model inference workflows with monitoring and alerting for real-time, fault-tolerant processing of sensor data with
focus on production reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable NLP and anomaly detection pipelines in Python to process high-volume datasets, reducing processing latency
by 41% and improving model accuracy
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing across scalable systems
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows for reliable integration
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples for optimized
performance and scalability
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure patterns and bottlenecks in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, accelerating root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and insights
•Automated recurringExcelworkflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and resolution for timely delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built end-to-end ML pipeline using Python, PyTorch, and LightGBM to classify patterns from large-scale time-series datasets, applying model
validation and benchmarking techniques
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision""",

    """TAILORED RESUME — Malhar Gudekar ML Engineer ByteDance
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, C++ (basic), Data Structures & Algorithms (Arrays, Trees, Graphs, DP), LeetCode
•Machine Learning & AI:PyTorch, Neural Networks, Generative AI, Model Optimization, Inference, NLP
•Systems & Tools:FastAPI, Distributed Systems, ETL Pipelines, Kafka, PySpark, PostgreSQL, Neo4j, AWS, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed production ML risk detection system using graph-based retrieval and ensemble modeling to classify bad actor patterns
across high-volume user activity data
•Designed ETL pipelines and SQL/Hive data querying infrastructure to process large-scale datasets, supporting real-time and offline risk signal
•Ran controlled experiments to validate risk model hypotheses, optimizing the detection pipeline and improving system performance by 64%
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across scalable distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data pipelines and analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built robust, production-readyPython generative AI pipelinewith retrieval and context summarization, improving response accuracy by43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability and
system reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed deep learning NLP pipelines in Python to extract behavioral features and detect anomalous activity patterns, reducing
processing latency by 41%
•Developed graph-based ML models using Neo4j and Kafka to map entity relationships and detect coordinated inauthentic behavior across
large-scale social datasets
•Developed and monitored ML model serving APIs, tracking inference performance metrics and automating deployment workflows to ensure
reliable, reproducible risk model outputs
•Applied unsupervised learning and distributed processing to surface anomalous behavioral signals across high-volume social media data
streams at scale
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure patterns and bottlenecks in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, accelerating root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and insights
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and resolution for timely delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Applied unsupervised learning and distributed processing to surface anomalous behavioral signals across social media data streams at scale
•Engineered features capturing behavioral abuse signals and transaction patterns, using scalable SQL/Hive pipelines compatible with Hadoop
for risk model training
•Defined risk control metrics and built threshold governance framework, incorporating model outputs to improve classification precision by
20% and promote data-driven risk decisions""",

    """TAILORED RESUME — Malhar Gudekar Platform and Integeration Engineer Vooma
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and integration of cross-platform data pipeline for 100+ users, translating customer requirements into scalable
ingestion workflows and third-party API connections
•Designed and optimizedPostgreSQL schema, indexing strategies, and query execution plansfor high-volume datasets, improving query
performance by 38% under production workloads
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Designed and developed production-grade REST and GraphQL APIs using FastAPI, implementing validation, monitoring, and automated
deployment workflows for scalable integration across distributed systems
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable microservices-based RAG platform integrating OpenAI and Anthropic APIs, using FastAPI, PostgreSQL, and
vector embeddings to serve production applications
•Designed fault-tolerant ETL pipelines and automated workflows using Python, TypeScript, and Node.js to ingest, transform, and index large
document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements in production environments
•Developed backend services enabling real-time, high-performance querying of unstructured data across distributed system architectures
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services and decision-making insights
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLfor data
extraction andDAXfor advanced calculations, enabling KPI tracking and data-driven decision-making
•Automated recurringExcel-based reporting workflows usingVBA, implementing data validation, transformation, and scheduling logic,
reducing report preparation time by42%and improving data consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliver product updates for DeepCover game, leveraging user feedback, telemetry
data, and performance insights to drive data-driven feature prioritization and improvements
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog grooming, sprint planning, and
issue resolution to improve cross-team visibility and ensure on-time milestone delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar Portfolio Analyst Access Analytix
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand analytics
•Designed and optimizedPostgreSQL architecturefor high-volume, production-scale datasets, improving query performance by 38%
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Developed production-gradeAPIsand deployment workflows to improve system reliability and reproducibility
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements
•Developed backend services enabling real-time, high-performance querying of unstructured data
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues
•Developed SQL queries to analyze operational performance, detect trends and anomalies, and support time-sensitive ad hoc analysis, accelerating
decision-making and root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained 20+ dashboards across Sales, Finance, and Operations using SQL and DAX, enabling real-time portfolio tracking,
KPI monitoring, and competitive business decision-making
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using user feedback and performance insights to guide
data-driven feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving cross-team visibility and supporting
on-time milestone reviews
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed market demand and pricing trends across product categories and regions to identify seasonal patterns, competitive dynamics, and
key drivers impacting inventory and portfolio decisions
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable pricing and market insights across product categories, enabling data-driven inventory decisions and reducing exposure to
supply and demand volatility""",

    """TAILORED RESUME — Malhar Gudekar Python Developer Precision tech
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, ETL Pipelines, Kafka, PySpark, scikit-learn, PyTorch, TensorFlow, Keras
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-basedRAG and agentic AI systemusingFastAPI,PostgreSQL, and vector embeddings for
production applications
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved AI system performance by 64% through model optimization, hyperparameter tuning, and pipeline improvements in production
•Developed microservices and backend services enabling real-time AI model serving and performance monitoring of unstructured data across
cloud-deployed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python generative AI pipeline using scikit-learn and retrieval-based techniques for model evaluation and summarization,
improving accuracy by 43%
•Developed CI/CD pipelines and asynchronous backend workflows for automated testing, deployment, and real-time data processing
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Processed large-scale datasets using PySpark distributed computing for ML model input preparation, enabling high-throughput data transfor-
mation and feature engineering
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built end-to-end ML system using Python, scikit-learn, and LightGBM for credit risk prediction, covering data preprocessing, feature
engineering, model training, evaluation, and cloud deployment
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar Quant Dev 1823
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, enabling distributed storage in
S3and downstream analytics consumption
•Designed and optimized SQL-based data models and warehouse tables in PostgreSQL, applying indexing and query tuning to improve
performance by 38%, enabling reliable high-speed data access for analytics and reporting pipelines
•Implementedworkflow orchestration using AWS Step Functionsand monitoring for real-time streaming pipelines, adding data quality
checks, logging, retries, and failure handling to ensure reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployedscalable ELT pipelinesinPythonfor high-volume social media datasets in distributed environments, reducing
processing latency by41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable greenfield data processing applications using FastAPI, PostgreSQL, and optimized storage layers, supporting
large-scale analytics and business-critical downstream reporting workflows
•Designed and deployed scalable ELT pipelines in Python and Pandas for high-volume datasets in distributed environments, reducing processing
latency by 41% and ensuring reliable data delivery for downstream analytics workflows
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintained SQL-based data pipelines and warehouse models using PostgreSQL and Snowflake-compatible schemas, writing complex
joins and aggregations to deliver analytics-ready datasets for business decision-making
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Consolidated and analyzed 500+ user feedback signals and gameplay telemetry records, creating structured datasets that accelerated feature
prioritization by 35%
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built an end-to-end quantitative data pipeline using Python, Pandas, and LightGBM to process large-scale financial time-series transaction
data, including ingestion, transformation, feature engineering, and predictive model integration
•Designed and implemented scalable ETL and feature engineering pipelines for financial time-series data, capturing behavioral trends and
temporal patterns such as rolling averages and spending frequency to improve quantitative model performance
•Developed a data-driven decision framework incorporating model outputs and risk thresholds to improve prediction precision by 20%, enabling
scalable credit risk analytics aligned with investment decision workflows""",

    """TAILORED RESUME — Malhar Gudekar Research Assistant Brigham Research Institute
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Machine Learning / Statistics:Classification, Regression, Feature Engineering, Model Evaluation, Precision, Recall, Accuracy, Statistical
Analysis, Predictive Analytics, Data Validation
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j, Scikit-learn, LightGBM
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool
•Designed and implemented end-to-end ML pipeline to process wearable time-series sensor data from 100+ users, handling noisy and irregular
physiological signals and engineering features to enable longitudinal behavioral analysis
•Developed optimized data pipelines for high-volume wearable health datasets, handling missing values, irregular sampling, and sensor artifacts
to enable efficient feature extraction for machine learning workflows
•Built PyTorch-based deep learning pipeline with feature extraction and pattern recognition to enhance behavioral signal analysis, improving
response accuracy by 43% and enabling reliable longitudinal health insights
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Developed Python ML pipelines using NumPy and SciPy for signal preprocessing, feature extraction, and pattern detection across large-scale
time-series datasets, reducing processing latency by 41%
•Built distributeddata pipelinesusingKafkaandNeo4jStreams to enablescalable ingestion, transformation, and real-time analysis of
high-volume unstructured datasets
•Designed production-grade inferenceAPIsand deployment workflows to support reproducibility, monitoring, and consistent evaluation of
machine learning outputs
Business Intelligence Group August 2025 - December 2025
Technical Consultant
•Built and deployedRetrieval-Augmented Generation(RAG) system using embeddings andvector search, combining data pipelines, feature
engineering, and retrieval optimization to improve document retrieval efficiency by 64%
•Designed scalableETLand feature pipelines usingFastAPIandPostgreSQLto transform unstructured data into structured formats suitable
for analytics and machine learning use cases
•Optimized indexing strategies and data processing workflows to enable low-latency querying and scalable deployment of AI-driven systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst
•Analyzed large-scale operational datasets usingPythonandPySparkto identify trends, anomalies, and performance issues, combining
exploratory analysis and root cause investigation to support data-driven decision-making
•BuiltPower BIdashboards to track key performance indicators and improve visibility into operational performance, reducing reporting time
by 40%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst
•Developed and maintained Power BI dashboards usingSQLandDAX, transforming raw data into actionable insights for business decision-
making across multiple domains.
•Performed data validation, cleaning, and transformation on large multi-source datasets usingSQLandExcel, improving data accuracy by over
30% and reducing reporting inconsistencies, enabling faster and more reliable decision-making across sales, finance, and operations teams
Stu/Dio at Illinois August 2025 - Present
Project Manager
•Led across-functionalteam of six to deliver and scale Deepcover game enhancements by leveraging user data, performance metrics, and
feedback analysis to drive feature prioritization and improve games outcomes
Projects
Scalable ML System for Customer Risk Prediction
•BuiltLightGBM-based machine learning model topredict customer credit riskfromtime-series transaction data, combining feature
engineering, classification modeling, and evaluation techniques to identify high-risk and low-risk segments
•Performed feature engineering on time-series behavioral patterns including temporal statistics, frequency-domain features, and trend indicators,
improving model precision by 26% and enhancing interpretability
•Evaluated model performance using precision, recall, and accuracy through reproducible analysis workflows, and designed a decision framework
to translate predictions into actionable recommendations""",

    """TAILORED RESUME — Malhar Gudekar SDE Amazon
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned theend-to-end design, development, and integrationof cross-platform system ingesting wearable data for 100+ users, enabling
scalable, continuous data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and query execution plansfor high-volume datasets, improving query
performance by 38% under production workloads
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Designed and developedproduction-grade REST APIs using FastAPI, implementing validation, error handling, and monitoring, and built
automated deployment workflows to ensurehigh reliability, reproducibility, and scalable integrationacross distributed systems
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings for production-grade applications
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency, high-throughput retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements in production environments
•Developed backend services enabling real-time, high-performance querying of unstructured data across distributed system architectures
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services and decision-making insights
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues in distributed systems environments
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLfor data
extraction andDAXfor advanced calculations, enabling KPI tracking and data-driven decision-making
•Automated recurringExcel-based reporting workflows usingVBA, implementing data validation, transformation, and scheduling logic,
reducing report preparation time by42%and improving data consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliver product updates for DeepCover game, leveraging user feedback, telemetry
data, and performance insights to drive data-driven feature prioritization and improvements
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog grooming, sprint planning, and
issue resolution to improve cross-team visibility and ensure on-time milestone delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar SDE Quince
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design, development, and deployment of cross-platform software system for 100+ users, shipping high-quality features and
continuously improving performance, reliability, and engineering standards
•Designed and optimizedPostgreSQL schema, indexing strategies, and query execution plansfor high-volume datasets, improving query
performance by 38% under production workloads
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highly scalable data processing pipelines in Python and Java to handle high-volume datasets, applying strong CS
fundamentals to reduce processing latency by 41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Designed and developed production-grade REST APIs using FastAPI and Node.js, leveraging AI-powered development tools to improve coding
efficiency and problem-solving, with validation, error handling, and monitoring for high reliability
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based Retrieval-Augmented Generation (RAG) system usingFastAPI,PostgreSQL, and vector
embeddings for production-grade applications
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency, high-throughput retrieval systems
•Improved system performance by 64% through optimized indexing strategies and pipeline tuning, maintaining strong documentation and
adhering to coding and architectural standards throughout production deployment
•Developed backend services enabling real-time, high-performance querying of unstructured data across distributed system architectures
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services and decision-making insights
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues in distributed systems environments
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLfor data
extraction andDAXfor advanced calculations, enabling KPI tracking and data-driven decision-making
•Automated recurringExcel-based reporting workflows usingVBA, implementing data validation, transformation, and scheduling logic,
reducing report preparation time by42%and improving data consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 to ship product features rapidly using AI-powered development tools, leveraging performance insights to
prioritize and deliver high-impact improvements in a fast-paced environment
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog grooming, sprint planning, and
issue resolution to improve cross-team visibility and ensure on-time milestone delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar SQL Developer
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Data Warehousing & Business Intelligence, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: DBMS, Big Data Analysis, Data Warehousing and Mining, Project Management, NLP, Machine Learning, Social Media Analytics
Skills
•Analytical: Data Analysis, Exploratory Data Analysis, Statistical Analysis, Trend Analysis, Root Cause Analysis, KPI Reporting, Data
Validation, Data Cleaning, Anomaly Detection, ETL, Predictive Analytics
•Programming / Querying:Python, SQL, Pandas, NumPy, PySpark, PostgreSQL, Neo4j
•Visualization / Reporting:Power BI, Tableau, DAX, Excel, VBA, Dashboard Development, Data Visualization
•Data / Cloud / Tools:AWS S3, EC2, Redshift, EKS, FastAPI, Docker, Git, Kafka, pgVector, GCP
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end analysis and development ofcross-platform system integratingwearable data for 100+ users, enabling scalabledata
ingestionand insights
•Designed and optimizedPostgreSQL datasetsfor high-volume data, improving query performance by 38% and enabling faster reporting
•Built robustPythonworkflows for data retrieval and summarization, improving multi-turn response accuracy by43%and supporting insights
•Developeddata workflowsfor real-time processing of longitudinal datasets with focus on reliability and consistent analytical outputs
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP analysis pipelinesinPythonto process large datasets, reducing processing latency by41%
•Built distributed data pipelines usingKafkaandNeo4jStreams for real-time, high-throughput data analysis and pattern detection
•Developed production-gradeAPIsand workflows to improve data access, reporting consistency, and reproducibility across processes
•Enabled large-scale data analysis across social media streams usingdistributed system architectureprinciples for better insights
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable data system to analyze and retrieve insights from large datasets usingFastAPI,PostgreSQL, and vector-based
retrieval methods
•Designed efficient, fault-tolerantETLpipelines to process and structure large document datasets for reporting and analytical use cases
•Improved system performance by64%through optimized indexing strategies and data processing improvements for faster analysis
•Developed backend services enabling real-time, high-performance querying and analysis of large-scale unstructured datasets
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving overall business
performance visibility across operations
•Processed and analyzed large-scale operational datasets usingPythonandPySparkto identify trends, inefficiencies, and performance issues
•DevelopedSQLandgraph queriesto analyze operations, detect data quality issues, and improve root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, usingSQLandDAXto
support KPI tracking and decision-making
•Automated recurringExcel-based reporting workflows usingVBA, reducing report preparation time by42%and improving data consistency
across reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6to deliver product updates for DeepCover, game, using performance data and insights to guide data-driven
feature decisions
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, improving visibility and supporting on-time
milestone delivery
Projects
FMCG Sales Demand Forecasting March 2025
View Project
•Analyzed FMCGsales demand dataacross categories and locations to identify trends, seasonal patterns, and key drivers impacting inventory
decisions
•Built and compared forecasting models includingARIMA,SARIMA, and regression to evaluate demand patterns and improve forecast
accuracy using RMSE and MAPE
•Derived actionable insights on promotions, pricing, and stock behavior, enabling better inventory planning and reducing stockouts and
overstocking risks""",

    """TAILORED RESUME — Malhar Gudekar SWE Aven
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design, development, and deployment of a cross-platform consumer data system for 100+ users, building from zero to
production with scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and query execution plansfor high-volume datasets, improving query
performance by 38% under production workloads
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Designed production-grade REST APIs using FastAPI, implementing validation, error handling, rate limiting, and performance monitoring,
and built automated deployment workflows for reliable, low-latency integration across distributed systems
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based AI system using FastAPI, PostgreSQL, and vector embeddings, powering consumer-facing
features with reliable, low-latency responses in production
•Designed efficient, fault-tolerantETLpipelines to process and index large document datasets for low-latency, high-throughput retrieval systems
•Improved system performance by 64% through optimized indexing and pipeline efficiency, directly reducing user-facing response latency
across production environments
•Developed backend services enabling real-time, high-performance querying and AI-driven decision-making across distributed system archi-
tectures, optimized for consistent performance under variable load
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services and decision-making insights
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues in distributed systems environments
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data quality issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLfor data
extraction andDAXfor advanced calculations, enabling KPI tracking and data-driven decision-making
•Automated recurringExcel-based reporting workflows usingVBA, implementing data validation, transformation, and scheduling logic,
reducing report preparation time by42%and improving data consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 to ship iterative product updates for DeepCover, using engagement metrics, telemetry data, and user feedback
to drive measurable feature prioritization and product improvements
•Tracked sprint progress, product delivery metrics, and QA issues through JIRA workflows, managing backlog and sprint planning to maintain
fast iteration cycles and on-time milestone delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built an end-to-end ML system in Python using LightGBM to assess consumer credit risk from transaction data, including feature engineering
on behavioral spending patterns, model training, and evaluation across time-series datasets
•Designed an automated decision framework for consumer credit line adjustments, incorporating model outputs and risk thresholds to improve
prediction precision by 20% and enable scalable, risk-aware classification""",

    """TAILORED RESUME — Malhar Gudekar SWE shade inc
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark, Semantic Search, LLM
Re-ranking
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed production RAG search system using FastAPI, PostgreSQL, pgvector, and vector embeddings with LLM re-ranking and
semantic retrieval pipelines
•Designed efficient, fault-tolerant pipelines to chunk, embed, index large document datasets for low-latency vector search and semantic retrieval
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimized PostgreSQL schema with pgvector indexing strategies and query execution plans for high-volume datasets, improving
query performance by 38% in production
•Built production-ready Python search pipeline with embedding strategies, retrieval quality evaluation, and context summarization, improving
accuracy by 43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developed production-grade REST APIs using FastAPI to serve AI search models, implementing validation, monitoring, and
deployment workflows across production systems
•Built data ingestion and integration pipelines enabling large-scale multi-source data processing and unified retrieval across production systems
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure patterns and performance issues in distributed
systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar Software Eng RA Labs
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-basedRAG and agentic AI systemusingFastAPI,PostgreSQL, and vector embeddings for
production applications
•Designed efficient, fault-tolerantETL and async pipelinesto process and index large document datasets for low-latency retrieval systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services powering real-time AI applications for business use cases, enabling high-performance model serving of unstructured
data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design, development, and cloud deployment of AI backend system ingesting wearable data for 100+ users, shipping scalable
features that enabled real-world data collection and analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built robust, production-readyPython generative AI pipelinewith retrieval and context summarization, improving response accuracy by43%
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure patterns and performance issues in distributed
systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of 6 in a startup-like environment to ship AI-driven product features for DeepCover game, using performance insights
and user feedback to prioritize high-impact delivery
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution to ensure
on-time delivery
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar Software Engineer GIGA
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based RAG and agentic AI system using FastAPI, PostgreSQL, and vector embeddings, enabling
conversation-aware AI workflows for production enterprise applications
•Designed fault-tolerant ETL and async pipelines to process, index, and dynamically update large document datasets for low-latency knowledge
retrieval in AI agent systems
•Improved system performance by64%through optimized indexing strategies and pipeline improvements in production environments
•Developed backend services enabling real-time, high-performance AI agent responses to unstructured enterprise data across distributed systems,
supporting natural language processing at scale
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimized PostgreSQL schema and indexing strategies for high-volume agent interaction data, improving query performance by
38% to enable fast context retrieval across production workloads
•Built production-ready Python generative AI pipeline with retrieval and conversation context summarization, improving multi-turn response
accuracy by 43% across agent interactions
•Developed asynchronous backend workflows for real-time, fault-tolerant processing of streaming interaction events, with focus on low-latency
handling and scalability across distributed systems
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highly scalable NLP and generative AI pipelines in Python for enterprise-scale natural language query processing,
reducing processing latency by 41% and improving agent response efficiency
•Built distributed event ingestion pipelines using Kafka and Neo4j Streams for real-time, high-throughput agent activity processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implement validation and scheduling logic, reducing report preparation time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Leveraged AI-assisted analysis of 10000+ player feedback points and gameplay telemetry to identify product opportunities, accelerating feature
prioritization by 35% and informing roadmap decisions
•Collaborated with engineering teams to integrate AI-driven insights into product planning, enabling data-backed feature development and
iterative user experience improvements
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance""",

    """TAILORED RESUME — Malhar Gudekar Software Engineer Haystack
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed production-grade LLM applications in Python, including multi-stage prompt pipelines, tool-integrated agentic workflows,
and RAG patterns with vector embeddings, served via FastAPI with PostgreSQL for scalable enterprise cloud deployment
•Designed and iterated on LLM retrieval components, chunking strategies, embedding generation, context assembly, and reranking, optimizing
prompt pipeline performance for low-latency RAG in production enterprise environments
•Improved LLM application performance by 64% through iterative component tuning and retrieval optimization, validated through structured
testing practices and code review cycles to ensure reliability and accuracy of AI outputs
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built production-ready Python LLM application with tool integrations, retrieval components, and multi-turn context summarization —
improving response accuracy by 43% through iterative prompt pipeline design, component testing, and stakeholder feedback cycles
•Developedasynchronous backend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable LLM and NLP pipelines in Python on GCP, applying modular component architecture and prompt engineering
techniques to reduce processing latency by 41% across high-volume enterprise datasets
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed and developedproduction-grade REST APIs using FastAPIto serve AI models, implementing validation, monitoring, and
automated deployment workflows to ensurescalable integrationacross distributed systems
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Retail Demand Forecasting March 2025
View Project
•Analyzed FMCG retail sales data across product categories and store locations to identify demand trends, seasonal patterns, and inventory
drivers
•Built and evaluated forecasting models, ARIMA, SARIMA, and regression , using RMSE and MAPE, deriving actionable insights on pricing,
promotions, and stock behavior for inventory planning
•Translated analytical findings into business recommendations, reducing simulated stockout and overstock risk across seasonal demand cycles""",

    """TAILORED RESUME — Malhar Gudekar Software Engineer NURO
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker, GCP, BigQuery, GCS, Spark Streaming
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintained scalable batch and streaming data pipelines on GCP and AWS, enabling distributed cloud storage and downstream
analytics consumption at scale
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented workflow orchestration using Airflow and AWS Step Functions, adding continuous testing, data quality checks, logging, retries,
and failure handling to ensure pipeline reliability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed scalable batch ELT pipelines in Python using GCP BigQuery for high-volume datasets in distributed environments,
reducing processing latency by 41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Designed storage systems and processing frameworks for large-scale distributed data, ensuring consistent availability and supporting evaluation
metrics and performance monitoring
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable data processing pipelines using Python, PostgreSQL, and GCP cloud storage layers to support large-scale analytics
and downstream data consumption
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
availability
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built data pipelines and dashboards to present evaluation metrics and performance KPIs, enabling clear comparisons of improvements and
regressions and reducing reporting time by 40%
•Processed large-scale datasets using Python and PySpark for distributed batch processing, implementing transformations, aggregations, and
performance monitoring at scale
•DevelopedSQL queriesto validate, reconcile, and analyze operational data, improving data quality and speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers to deliver data-driven improvements, analytics insights, and system tracking
•ManagedAgile workflowsusing JIRA, tracking delivery, QA issues, and sprint progress to ensure timely and reliable releases
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

    """TAILORED RESUME — Malhar Gudekar Software Engineer Relativity
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed a scalable, multi-tenant RAG and agentic AI platform in Python, hosted on Azure Kubernetes Service (AKS), integrating
GPT-4 APIs for AI traffic routing with async orchestration, rate-limit handling, and fault-tolerant request processing across distributed services
•Designed fault-tolerant async job orchestration pipelines on Azure, implementing retry logic, dead-letter queuing, and distributed backpressure
handling to ensure reliable, high-throughput document processing for downstream AI retrieval services
•Improved end-to-end AI system performance by 64% through optimized indexing and pipeline tuning, supported by comprehensive unit and
integration test suites with static analysis checks in GitHub Actions CI/CD , ensuring reliability across distributed service layers
•Developed backend services enabling real-time, high-performanceAI model servingof unstructured data across distributed systems
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Ownedend-to-end design, development, and integrationof cross-platformAI backend systemingesting wearable data for 100+ users,
enabling scalable data collection and downstream analytics
•Designed and optimizedPostgreSQL schema, indexing strategies, and distributed query execution plansfor high-volume datasets,
improving query performance by 38% in production workloads
•Built robust, production-readyPython generative AI pipelinewith retrieval and context summarization, improving response accuracy by43%
•Developed event-driven, asynchronous backend workflows using Kafka for real-time, fault-tolerant processing of high-volume data streams —
applying domain-driven service boundaries and distributed state management to ensure reliability and fair resource usage across consumers
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP and generative AI pipelinesinPythonto process datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing
•Designed production-grade REST APIs in Python to serve AI models across distributed services, implementing validation, observability, and
deployment via GitHub Actions CI/CD, with coverage and static analysis to maintain reliability in high-throughput, multi-service environments
•Enabled large-scale data processing across social media streams usingdistributed systems and large-scale processingprinciples
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving operational visibility
•Processed and optimized large-scale datasets usingPythonandPySparkto identify failure and performance issues in distributed systems
•DevelopedSQLandgraph queriesto map dependencies, analyze operations, detect data issues, speeding root-cause analysis by26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Developed and maintained20+ Power BIdashboards across Sales, Finance, and Operations for enterprise clients, leveragingSQLandDAX,
enabling KPI tracking and data-driven decisions
•Automated recurringExcel-based workflows usingVBA, implementing validation and scheduling logic, reducing report preparation time by
42%and improving consistency
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers and designers to deliverAI-driven product featuresfor DeepCover game, leveraging feedback and
performance insights for feature prioritization
•Trackedsprintprogress, delivery metrics, andQA issuesthroughJIRA-based workflows, managing backlog and issue resolution
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar System Integeration Engineer Eventus Wholehealth
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages & DSA:Python, SQL, Data Structures & Algorithms (Arrays, Hashing, Trees, Graphs, Dynamic Programming), LeetCode
•Backend & Systems:FastAPI, REST APIs, Microservices, Distributed Systems, ETL Pipelines, Kafka, PySpark
•Databases, Cloud & Tools:PostgreSQL, Neo4j, AWS (S3, EC2, EKS), GCP, Docker, Git
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Owned end-to-end design, development, and systems integration of cross-platform backend for 100+ users, building REST API-based data
collection workflows and enabling reliable downstream analytics and reporting
•Designed and optimized PostgreSQL schema, indexing strategies, and query execution plans for high-volume datasets, improving query
performance by 38% to support low-latency API responses and downstream integrations
•Built robust, production-readyPythonpipeline with retrieval and context summarization, improving multi-turn response accuracy by43%
•Developedbackend workflowsfor real-time, fault-tolerant processing of longitudinal health data with focus on reliability and scalability
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed highlyscalable NLP pipelinesinPythonto process high-volume datasets, reducing processing latency by41%
•Built distributed data ingestion pipelines usingKafkaandNeo4jStreams for real-time, high-throughput processing and pattern detection
•Designed production-grade REST APIs using FastAPI, implementing validation, error handling, monitoring, and alerting, and built automated
deployment workflows to support reliable systems integration across distributed operational environments
•Enabled large-scale data processing across social media streams usingdistributed system architectureprinciples
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable, microservices-based AI system using FastAPI and PostgreSQL, designing REST API integrations and automated
data workflows for production-grade enterprise applications
•Designed fault-tolerant ETL pipelines with fail-safe mechanisms and error handling to process large datasets for low-latency retrieval, ensuring
system reliability and data protection across production environments
•Improved system performance by64%through optimized indexing strategies and pipeline efficiency improvements in production environments
•Developed backend services enabling real-time, high-performance querying of unstructured data across distributed system architectures
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Built interactivePower BIdashboards forlogisticsandmobility KPIs, reducing reporting time by40%and improving visibility into operational
performance across transportation services and decision-making insights
•Processed and optimized large-scale operational datasets usingPythonandPySparkto identify failure patterns, trends, and performance
issues in distributed systems environments
•Developed backend services using Git-based CI/CD workflows, maintaining technical documentation and architecture diagrams to support
reliable deployment across distributed, high-availability environments
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Science Intern Mumbai, IN
•Developed and maintained 20+ Power BI dashboards across Finance and Operations for enterprise clients, using SQL data extraction and DAX
to build reports and dashboards supporting operational KPI tracking and decision-making
•Automated recurringExcel-based reporting workflows usingVBA, implementing data validation, transformation, and scheduling logic,
reducing report preparation time by42%and improving data consistency across weekly reporting cycles
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led a cross-functional team of 6 engineers and designers to deliver 10+ product enhancements, translating user requirements and analytics
•Utilized gameplay telemetry and user feedback data to prioritize engineering efforts, improving delivery efficiency and product quality
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end machine learning systemusing Python, Pandas, and LightGBM to forecast customer spending and assess credit risk from
large-scaletime-seriestransaction data, including data preprocessing, feature engineering, model training, and evaluation
•Designed and implementedscalable ETL and feature engineering pipelines, capturing behavioral trends and temporal patterns such as
rolling averages and spending frequency to improve model performance
•Developed adecision framework for credit line adjustments, incorporating model outputs and risk thresholds to improve prediction precision
by 20% and enable risk-aware classification of customers""",

    """TAILORED RESUME — Malhar Gudekar swe data int city of philadelphia
Malhar Gudekar
(217) -766-0681 — gudekar2@illinois.edu — LinkedIn — Portfolio — GitHub
Education
University of Illinois Urbana ChampaignAugust 2024 - May 2026
Master of Science, Information Management GPA: 3.8/4
•Coursework: Web Programming, Machine Learning & Cloud, Information Management, Information Consulting, Methods of Data Science
University of Mumbai June 2019 - May 2023
Bachelor of Engineering, Computer Science GPA: 9.25/10
•Coursework: Data Structures & Algorithms, Operating Systems, Computer Networks, Object-Oriented Programming, Machine Learning, NLP
Skills
•Languages:Python, SQL, Java(leetcode), C++(leetcode)
•Data Engineering:ETL/ELT Pipelines, Data Modeling, Snowflake, PySpark, Workflow Orchestration (Airflow, Step Functions, AWS Glue)
•Cloud & Tools:AWS (S3, EC2, EKS), PostgreSQL, Neo4j, Git, CI/CD, Docker
Work Experience
University of Illinois Urbana ChampaignMay 2025 - Present
Research Assistant - iSchool Champaign, USA
•Built and maintainedAWS-based scalable data pipelinesto ingest high-volume wearable data for 100+ users, enabling distributed storage in
S3and downstream analytics consumption
•Designed and optimizedSQL-based data models and warehouse tablesin PostgreSQL, applying indexing and query tuning techniques to
improve performance by 38% for large datasets
•Implemented workflow orchestration using AWS Step Functions, adding data quality checks, logging, retries, and failure handling, and
maintained clear technical documentation for data flows and integration processes
Research Assistant - CHI AI in Infodemic ManagementJanuary 2025 - May 2025
•Designed and deployed Python ELT pipelines consuming external APIs and processing structured JSON datasets across distributed environ-
ments, reducing processing latency by 41%
•Built distributed real-time ingestion pipelines usingKafkaandNeo4j, enabling streaming data processing, transformation, and graph-based
analytics at scale
•Applieddistributed data processing and big data principlesto handle large-scale streaming data and ensure consistent data availability
Business Intelligence Group August 2025 - December 2025
Technical Consultant Champaign, USA
•Built and deployed scalable data integration pipelines using FastAPI and PostgreSQL, consuming internal and external APIs with structured
JSON data to support downstream applications and cross-system data flows
•Designed fault-tolerantETL workflowsfor ingesting and transforming high-volume document datasets, ensuring low-latency and reliable data
•Developed backend services and usedGit-based CI/CD workflowsto enable reliable deployment and real-time querying across distributed
and high-availability environments
Swift Mobil Software Solutions ProviderJuly 2023 - October 2023
Data Analyst Mumbai, IN
•Builtdata pipelinesfeedingPower BI dashboardsfor logistics KPIs, reducing reporting time by40%and improving data availability for
business decision-making
•Processed large-scale datasets usingPythonandPySpark distributed processing, implementing transformations and aggregations for
performance monitoring
•Developed and maintained SQL queries and database objects to validate, reconcile, and analyze operational data, improving data integrity and
accelerating root-cause analysis by 26%
Pscope Technologies Pvt. Ltd. January 2023 - June 2023
Data Analyst Mumbai, IN
•Built and maintainedSQL-based data pipelinessupportingPower BI dashboards, designing data warehouse models, writing complex joins
and aggregations, and ensuring delivery of analytics-ready datasets across business functions
•Automateddata transformation workflowsusing VBA, implementing validation checks, error handling, and scheduling logic to streamline
large-scale data processing and cut reporting time by42%
Stu/Dio at Illinois August 2025 - Present
Project Manager Champaign, USA
•Led cross-functional team of6engineers to deliver data-driven improvements, analytics insights, and system tracking
•Managed Agile workflows using JIRA, tracking QA issues and sprint progress while maintaining technical documentation for system changes
and supporting production deployments under established review processes
Projects
Scalable ML System for Customer Risk PredictionMarch 2025
UIUC Hackathon
•Built anend-to-end data pipelineusing Python, Pandas, and LightGBM to process large-scaletime-seriestransaction data, including ingestion,
transformation, feature engineering, and model integration
•Designed and implementedscalable ETL and feature engineering pipelinesfor large datasets, capturing behavioral trends and temporal
patterns to improve model performance
•Developed adata-driven decision framework, incorporating pipeline outputs and risk thresholds to improve prediction precision by 20% and
enable scalable analytics workflows""",

]