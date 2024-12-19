# Streamlit Apps Collection

This repository contains multiple Streamlit applications organized by topic.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Apps

To run a specific app:
```bash
streamlit run apps/finance/stock_analyzer.py
```

To use the app launcher:
```bash
streamlit run scripts/run_app.py
```

## Project Structure

- `common/`: Shared utilities and components
- `apps/`: Individual Streamlit applications
- `assets/`: Static files and resources
- `scripts/`: Helper scripts

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

MIT
