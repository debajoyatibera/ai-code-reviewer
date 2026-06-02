# 💻 AI-Powered Code Reviewer (Enterprise Edition)

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-blue?style=for-the-badge)](https://code-reviewer-263881708620.us-central1.run.app/)

An enterprise-grade, web-based application that acts as an automated senior software developer. This tool allows users to upload or paste code snippets in various languages (Python, C, JavaScript, HTML/CSS, etc.) and receive instant, structured feedback on bugs, logical errors, and efficiency improvements.

## 🚀 Live Application
**Test the live application here:** [https://code-reviewer-263881708620.us-central1.run.app/](https://code-reviewer-263881708620.us-central1.run.app/)

## ✨ Features
* **Multi-Language Support:** Analyzes code written in Python, C, JavaScript, HTML/CSS, and more.
* **Intelligent Analysis:** Powered by Google's latest `gemini-2.5-flash` model via Vertex AI.
* **Structured Feedback:** Automatically breaks down reviews into:
  1. A brief summary of the code's purpose.
  2. Identification of bugs, logic errors, and syntax issues.
  3. Actionable suggestions for improving efficiency, memory management, and readability.
* **File Uploads:** Supports direct `.py`, `.c`, `.js`, `.html`, and `.txt` file uploads for seamless reviewing.
* **Secure Architecture:** Built without hardcoded API keys, utilizing Google Cloud IAM for secure, enterprise-level authentication.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/) (Python)
* **AI Engine:** Google Cloud [Vertex AI](https://cloud.google.com/vertex-ai) (Gemini 2.5 Flash)
* **Deployment:** Containerized and hosted on [Google Cloud Run](https://cloud.google.com/run)
* **Language:** Python 3

## 🧠 How It Works
The application uses Streamlit for a lightweight, dark-mode responsive frontend. When a user submits code, the app constructs a highly specific prompt injecting the selected programming language and the raw code. This payload is securely transmitted to Google Cloud's Vertex AI platform using Default Application Credentials (IAM), where the Gemini 2.5 Flash model processes the logic and returns a comprehensive markdown-formatted review.

---
*Built as a computer science vacation engineering project.*
