# FastAPI Chatbot

A modern, extensible chatbot backend built with FastAPI and OpenAI, featuring a clean API, modular architecture, and a beautiful web-based chat interface. This project is designed for rapid prototyping and easy deployment of conversational AI applications.

## Features

- **FastAPI Backend**: High-performance, async API for chat interactions.
- **OpenAI Integration**: Easily connect to OpenAI's GPT models for natural language responses.
- **Modular Structure**: Organized codebase with clear separation of API, core logic, models, and services.
- **Environment Management**: Uses `python-dotenv` and `pydantic-settings` for secure, flexible configuration.
- **Modern Web UI**: Included HTML/CSS/JS chat interface for local testing and demos.
- **Easy Deployment**: Run locally with Uvicorn or deploy to any cloud provider supporting ASGI.

## Project Structure

```
app/
  __init__.py
  main.py                # FastAPI app entrypoint
  api/
    v1/
      endpoints.py       # API endpoints (e.g., /api/)
  core/
    config.py            # Settings and configuration
  models/
    schema.py            # Pydantic models and schemas
  services/
    llm_service.py       # OpenAI (or other LLM) integration
index.html               # Web chat interface
requirements.txt         # Python dependencies
```

## Quickstart

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/fastapi-chatbot.git
cd fastapi-chatbot
```

### 2. Set Up Python Environment

It is recommended to use a virtual environment:

```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/macOS:
source venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with your OpenAI API key:

```
OPENAI_API_KEY=your-openai-api-key
```

You can also configure other settings in `app/core/config.py` or via environment variables.

### 5. Run the Application

```sh
uvicorn app.main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 6. Use the Web Chat Interface

Open `index.html` in your browser. The chat UI will connect to the FastAPI backend at `http://127.0.0.1:8000/api/`.

## API Usage

- **POST /api/**
  - Request: `{ "message": "Hello!" }`
  - Response: `{ "message": "Hi, how can I help you today?" }`

## Customization

- **Change LLM Provider**: Edit `app/services/llm_service.py` to use a different LLM or add custom logic.
- **Add Endpoints**: Extend `app/api/v1/endpoints.py` for more API routes.
- **UI Tweaks**: Modify `index.html` for branding or new features.

## Requirements

- Python 3.8+
- See `requirements.txt` for all dependencies.

## License

MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://openai.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

_Feel free to fork, contribute, and build your own AI-powered chatbots!_
