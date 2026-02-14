class SQLBuilder:
    def __init__(self):
        pass

    def detect_aggregations(self, intent):
        if intent == "AGGREGATE_SUM":
            return "SUM"
        elif intent == "AGGREGATE_COUNT":
            return "COUNT"
        elif intent == "AGGREGATE_AVG":
            return "AVG"
        return None

    def construct_query(self, tables, intent, entities):
        """
        Builds the query strings based on intent and entities.
        Ref: Case 1 & 2 [cite: 153-162].
        """
        table = tables[0] # Primary table
        agg_func = self.detect_aggregations(intent)
        
        # SELECT Clause
        if agg_func:
            select_clause = f"SELECT {agg_func}({table}.RevenueColumn)"
        else:
            select_clause = f"SELECT {table}.*"
            
        # FROM Clause
        from_clause = f"FROM {table}"
        
        # WHERE Clause (Time filters)
        where_conditions = []
        if entities['years']:
            # Case 5: "in 2023" -> YEAR(SaleDate)=2023 [cite: 178]
            for year in entities['years']:
                where_conditions.append(f"YEAR({table}.SaleDate) = {year}")
                
        # WHERE Clause (Literals/Products/Regions)
        if entities['literals']:
            # Case 1: "Widget" -> ProductName='Widget' [cite: 155]
            for lit in entities['literals']:
                # Heuristic: assume literal is a product or region
                where_conditions.append(f"{table}.Attribute = '{lit}'")

        where_clause = ""
        if where_conditions:
            where_clause = "WHERE " + " AND ".join(where_conditions)

        # Assembly
        query = f"{select_clause} {from_clause} {where_clause}"
        return query