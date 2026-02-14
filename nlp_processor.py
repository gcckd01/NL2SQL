import re
from datetime import datetime

class NLPProcessor:
    """
    Handles preprocessing, tokenization, intent recognition, and entity detection.
    Paper Reference: Section 6 (Model Diagram - Top Right Block) [cite: 104-107].
    """
    
    def __init__(self):
        # Mappings based on Case Studies 1-4 [cite: 153-170]
        self.intent_patterns = {
            r"(?i)(show|give|list|get)": "RETRIEVE",
            r"(?i)(how many|count)": "AGGREGATE_COUNT",
            r"(?i)(sum|total)": "AGGREGATE_SUM",
            r"(?i)(average|avg)": "AGGREGATE_AVG"
        }
        
    def process(self, query):
        """
        Main pipeline for NLP tasks: Tokenization -> Intent -> Entities.
        """
        cleaned_query = self.clean_text(query)
        intent = self.identify_intent(cleaned_query)
        entities = self.extract_entities(cleaned_query)
        tokens = cleaned_query.split()
        
        return {
            "original": query,
            "tokens": tokens,
            "intent": intent,
            "entities": entities
        }

    def clean_text(self, text):
        """Removes special characters and standardizes spacing."""
        text = re.sub(r'[^\w\s\'-]', '', text)
        return text.strip()

    def identify_intent(self, text):
        """
        Determines if the user wants a simple selection or an aggregation.
        """
        for pattern, intent in self.intent_patterns.items():
            if re.search(pattern, text):
                return intent
        return "RETRIEVE" # Default fallback

    def extract_entities(self, text):
        """
        Extracts dates, years, and quoted values (potential table/column values).
        Ref: Case 3 "between 2020 and 2023"[cite: 164].
        """
        entities = {
            "years": [],
            "literals": []
        }
        
        # Extract Years (e.g., 2021, 2023)
        years = re.findall(r'\b(20\d{2})\b', text)
        entities['years'] = [int(y) for y in years]
        
        # Extract potential string literals (e.g., 'Widget', 'USA')
        # Simple heuristic: capitalized words not at the start of sentence
        words = text.split()
        for w in words[1:]: 
            if w[0].isupper() and w.isalpha():
                entities['literals'].append(w)
                
        return entities