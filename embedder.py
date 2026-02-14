import json
import torch
import os
from transformers import AutoTokenizer, AutoModel

class LlamaEmbedderWrapper:
    """
    Wrapper for the embedding model described in Section 5.1 [cite: 51-54].
    """
    def __init__(self, config_path="models/config.json"):
        # Load configuration
        with open(config_path, 'r') as f:
            self.config = json.load(f)['embedder']
            
        print(f"Loading model: {self.config['model_name']}...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.config['model_name'])
        self.model = AutoModel.from_pretrained(self.config['model_name'])
        self.embedding_dim = self.config['dimension']

    def get_embedding(self, text):
        """
        Generates vector representation.
        """
        inputs = self.tokenizer(
            text, 
            return_tensors="pt", 
            padding=True, 
            truncation=True, 
            max_length=self.config['max_sequence_length']
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
            
        # Mean pooling to get a single vector per sentence
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()
        return embeddings