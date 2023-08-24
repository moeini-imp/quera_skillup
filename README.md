

```markdown
# Quera SkillUp FastAPI Application

This repository contains a FastAPI application that is part of the Quera SkillUp challenge. The application is designed to provide hints and challenges for participants.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Docker: Make sure you have Docker installed on your system.

### Installation and Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/moeini-imp/quera_skillup.git
   cd quera_skillup
   ```

2. Build the Docker image:

   ```sh
   docker build -t quera-skillup-app .
   ```

### Running the Application with Redis

The Docker image includes both the FastAPI application and a Redis server running on separate ports within the same container.

1. Run the Docker container to start the FastAPI application and Redis server:

   ```sh
   docker run -d -p 8000:8000 -p 6379:6379 quera-skillup-app
   ```

2. Access the FastAPI application:

   Open your web browser and navigate to `http://localhost:8000`.

## Usage

- Access the main route at `http://localhost:8000/skillup/challenge` to receive a hint.
- Follow the instructions provided to progress through the challenges.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to copy and paste this markdown code into your repository's README file and adjust it as needed.
