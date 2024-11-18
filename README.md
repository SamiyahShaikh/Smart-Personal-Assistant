# Smart Personal Assistant

A smart personal assistant that performs tasks like scheduling, reminders, fetching information, and voice-based commands. The assistant integrates with APIs like Google Calendar for scheduling and uses NLP to understand user commands. The AI can also provide responses, reminders, and personalized suggestions.

## Architecture Overview

1. Frontend: A web interface built with React and Bootstrap for voice input (using Web Speech API) and interaction with the assistant.
2. Backend: Python Flask server handling requests from the frontend, interfacing with NLP models, and interacting with third-party APIs like Google Calendar.
3. ML/NLP Models: Use pre-trained NLP models (e.g., BERT) to process and respond to user queries.
4. Database: Firebase to store tasks, reminders, and user preferences.
5. APIs: Integration with Google Calendar API, OpenWeatherMap, and NewsAPI for external services.
