"""API package for all endpoint definitions."""

from flask import Blueprint

# Import blueprints
from .main import main_bp
from .analysis import analysis_bp
from .description import description_bp

# Export the blueprints for app registration
__all__ = ['main_bp', 'analysis_bp', 'description_bp']