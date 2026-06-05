from entities import AssetTruck, GeoNode

def run_logistics_tests():
    print("[TESTING RUNTIME] Launching infrastructure unit validation sweeps...")
    
    # Validation 1: Capacity enforcement logic
    carrier = AssetTruck(truck_id=1, capacity_limit=50)
    success = carrier.load_inventory(60)
    assert success is False, "Truck entity failed to trap resource volume exceptions."
    print(" -> Validation Step 1: Volume limits successfully trapped.")
    
    # Validation 2: Boundary check
    hub = GeoNode(5, 10, 10, 0)
    assert hub.demand == 0
    print(" -> Validation Step 2: Hub node configuration bounds verified.")
    print("[SUCCESS] All architectural entities functioning within expected targets.")

if __name__ == "__main__":
    run_logistics_tests()
