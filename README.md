Homework Assignment: Adaptive Personalization Engine

Student Metadata
Name: Nicole Shane P. Tuazon
Section: BSCS - 4D
Date: October 6, 2026

---

🚀 How To Run the Code
This program is written in standard **Python 3** and requires no external third-party dependencies.

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/your/project-folder
   ```
3. Run the application script:
   ```bash
   python app.py
   ```

---
🧠 Personalization Logic & UX Explanation

This project implements a rule-based AI configuration targeting an **E-Learning platform** environment. The system dynamically monitors user states to prevent two classic pitfalls in educational design: *cognitive overload* (frustration from high difficulty) and *boredom* (loss of interest from low difficulty).

Rule 1: Adaptive Remediation Rule
Logic: If `user_quiz_score < 70` → Then `recommend_remedial_material()`
UX Impact: When a student scores below a passing threshold (70%), the system steps in like a digital tutor. It shifts their default dashboard pace to "Beginner" and proactively anchors foundational concepts. This ensures the user isn't forced into advanced concepts before mastering prerequisites, decreasing drop-out rates and boosting student confidence.

 Rule 2: Dynamic Difficulty Escalation Rule
Logic: If `user_daily_streak >= 5` → Then `unlock_challenge_mode()`
UX Impact: Retaining students requires rewarding consistency. If a user builds a high daily retention habit (5+ days active), the platform escalates the experience. Unlocking elite, gamified problem rooms creates an intentional sense of accomplishment and directly rewards user loyalty, keeping high-performing students engaged.
