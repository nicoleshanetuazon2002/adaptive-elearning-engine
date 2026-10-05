"""
Adaptive E-Learning Personalization Engine
Author: Nicole Shane P. Tuazon
Date: October 6, 2026
"""

class UserProfile:
    def __init__(self, name: str, quiz_score: float, daily_streak: int):
        self.name = name
        self.quiz_score = quiz_score        # Grade out of 100
        self.daily_streak = daily_streak    # Consecutive days active
        self.learning_pace = "Standard"     # Default system behavior
        self.challenge_unlocked = False     # Default status

def evaluate_adaptive_rules(user: UserProfile) -> None:
    print(f"\n--- Processing Profile for {user.name} ---")
    print(f"Current Status -> Quiz Score: {user.quiz_score}%, Streak: {user.daily_streak} days")
    
    # -------------------------------------------------------------------------
    # Rule 1: Adaptive Remediation Rule
    # If a student struggles on assessment, automatically downshift complexity
    # and surface core foundational topics.
    # -------------------------------------------------------------------------
    if user.quiz_score < 70:
        user.learning_pace = "Beginner (Remedial)"
        print("\n[Rule 1 Triggered] Action: Recommending foundational material.")
        print(" -> System Message: We noticed you had trouble with the last quiz.")
        print(" -> Action: Dynamic study guides and practice blocks have been added to your dashboard.")
    else:
        print("\n[Rule 1 Skipped] Action: User maintains standard or advanced pace.")

    # -------------------------------------------------------------------------
    # Rule 2: Dynamic Difficulty Escalation Rule
    # If a student maintains a high activity streak, reward their momentum
    # by unlocking gamified "Challenge Mode" modules to prevent boredom.
    # -------------------------------------------------------------------------
    if user.daily_streak >= 5:
        user.challenge_unlocked = True
        print("\n[Rule 2 Triggered] Action: Unlocking Challenge Mode!")
        print(f" -> System Message: Awesome consistency! {user.daily_streak}-day streak milestone hit.")
        print(" -> Action: Elite-tier problem sets are now live on your sidebar.")
    else:
        print("\n[Rule 2 Skipped] Action: Challenge Mode locked. Keep building your daily habit!")

    # Summary Output
    print(f"\nUpdated Application State -> Pace: {user.learning_pace} | Challenge Unlocked: {user.challenge_unlocked}")

# --- Test Executions mimicking dynamic real-world student behaviors ---
if __name__ == "__main__":
    # Case A: Struggling user with low consistency
    student_a = UserProfile(name="Alex", quiz_score=62.5, daily_streak=2)
    evaluate_adaptive_rules(student_a)
    
    # Case B: High-performing, dedicated user
    student_b = UserProfile(name="Sam", quiz_score=94.0, daily_streak=7)
    evaluate_adaptive_rules(student_b)
