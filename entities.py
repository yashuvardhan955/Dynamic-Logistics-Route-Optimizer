import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GeoNode:
    """Models coordinate placements for regional fulfillment centers."""
    def __init__(self, node_id, longitude, latitude, resource_demand=15):
        self.node_id = node_id
        self.x = longitude
        self.y = latitude
        self.demand = resource_demand
        logging.debug(f"GeoNode {self.node_id} mapped at position ({self.x}, {self.y}).")

class AssetTruck:
    """Abstract representation tracking dynamic vehicle logistics limits."""
    def __init__(self, truck_id, capacity_limit=250):
        self.truck_id = truck_id
        self.max_capacity = capacity_limit
        self.current_load = 0
        self.route_history = []

    def load_inventory(self, product_weight):
        if self.current_load + product_weight > self.max_capacity:
            logging.warning(f"Capacity breached for vehicle {self.truck_id}. Payload rejected.")
            return False
        self.current_load += product_weight
        return True
