# 📚 Enterprise Knowledge Base Q&A System Using Amazon Bedrock (RAG)

## 🚀 Project Overview

This project implements an **Enterprise Knowledge Base Question-Answering System** using **Amazon Bedrock Knowledge Bases (RAG)**.

The system enables users to ask natural language questions about internal company documents and receive **accurate, citation-backed responses**.

It combines:

* **Semantic search (vector retrieval)**
* **Large Language Models (LLMs)**
* **Cloud deployment on AWS**

---

## 🧠 Business Context

Traditional enterprise search systems rely on keyword matching, which:

* fails to understand context
* returns irrelevant results

At the same time, LLMs:

* can generate incorrect answers (hallucinations)
* lack access to private company data

### ✅ Solution

Amazon Bedrock Knowledge Bases solve both problems by:

* retrieving relevant information using embeddings
* generating grounded responses using LLMs

---

## ❗ Problem Statement

Develop a production-ready **RAG (Retrieval-Augmented Generation)** system that:

* allows employees to query internal documents
* returns accurate answers with source citations
* avoids hallucinations for unknown queries

---

## 🏗️ Architecture

```text
User
  ↓
Streamlit Web App
  ↓
Amazon Bedrock Agent Runtime
  ↓
Bedrock Knowledge Base
  ↓
OpenSearch Serverless (Vector Store)
  ↓
Amazon S3 (Private Documents)
  ↓
Response with Citations
```

---

## ☁️ AWS Services Used

* **Amazon S3** → stores internal documents
* **Amazon Bedrock Knowledge Base** → managed RAG system
* **Amazon OpenSearch Serverless** → vector database
* **Amazon EC2** → hosts the application
* **AWS IAM** → secure access control

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit
* Boto3
* AWS Bedrock APIs

---

## 📂 Project Structure

```text
rag_app/
│── app.py               # Streamlit frontend
│── backend.py           # Bedrock integration
│── requirements.txt     # Dependencies
│── README.md
```

---

## ✨ Features

### 🔍 Intelligent Search

* Semantic understanding using embeddings
* Context-aware responses

### 📄 Citation-Based Answers

* Displays source documents (S3 URIs)
* Ensures transparency

### 🧠 Hallucination Control

* Returns safe responses when data is missing

### ☁️ Cloud Deployment

* Fully deployed on AWS EC2
* Accessible via browser

---

## 🌐 Live Application

```text
http://3.93.74.210:8501
```

---

## 🧪 Sample Questions

```text
What is leave policy?
What is reimbursement policy?
What are the working hours?
Summarize all company policies.
What is work from home policy?
```

---

## 📊 Results

* ✅ Accurate answers retrieved from internal documents
* ✅ Multi-document summarization works
* ✅ Unknown queries handled safely
* ✅ Source citations provided

---

## ⚙️ Setup Instructions

### 🔹 Local Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

### 🔹 AWS Deployment (EC2)

1. Launch EC2 instance
2. Connect via SSH
3. Install dependencies
4. Configure AWS credentials
5. Run Streamlit app:

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

---

## 🔐 Security Considerations

* IAM-based access control
* Private documents stored in S3
* Credentials managed securely

---

## 🚀 Future Enhancements

* Add authentication (login system)
* Use IAM roles instead of access keys
* Deploy with HTTPS and custom domain
* Improve UI/UX
* Add chat history and session memory

---

## 🎯 Conclusion

This project demonstrates a complete **end-to-end RAG system** using Amazon Bedrock Knowledge Bases.

It successfully:

* bridges the gap between LLMs and private enterprise data
* provides accurate, context-aware answers
* reduces hallucination risks
* delivers a scalable cloud-based solution

---

## 🙌 Author

**Embadi Anji**

---

## ⭐ Acknowledgement

Built using AWS Bedrock and modern Generative AI concepts.
