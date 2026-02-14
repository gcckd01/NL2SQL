# Context-Aware Natural Language to SQL (NL2SQL) Engine

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![NLP](https://img.shields.io/badge/AI-LlamaEmbedder-purple)
![Status](https://img.shields.io/badge/Status-Research_Prototype-green)

## 📌 Overview
This project is an intelligent SQL query generator that translates natural language questions into optimized SQL queries. [cite_start]Unlike traditional template-based systems, this engine utilizes **LlamaEmbedder** for deep semantic understanding and a **Graph-Based Metadata** system to ensure schema accuracy[cite: 6, 7].

 this system addresses the gap between non-technical user intent and complex database syntax. It features a custom query optimization pipeline that has demonstrated **30–35% faster response times** for complex queries involving joins and aggregations.

## 🚀 Key Features
* [cite_start]**Context-Aware Translation:** Uses a fine-tuned LlamaEmbedder (512-dim) to capture semantic relationships between words[cite: 54].
* [cite_start]**Graph-Based Schema Mapping:** Represents database metadata (tables, keys, types) as a graph to navigate relationships efficiently[cite: 57].
* [cite_start]**Predictive Logic:** Auto-detects aggregations (`SUM`, `COUNT`), filters (`WHERE`), and groupings (`GROUP BY`)[cite: 42].
* [cite_start]**Automated Optimization:** Validates syntax and optimizes query structure before execution[cite: 43].

## 🏗️ Architecture
[cite_start]The system follows a multi-stage pipeline approach[cite: 59]:
1.  [cite_start]**NLP & Tokenization:** User input is processed to detect intent and entities[cite: 60].
2.  [cite_start]**Semantic Embedding:** High-dimensional vector generation using LlamaEmbedder[cite: 53].
3.  [cite_start]**Schema Contextualization:** Mapping semantic vectors to the metadata graph[cite: 61].
4.  [cite_start]**SQL Construction:** Clause generation (SELECT, FROM, JOIN) and aggregation analysis[cite: 62, 63].
5.  [cite_start]**Validation:** Final syntax check and performance tuning[cite: 64].

## 🛠️ Installation
```bash
git clone [https://github.com/yourusername/nl2sql-engine.git](https://github.com/yourusername/nl2sql-engine.git)
cd nl2sql-engine
pip install -r requirements.txt
Project report [https://drive.google.com/file/d/1AuLeaRILgSE54DnYURXkVI6J-rBUC0ef/view?usp=sharing]