import time
import random

class ARSI_System:
    def __init__(self):
        self.agents = ["Validation_Agent", "Risk_Reasoning_Agent", "Lifecycle_Agent"]
        
    def simulate_hazard(self, hazard_type):
        print(f"\n[EVENT] New Report: {hazard_type} detected at Lat: 12.97, Long: 77.59")
        time.sleep(1)
        
        # Agent 1: Validation
        trust_score = random.uniform(85, 98)
        print(f"[{self.agents[0]}] -> Source verified. Trust Score: {trust_score:.2f}%")
        
        # Agent 2: Risk Reasoning (The Formula)
        severity = (8 * 1.5) / 2 # Example S = (H*V)/P
        print(f"[{self.agents[1]}] -> Severity calculated for 2-Wheelers: {severity}/10")
        
        # Agent 3: Lifecycle
        print(f"[{self.agents[2]}] -> Live map updated. Setting decay timer: 120 mins.")
        print("--- Alert Broadcasted to nearby HUDs ---")

if __name__ == "__main__":
    system = ARSI_System()
    hazards = ["Open Pothole", "Oil Spill", "Minor Flood"]
    for h in hazards:
        system.simulate_hazard(h)