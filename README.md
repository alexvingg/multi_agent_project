# Multi-Agent Chat Project

A multi-agent conversational system built with AutoGen that features specialized AI agents for different domains: weather forecasting, politics, and football/soccer.

## Features

- **Weather Agent (ClimaAgent)**: Provides climate information and weather forecasts for Brazilian cities using the HG Brasil API
- **Politics Agent (PoliticaAgent)**: Discusses Brazilian and international politics, including election context
- **Football Agent (FutebolAgent)**: Specialized in football/soccer commentary, teams, championships, and players
- **Multi-Agent Coordination**: Agents automatically collaborate to answer complex, multi-topic questions

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- HG Brasil Weather API key (free tier available at [hgbrasil.com](https://hgbrasil.com/status/weather))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/alexvingg/multi_agent_project.git
cd multi_agent_project
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Add your API keys:
```bash
OPENAI_API_KEY=your_openai_api_key_here
HG_BRASIL_API_KEY=your_hg_brasil_api_key_here
```

## Usage

Run the main script:
```bash
python main.py
```

The system will start a conversation where you can ask questions about:
- Weather conditions in Brazilian cities
- Political topics and elections
- Football/soccer news and information

### Example Questions

- "Como é o clima em Salvador?"
- "Como foram as eleições na Bahia?"
- "Em que posição o Brasil ficou na última copa do mundo?"
- Or combine topics: "Como está o tempo no Rio de Janeiro e quais times de futebol são de lá?"

## Project Structure

```
multi_agent_project/
├── main.py                          # Main application entry point
├── multi_agent_chat/
│   ├── __init__.py
│   └── weather_tool.py              # Weather API integration
├── requirements.txt                  # Python dependencies
├── .env.example                     # Environment variables template
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key for powering the AI agents
- `HG_BRASIL_API_KEY`: Your HG Brasil API key for weather data

### Agent Configuration

You can customize agent behavior by modifying the `system_message` parameter in `main.py`:
- Temperature setting (creativity level)
- Maximum conversation rounds
- Speaker selection method

## Error Handling

The system includes comprehensive error handling:
- API timeout protection
- Input validation
- Detailed error messages
- Logging for debugging

## Logging

The application logs important events and errors. Logs include:
- Agent initialization
- API calls
- Errors and warnings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Troubleshooting

### Common Issues

1. **API Key Not Found**: Ensure your `.env` file is properly configured with valid API keys
2. **Weather Data Not Loading**: Verify your HG Brasil API key is valid and has not exceeded rate limits
3. **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`

## Acknowledgments

- Built with [AutoGen](https://github.com/microsoft/autogen) by Microsoft
- Weather data provided by [HG Brasil](https://hgbrasil.com/)
- Powered by OpenAI's language models