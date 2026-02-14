import json
import networkx as nx

class MetadataGraph:
    def __init__(self, schema_path):
        """
        Loads schema metadata into a graph structure for efficient navigation[cite: 57].
        Metadata includes table relationships, types, and keys[cite: 56].
        """
        self.graph = nx.DiGraph()
        self.load_schema(schema_path)

    def load_schema(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
        
        for table in data['tables']:
            self.graph.add_node(table['name'], type='table', columns=table['columns'])
            for col in table['columns']:
                # Add edges for relationships (Foreign Keys)
                if col.get('foreign_key'):
                    self.graph.add_edge(table['name'], col['foreign_key'], relation="FK")

    def find_path(self, table_a, table_b):
        """Finds the join path between two tables."""
        try:
            return nx.shortest_path(self.graph, table_a, table_b)
        except nx.NetworkXNoPath:
            return None