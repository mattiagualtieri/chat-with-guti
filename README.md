# Chat With Guti

**Chat With Guti** is an LLM-powered chatbot that allows you to interact directly with the professional resume of Mattia Gualtieri. This chatbot provides instant, conversational access to Mattia's career achievements, skills, and experience.

## What is it?

Chat With Guti leverages Gemini LLM models to answer questions about Mattia Gualtieri's background, projects, and expertise. The chatbot is designed to:

- Provide concise, user-friendly answers in real time
- Emphasize measurable achievements and real experience
- Never invent information—always stay aligned with the actual resume
- Offer a modern, mobile-friendly chat experience

## Technologies Used

- **Python** — Core backend language
- **FastAPI** — High-performance web framework for the backend API
- **LangGraph** — Advanced orchestration and LLM integration
- **React** — Modern frontend framework for a responsive, interactive UI
- **Docker** — Containerized deployment for both frontend and backend
- **GitHub Actions** — Automated CI/CD for seamless deployment

## Features

- Natural language chat interface to Mattia's resume
- Answers about work experience, skills, projects, and education
- Secure, production-ready deployment with HTTPS (Traefik + Docker)

## How it works

1. **Frontend**: Built with React and Tailwind CSS, the web app provides a sleek chat interface accessible from any device.
2. **Backend**: FastAPI serves as the API layer, orchestrating requests and responses with the help of LangGraph and Gemini LLM.
3. **Deployment**: Both frontend and backend are containerized with Docker and orchestrated with Traefik for secure, scalable deployment. CI/CD is managed via GitHub Actions.

## Demo

The chatbot is available at [https://chatwithguti.it](https://chatwithguti.it)

## License

MIT License. See [LICENSE](LICENSE) for details.

---

This README was kindly written by Gemini 2.5 Pro