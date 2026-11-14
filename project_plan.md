# ConceptOS

## 1. Problem Statement
Students often find it difficult to understand large study materials, identify their weak topics and plan their learning effectively. ConceptOS aims to provide an AI-powered platform that analyses study materials, supports personalised learning and tracks student progress.

## 2. Project Objectives
1. Allow students to upload study materials.
2. Extract and understand information from documents.
3. Answer questions based on uploaded materials.
4. Generate quizzes and assessments.
5. Identify learning gaps.
6. Track student progress.
7. Recommend topics for further study.

## 3. Target Users
Primary users: College students who want to understand their study materials, identify knowledge gaps and improve their learning progress.

## 4. Main Features
Module	              What it does
Document Manager	- Uploads and manages PDFs
AI Tutor	        - Answers questions from notes
Knowledge Map	    - Shows relationships between concepts
Assessment Centre	- Generates quizzes and evaluates answers
Learner Profile	    - Tracks topic mastery
Learning Planner	- Suggests what to study next
Dashboard	        - Displays learning progress

## 5. Technologies We Plan to Use
Component	        What it means	                Technology we plan to use
Frontend	        Application interface	        Streamlit
Backend	Handles     Application requests	        FastAPI
AI Engine	        Performs AI tasks	            Python, AI models
Database	        Stores structured information	PostgreSQL
Vector database	    Searches by meaning	            pgvector
File processing	    Reads PDF files	                PyMuPDF      

## 6. What Makes ConceptOS Useful?
The important difference is that ConceptOS should understand your learning progress, not just answer questions

If the student repeatedly makes mistakes in truth tables, ConceptOS can identify that as a possible weak area and recommend practising truth tables.
That is the kind of experience we want to build

Unlike a basic AI chatbot, ConceptOS aims to maintain a learner profile, analyse assessment performance and recommend topics based on identified knowledge gaps.