"""Configuration management module for the multi-agent chat system."""

import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class Config:
    """Configuration class to manage environment variables and settings."""
    
    @staticmethod
    def get_hg_brasil_api_key() -> Optional[str]:
        """
        Get the HG Brasil API key from environment variables.
        
        Returns:
            The API key if found, None otherwise.
        """
        api_key = os.getenv("HG_BRASIL_API_KEY")
        if not api_key:
            logger.warning("HG_BRASIL_API_KEY environment variable not set")
        return api_key
    
    @staticmethod
    def get_openai_api_key() -> Optional[str]:
        """
        Get the OpenAI API key from environment variables.
        
        Returns:
            The API key if found, None otherwise.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.warning("OPENAI_API_KEY environment variable not set")
        return api_key
    
    @staticmethod
    def validate_required_keys() -> bool:
        """
        Validate that all required API keys are set.
        
        Returns:
            True if all required keys are set, False otherwise.
        """
        hg_key = Config.get_hg_brasil_api_key()
        openai_key = Config.get_openai_api_key()
        
        if not hg_key:
            logger.error("Missing required environment variable: HG_BRASIL_API_KEY")
            return False
        
        if not openai_key:
            logger.error("Missing required environment variable: OPENAI_API_KEY")
            return False
        
        logger.info("All required API keys are configured")
        return True


# Configuration constants
DEFAULT_LLM_TEMPERATURE = 0.7
DEFAULT_MAX_ROUNDS = 10
DEFAULT_TIMEOUT = 10  # seconds for API calls
