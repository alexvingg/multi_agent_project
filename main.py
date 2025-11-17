"""
Multi-Agent Chat System with specialized agents for weather, politics, and sports.

This module creates a group chat system with multiple AI agents, each specialized
in different domains (weather, politics, and football/soccer). Users can interact
with all agents in a single conversation.
"""

import logging
from autogen import ConversableAgent, UserProxyAgent, GroupChat, GroupChatManager, register_function
from multi_agent_chat.weather_tool import obter_clima
from dotenv import load_dotenv
from autogen.oai.openai_utils import config_list_from_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# LLM Configuration for all agents
llm_config = {
    "config_list": config_list_from_dotenv(),
    "temperature": 0.7
}

# Weather Agent - Specialized in meteorology and weather forecasts
clima_agent = ConversableAgent(
    name="ClimaAgent",
    system_message=(
"""Você é um meteorologista. Quando perguntarem sobre o tempo:
- Primeiro, explique o tipo de clima predominante da cidade (ex: tropical, semiárido, etc.), com base em conhecimento geral da região.
- Se a pergunta tiver múltiplos assuntos, responda apenas à parte que trata de clima.
- Depois, utilize a função 'obter_clima' para buscar a previsão do tempo atual.
- Se a cidade não for informada, peça educadamente para o usuário fornecê-la.
- Retorne as duas partes (clima típico + previsão atual) em uma única resposta natural e fluida.
"""
    ),
    llm_config=llm_config,
)

# Register the weather function as a tool for the weather agent
register_function(
    obter_clima,
    caller=clima_agent,
    executor=clima_agent,
    description="Consulta a previsão do tempo atual para uma cidade usando a API da HGBrasil."
)
logger.info("Weather agent initialized with weather tool")

# Politics Agent - Specialized in Brazilian and international politics
politica_agent = ConversableAgent(
    name="PoliticaAgent",
    system_message=("""Você é um especialista em política brasileira e internacional. 
    - Responda apenas a perguntas relacionadas a política.
    - Se a pergunta tiver múltiplos assuntos, responda apenas à parte que trata de política.
    - Sempre que for mencionada uma cidade ou estado, utilize essa localização para contextualizar com base nas últimas eleições relevantes (municipais, estaduais ou federais).
    """),
    llm_config=llm_config,
)
logger.info("Politics agent initialized")

# Football/Soccer Agent - Specialized in sports commentary
futebol_agent = ConversableAgent(
    name="FutebolAgent",
    system_message="Você é um comentarista esportivo especializado em futebol. Fale apenas sobre futebol, clubes, campeonatos e jogadores. Se a pergunta tiver múltiplos assuntos, responda apenas à parte que trata de esporte.",
    llm_config=llm_config,
)
logger.info("Football agent initialized")

# User Proxy Agent - Represents the human user in the conversation
user_proxy = UserProxyAgent(
    name="Você",
    human_input_mode="ALWAYS",
    code_execution_config=False
)
logger.info("User proxy agent initialized")

# Create group chat with all specialized agents
group_chat = GroupChat(
    agents=[user_proxy, clima_agent, futebol_agent, politica_agent],
    speaker_selection_method="auto",
    select_speaker_auto_llm_config=llm_config,
    max_round=10
)
logger.info("Group chat configured with all agents")

# Group chat manager to coordinate agent interactions
manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)
logger.info("Group chat manager initialized")

# Start the conversation
if __name__ == "__main__":
    logger.info("Starting multi-agent chat session")
    user_proxy.initiate_chat(
        manager,
        silent=False,
        message="Como é o clima em Salvador? E como foram as eleições na Bahia de governador? Em que posição o Brasil ficou na última copa do mundo de futebol?"
    )