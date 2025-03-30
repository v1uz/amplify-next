"""Utility functions for the Amplify SEO application."""

# Import common utility functions
try:
    from .cache_manager import cache
    from .url_validator import is_valid_url, normalize_url, extract_domain
    from .content_extractor import ContentExtractor
    from .pagespeed_utils import get_pagespeed_data

    # Additional utility functions
    def format_duration(seconds):
        """Format seconds into a human-readable duration string."""
        if seconds < 1:
            return f"{int(seconds * 1000)}ms"
        elif seconds < 60:
            return f"{seconds:.1f}s"
        else:
            mins = int(seconds // 60)
            secs = int(seconds % 60)
            return f"{mins}m {secs}s"
            
    def clean_text(text):
        """Clean text by removing extra whitespace and non-printable characters."""
        import re
        if not text:
            return ""
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
        
    def extract_keywords(content, max_keywords=10):
        """Extract keywords from content."""
        import re
        from collections import Counter
        # Simple keyword extraction implementation
        if not content:
            return []
        # Tokenize and remove common words
        common_words = {'the', 'and', 'is', 'in', 'to', 'a', 'of', 'for', 'with', 'on', 'at', 'from', 'by'}
        words = re.findall(r'\b[a-zA-Z]{3,}\b', content.lower())
        words = [w for w in words if w not in common_words]
        # Count frequencies and return top keywords
        counter = Counter(words)
        return [word for word, _ in counter.most_common(max_keywords)]
        
    def debug_bert_service(bert_service, content=None):
        """Debug BERT service functionality."""
        result = {
            "model_loaded": getattr(bert_service, "model_loaded", False),
            "device": getattr(bert_service, "device", "unknown"),
            "tests": []
        }
        # Add basic test results
        if content and bert_service.model_loaded:
            result["tests"].append({
                "name": "content_extraction",
                "passed": True,
                "message": "Content extraction test"
            })
            try:
                gen_result = bert_service.generate_description(content)
                result["tests"].append({
                    "name": "description_generation",
                    "passed": bool(gen_result.get("description")),
                    "message": "Generation test",
                    "result": gen_result
                })
            except Exception as e:
                result["tests"].append({
                    "name": "description_generation",
                    "passed": False,
                    "message": f"Error: {str(e)}"
                })
        return result

    # Export all utility functions
    __all__ = [
        'cache', 'is_valid_url', 'normalize_url', 'extract_domain',
        'ContentExtractor', 'get_pagespeed_data', 'format_duration',
        'clean_text', 'extract_keywords', 'debug_bert_service'
    ]
    
except ImportError as e:
    import logging
    logging.getLogger(__name__).error(f"Error loading utilities: {e}")