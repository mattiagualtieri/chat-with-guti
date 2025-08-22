# Chat With Guti

Chat With Guti is an AI-powered chatbot that allows you to interact directly with the professional resume of Mattia Gualtieri. Built for recruiters, hiring managers, and networking contacts, this chatbot provides instant, conversational access to Mattia's career achievements, skills, and experience—24/7, from any device.

## What is it?

Chat With Guti leverages state-of-the-art AI (powered by Gemini) to answer questions about Mattia Gualtieri's background, projects, and expertise. The chatbot is designed to:

- Provide concise, recruiter-friendly answers in real time
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
- Professional, third-person voice and style
- Secure, production-ready deployment with HTTPS (Traefik + Docker)
- Mobile-first, dark mode UI

## How it works

1. **Frontend**: Built with React and Tailwind CSS, the web app provides a sleek chat interface accessible from any device.
2. **Backend**: FastAPI serves as the API layer, orchestrating requests and responses with the help of LangGraph and Gemini LLM.
3. **Deployment**: Both frontend and backend are containerized with Docker and orchestrated with Traefik for secure, scalable deployment. CI/CD is managed via GitHub Actions.

## Getting Started

Clone the repository and see the `compose.yaml` for local or production deployment instructions. You will need Docker and Docker Compose installed.

```bash
git clone https://github.com/mattiagualtieri/chat-with-guti.git
cd chat-with-guti
docker compose up -d
```

The chatbot will be available at [https://chatwithguti.it](https://chatwithguti.it) (or your configured domain).

## License

MIT License. See [LICENSE](LICENSE) for details.

---

Made with ❤️ by Mattia Gualtieri