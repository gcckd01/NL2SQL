# Re-confirming the imports for src/pipeline.py
from .nlp_processor import NLPProcessor
from .embedder import LlamaEmbedderWrapper
from .metadata_manager import MetadataGraph
from .query_builder import SQLBuilder
from .validator import QueryValidator

class NL2SQLPipeline:
    def __init__(self, schema_path):
        self.nlp = NLPProcessor()
        # Initialize Embedder (Using a mock if Llama not available locally)
        self.embedder = LlamaEmbedderWrapper() 
        self.metadata = MetadataGraph(schema_path)
        self.builder = SQLBuilder()
        self.validator = QueryValidator()

    def generate(self, natural_query):
        # 1. Tokenization & Intent
        nlp_data = self.nlp.process(natural_query)
        
        # 2. Semantic Embedding (Paper: "Context Understanding")
        # In a full impl, we use this vector to find similar past queries.
        # For this prototype, we just log it.
        # vector = self.embedder.get_embedding(natural_query)
        
        # 3. Metadata Mapping
        # Map found entities (literals) to schema
        # (Simplified: finding tables mentioned in tokens)
        relevant_tables = []
        for token in nlp_data['tokens']:
            # Check against graph nodes (Case insensitive match)
            for node in self.metadata.graph.nodes:
                if token.lower() in node.lower():
                    relevant_tables.append(node)
        
        # Default to "Sales" if no table found (common in the paper's examples)
        if not relevant_tables:
            relevant_tables = ["Sales"]

        # 4. Construction
        raw_query = self.builder.construct_query(
            tables=relevant_tables,
            intent=nlp_data['intent'],
            entities=nlp_data['entities']
        )
        
        # 5. Validation & Optimization
        final_query = self.validator.optimize(raw_query)
        
        return final_query