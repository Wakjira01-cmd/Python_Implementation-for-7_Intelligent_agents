"""
╔══════════════════════════════════════════════════════════════════╗
║     KNOWLEDGE-BASED AGENT - DEPARTMENT ASSIGNMENT SYSTEM        ║
║     Course: Introduction to Artificial Intelligence (CoSc3112)  ║
║     Name: Wakjira Berhanu                                       ║
║     ID: UGR/20996/16                                            ║
║     Chapter 4: Knowledge Representation and Reasoning           ║
╚══════════════════════════════════════════════════════════════════╝


Knowledge-Based Agent - Department Assignment
Rules: Skill(+2 each) | Interest(+3) | Exam(+5 if eligible) | Decision(highest points)
"""

class DepartmentAgent:
    """Knowledge-based agent using inference rules"""
    
    def __init__(self):
        # Knowledge Base: Department requirements
        self.departments = {
            "Computer Science": {"skills": ["math", "programming", "algorithms"], "interest": "theory", "min": 70},
            "Information Technology": {"skills": ["networking", "hardware", "databases"], "interest": "system", "min": 60},
            "Software Engineering": {"skills": ["programming", "design", "testing"], "interest": "development", "min": 65},
            "Digital Technology": {"skills": ["multimedia", "graphics", "design"], "interest": "creative", "min": 55}
        }
    
    def run(self):
        print("\n=== DEPARTMENT ASSIGNMENT SYSTEM ===\n")
        
        # Get student input
        skills = [s.strip().lower() for s in input("Skills (comma-separated): ").split(",") if s.strip()]
        interest = input("Interest (theory/system/development/creative): ").strip().lower()
        
        # Validate score
        while True:
            try:
                score = int(input("Exam score (0-100): "))
                if 0 <= score <= 100:
                    break
                print("Score must be 0-100")
            except ValueError:
                print("Enter a number")
        
        # Evaluate each department
        print("\n--- EVALUATION ---")
        results = []
        
        for name, req in self.departments.items():
            # Rule 3: Exam eligibility check
            if score < req["min"]:
                print(f"{name}: NOT ELIGIBLE (score {score} < {req['min']})")
                continue
            
            print(f"\n{name}: ELIGIBLE")
            
            # Rule 1: Skill points (+2 per match)
            match = [s for s in skills if s in req["skills"]]
            points = len(match) * 2
            print(f"  Skills: +{points} points (matched: {match if match else 'none'})")
            
            # Rule 2: Interest points (+3 if match)
            if interest == req["interest"]:
                points += 3
                print(f"  Interest: +3 points (matches)")
            else:
                print(f"  Interest: +0 points")
            
            # Rule 3: Exam points (+5)
            points += 5
            print(f"  Exam: +5 points")
            print(f"  TOTAL: {points} points")
            
            results.append((name, points))
        
        # Rule 4: Decision - recommend highest points
        print("\n--- RECOMMENDATION ---")
        
        if not results:
            print("No eligible departments")
            return
        
        highest = max(p for _, p in results)
        best = [n for n, p in results if p == highest]
        
        # Show ranking
        for n, p in sorted(results, key=lambda x: x[1], reverse=True):
            print(f"  {n}: {p} points")
        
        # Final decision
        if len(best) == 1:
            print(f"\nRecommend: {best[0]} with {highest} points")
        else:
            print(f"\nTie between: {' or '.join(best)} ({highest} points each)")


# Run agent
if __name__ == "__main__":
    DepartmentAgent().run()