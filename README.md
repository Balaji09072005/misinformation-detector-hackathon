# AI Misinformation Detector

**A prototype built for the GenAI Exchange Hackathon.**

This project is an AI-powered tool that helps users detect potential misinformation in online articles by scraping the content and analyzing it for manipulative language and tone.

## 🚀 The Problem

The rapid spread of fake news and misinformation across social media in India poses a severe threat, leading to social unrest, public health crises, and financial scams. This project aims to provide users with an accessible tool to critically evaluate the content they consume.

## ✨ Our Solution

Our web application allows a user to paste a URL of a news article. The backend, built with Python and Flask, scrapes the article's content. This content is then analyzed for markers of misinformation (using a smart simulation). The final report, including a tone analysis, is displayed to the user on a clean, modern interface.

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **AI:** Dynamic Simulation of a Generative AI Model's output
* **Deployment:** The frontend is deployed on Netlify.

## ⚙️ How to Run This Project Locally

1.  Download and unzip the code.
2.  Open the project in VS Code.
3.  In a terminal, navigate to the `backend` folder: `cd backend`
4.  Create and activate a virtual environment: `python -m venv venv` and then `venv\Scripts\activate`
5.  Install the required libraries: `python -m pip install -r requirements.txt`
6.  Run the backend server: `python app.py`
7.  In the VS Code explorer, right-click `frontend/index.html` and select "Open with Live Server".
