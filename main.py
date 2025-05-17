import os
from autogen import ConversableAgent, UserProxyAgent, GroupChat, GroupChatManager, register_function
from multi_agent_chat.weather_tool import obter_clima
from autogen.agentchat import AssistantAgent

from dotenv import load_dotenv


from autogen.oai.openai_utils import config_list_from_dotenv

load_dotenv()  

llm_config = {
    "config_list": config_list_from_dotenv(),
    "temperature": 0.7
}

# Agente Clima
clima_agent = ConversableAgent(
    name="ClimaAgent",
    system_message=(
"""Você é um meteorologista. Quando perguntarem sobre o tempo:
- Primeiro, explique o tipo de clima predominante da cidade (ex: tropical, semiárido, etc.), com base em conhecimento geral da região.
-  Se a pergunta tiver múltiplos assuntos, responda apenas à parte que trata de esporte.
- Depois, utilize a função 'obter_clima' para buscar a previsão do tempo atual.
- Se a cidade não for informada, peça educadamente para o usuário fornecê-la.
- Retorne as duas partes (clima típico + previsão atual) em uma única resposta natural e fluida.
"""
    ),

    llm_config=llm_config,
)

# Registrar a função como Tool
register_function(
    obter_clima,
    caller=clima_agent,
    executor=clima_agent,
    description="Consulta a previsão do tempo atual para uma cidade usando a API da HGBrasil."
)

# Agente Política
politica_agent = ConversableAgent(
    name="PoliticaAgent",
    system_message=("""Você é um especialista em política brasileira e internacional. 
    - Responda apenas a perguntas relacionadas a política.
    - Se a pergunta tiver múltiplos assuntos, responda apenas à parte que trata de política.
    - Sempre que for mencionada uma cidade ou estado, utilize essa localização para contextualizar com base nas últimas eleições relevantes (municipais, estaduais ou federais).
    """),
    llm_config=llm_config,
)

# Agente Futebol
futebol_agent = ConversableAgent(
    name="FutebolAgent",
    system_message="Você é um comentarista esportivo especializado em futebol. Fale apenas sobre futebol, clubes, campeonatos e jogadores. Se a pergunta tiver múltiplos assuntos, responda apenas à parte que trata de esporte.",
    llm_config=llm_config,
)

# Agente usuário
user_proxy = UserProxyAgent(
    name="Você",
    human_input_mode="ALWAYS",
    code_execution_config=False
)

speaker_selector = AssistantAgent(
    name="SpeakerSelector",
    llm_config=llm_config,
)

group_chat = GroupChat(
    agents=[user_proxy, clima_agent, futebol_agent, politica_agent],
    speaker_selection_method="auto",
    select_speaker_auto_llm_config=llm_config,
    max_round=10
)

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)

# Início da conversa
user_proxy.initiate_chat(
    manager,
    silent=True,
    message="Como é o clima em Salvador? e como foram as eleicoes na bahia de governador? Em que posicao o brasil na ultima copa do mundo de futebol e quem ele?"
)