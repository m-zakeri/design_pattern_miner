import networkx as nx

mediator_pattern = DiGraph()
mediator_pattern.add_nodes_from([ (1, 2, {'type': "as"}), (3, 2, {'type': "as"}), (4, 1, {'type': "as"}), (4, 3, {'type': "as"}), (4, 2, {'type': "ge"}) ])

state_pattern = DiGraph()
state_pattern.add_nodes_from([ (1, 2, {'type': "as"}), (3, 2, {'type': "ge"}) ])

proxy_pattern = DiGraph()
proxy_pattern.add_nodes_from([ (2, 1, {'type': "ge"}), (3, 1, {'type': "ge"}), (2, 3, {'type': "as"}) ])


design_patterns = dict()

design_patterns["abstract_factory"] = nx.DiGraph()
design_patterns["abstract_factory"].add_nodes_from(["ConcreteFactory", "AbstractFactory", ""])