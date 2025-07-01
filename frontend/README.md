# Math RAG Frontend

React-based frontend for the Math College RAG system.

## Features
- Search interface for math problems
- Displays questions and solutions
- Filter results by difficulty/chapter
- Responsive Material UI design

## Technologies
- React 18
- Material UI 5
- Axios
- React Markdown

## Setup
1. Install Node.js 18+ and npm 9+
2. Clone repository
   ```bash
   git clone [repo-url]
   cd frontend
   ```
3. Install dependencies
   ```bash
   npm install
   ```
4. Configure API endpoint
   ```bash
   echo "REACT_APP_API_URL=http://localhost:8000" > .env
   ```
5. Run development server
   ```bash
   npm start
   ```

## Environment Variables
| Variable | Description |
|----------|-------------|
| `REACT_APP_API_URL` | Backend API base URL |

## Available Scripts
- `npm start`: Runs development server
- `npm build`: Creates production build
- `npm test`: Runs tests