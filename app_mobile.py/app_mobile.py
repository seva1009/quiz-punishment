#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUIZ PUNISHMENT - Mobile Version
Each mistake was punished with time off.
Author: [seva1009]
Version: 1.0
Year: 2026
"""

import os
import sys
import time
import random
from datetime import datetime

# ========== CONFIGURATION ==========
APP_NAME = "Quiz Punishment 📱"
VERSION = "1.0"
AUTHOR = "seva1009"
BASE_PUNISHMENT = 60  # 60 seconds = 1 minute (change to 300 for 5 min)

# ========== MAIN CLASS ==========
class QuizPunishmentApp:
    def __init__(self):
        self.points = 0
        self.consecutive_errors = 0
        self.history = []
        self.user = ""
        
        # Questions database (EASY TO MODIFY)
        self.questions = self.load_questions()
    
    def load_questions(self):
        """Load all quiz questions"""
        return [
            # MATHEMATICS
            {
                "id": 1,
                "category": "Mathematics",
                "difficulty": "Easy",
                "text": "What is 15 + 27?",
                "options": {"A": "40", "B": "42", "C": "45", "D": "50"},
                "correct": "B",
                "explanation": "15 + 27 = 42"
            },
            {
                "id": 2,
                "category": "Mathematics",
                "difficulty": "Medium",
                "text": "What is 8 × 7?",
                "options": {"A": "54", "B": "56", "C": "58", "D": "60"},
                "correct": "B",
                "explanation": "8 × 7 = 56 (multiplication table of 8)"
            },
            {
                "id": 3,
                "category": "Mathematics",
                "difficulty": "Hard",
                "text": "Square root of 144?",
                "options": {"A": "10", "B": "11", "C": "12", "D": "13"},
                "correct": "C",
                "explanation": "12 × 12 = 144"
            },
            
            # GENERAL KNOWLEDGE
            {
                "id": 4,
                "category": "General Knowledge",
                "difficulty": "Easy",
                "text": "Capital of France?",
                "options": {"A": "London", "B": "Berlin", "C": "Paris", "D": "Madrid"},
                "correct": "C",
                "explanation": "Paris is the capital of France"
            },
            {
                "id": 5,
                "category": "General Knowledge",
                "difficulty": "Medium",
                "text": "Largest planet in the solar system?",
                "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
                "correct": "C",
                "explanation": "Jupiter is the largest planet"
            },
            {
                "id": 6,
                "category": "General Knowledge",
                "difficulty": "Hard",
                "text": "Year humans first landed on the Moon?",
                "options": {"A": "1965", "B": "1969", "C": "1972", "D": "1975"},
                "correct": "B",
                "explanation": "Apollo 11 landed on the Moon in 1969"
            },
            
            # SCIENCE
            {
                "id": 7,
                "category": "Science",
                "difficulty": "Easy",
                "text": "H2O is the formula for...?",
                "options": {"A": "Oxygen", "B": "Carbon dioxide", "C": "Water", "D": "Salt"},
                "correct": "C",
                "explanation": "H2O is the chemical formula for water"
            },
            {
                "id": 8,
                "category": "Science",
                "difficulty": "Medium",
                "text": "Main organ of the circulatory system?",
                "options": {"A": "Lung", "B": "Liver", "C": "Heart", "D": "Kidney"},
                "correct": "C",
                "explanation": "The heart pumps blood"
            },
            
            # HISTORY
            {
                "id": 9,
                "category": "History",
                "difficulty": "Medium",
                "text": "Who painted the Mona Lisa?",
                "options": {"A": "Michelangelo", "B": "Leonardo da Vinci", "C": "Picasso", "D": "Van Gogh"},
                "correct": "B",
                "explanation": "Leonardo da Vinci painted the Mona Lisa"
            },
            
            # GEOGRAPHY
            {
                "id": 10,
                "category": "Geography",
                "difficulty": "Medium",
                "text": "Longest river in the world?",
                "options": {"A": "Amazon", "B": "Nile", "C": "Mississippi", "D": "Yangtze"},
                "correct": "A",
                "explanation": "The Amazon River is the longest"
            }
        ]
    
    def clear_screen(self):
        """Clear screen (compatible with Termux and PC)"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_banner(self):
        """Display main banner"""
        self.clear_screen()
        print("\033[1;36m" + "═" * 52 + "\033[0m")
        print("\033[1;35m           🧠 QUIZ PUNISHMENT 📱           \033[0m")
        print("\033[1;36m" + "═" * 52 + "\033[0m")
        print("    Each error = Temporary block")
        print("    Version: {} | Author: {}".format(VERSION, AUTHOR))
        print("\033[1;36m" + "═" * 52 + "\033[0m")
    
    def show_progress(self, current, total):
        """Show progress bar"""
        percentage = (current / total) * 100
        bars = int(percentage / 2)  # 50 characters max
        spaces = 50 - bars
        
        print(f"\n📊 Progress: [\033[1;32m{'█' * bars}\033[0m{'░' * spaces}] {percentage:.1f}%")
        print(f"   Question {current} of {total}")
        print(f"   🏆 Points: {self.points} | ❌ Consecutive errors: {self.consecutive_errors}")
        print("─" * 52)
    
    def calculate_punishment(self):
        """Calculate punishment time (progressive)"""
        base = BASE_PUNISHMENT
        extra = self.consecutive_errors * 30  # 30 extra seconds per consecutive error
        return min(base + extra, 300)  # Maximum 5 minutes
    
    def show_question(self, number, question):
        """Display a question with formatting"""
        self.show_banner()
        self.show_progress(number, len(self.questions))
        
        print(f"\n\033[1;33m[{question['category']}] - Difficulty: {question['difficulty']}\033[0m")
        print(f"\n\033[1;37m{question['text']}\033[0m")
        print("\n" + "─" * 52)
        
        for letter, text in question['options'].items():
            print(f"  \033[1;32m{letter})\033[0m {text}")
        
        print("─" * 52)
    
    def get_answer(self):
        """Get and validate user answer"""
        while True:
            try:
                answer = input("\nYour answer (A/B/C/D) or 'Q' to quit: ").upper().strip()
                
                if answer == 'Q':
                    return None  # Signal to quit
                
                if answer in ['A', 'B', 'C', 'D']:
                    return answer
                
                print("\033[1;31m❌ Error: Only A, B, C or D\033[0m")
                
            except KeyboardInterrupt:
                print("\n\n👋 Exiting quiz...")
                return None
    
    def execute_block(self, seconds):
        """Execute the blocking screen"""
        self.show_banner()
        
        print("\n\033[1;31m" + "╔" + "═" * 48 + "╗" + "\033[0m")
        print("\033[1;31m" + "║" + " " * 10 + "🚫 APPLICATION BLOCKED" + " " * 10 + "║" + "\033[0m")
        print("\033[1;31m" + "╚" + "═" * 48 + "╝" + "\033[0m")
        
        print(f"\n📛 Reason: Error in quiz question")
        
        minutes = seconds // 60
        secs = seconds % 60
        if minutes > 0:
            print(f"⏰ Block time: {minutes} minute{'s' if minutes > 1 else ''} {secs} second{'s' if secs != 1 else ''}")
        else:
            print(f"⏰ Block time: {seconds} second{'s' if seconds > 1 else ''}")
        
        print("\n💡 Use this time to think about the correct answer.")
        print("   You'll do better next time!")
        print("\n" + "─" * 50)
        
        # Countdown
        for i in range(seconds, 0, -1):
            minutes = i // 60
            secs = i % 60
            formatted_time = f"{minutes:02d}:{secs:02d}"
            print(f"\r⏳ Time remaining: \033[1;33m{formatted_time}\033[0m", end='', flush=True)
            time.sleep(1)
        
        print("\n\n\033[1;32m✅ UNBLOCKED! Continuing...\033[0m")
        time.sleep(2)
    
    def record_attempt(self, question, answer, correct):
        """Record attempt in history"""
        self.history.append({
            'question': question['text'],
            'answer': answer,
            'correct': correct,
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'points': self.points
        })
    
    def execute_quiz(self):
        """Execute complete quiz"""
        # Introduction
        self.show_banner()
        
        if not self.user:
            self.user = input("👤 What's your name? ").strip()
            if not self.user:
                self.user = "Player"
        
        print(f"\nHello {self.user}! Welcome to Quiz Punishment.")
        print("\n🎮 GAME RULES:")
        print("• Answer questions with A, B, C, D")
        print(f"• Each error = {BASE_PUNISHMENT//60} minute{'s' if BASE_PUNISHMENT//60 > 1 else ''} block")
        print("• Consecutive errors increase punishment")
        print("• Each correct answer = +10 points")
        print("• Type 'Q' to quit at any time")
        
        input("\nPress Enter to begin...")
        
        # Shuffle questions
        shuffled_questions = self.questions.copy()
        random.shuffle(shuffled_questions)
        
        # Execute questions
        for i, question in enumerate(shuffled_questions, 1):
            self.show_question(i, question)
            answer = self.get_answer()
            
            if answer is None:  # User wants to quit
                print(f"\n👋 Goodbye {self.user}!")
                return
            
            is_correct = answer == question['correct']
            self.record_attempt(question, answer, is_correct)
            
            if is_correct:
                self.points += 10
                self.consecutive_errors = 0
                print(f"\n\033[1;32m✅ CORRECT! +10 points\033[0m")
                print(f"💡 {question['explanation']}")
                print(f"🏆 Total points: \033[1;33m{self.points}\033[0m")
            else:
                self.consecutive_errors += 1
                correct_answer = question['options'][question['correct']]
                print(f"\n\033[1;31m❌ INCORRECT!\033[0m")
                print(f"💡 The answer was: \033[1;32m{question['correct']}) {correct_answer}\033[0m")
                print(f"💡 {question['explanation']}")
                
                # Calculate and apply punishment
                punishment = self.calculate_punishment()
                minutes = punishment // 60
                secs = punishment % 60
                
                if minutes > 0:
                    print(f"\n⏳ Punishment: {minutes} min {secs} sec")
                else:
                    print(f"\n⏳ Punishment: {secs} sec")
                
                print(f"📛 Consecutive errors: {self.consecutive_errors}")
                
                input("\nPress Enter to start blocking...")
                self.execute_block(punishment)
            
            # Pause between questions (except last)
            if i < len(shuffled_questions):
                input("\nPress Enter for next question...")
        
        # Show final results
        self.show_results()
    
    def show_results(self):
        """Show final results"""
        self.show_banner()
        
        print("\n" + "═" * 52)
        print("           🎉 FINAL RESULTS 🎉")
        print("═" * 52)
        
        max_points = len(self.questions) * 10
        percentage = (self.points / max_points) * 100
        
        print(f"\n👤 Player: {self.user}")
        print(f"📊 Total questions: {len(self.questions)}")
        print(f"🏆 Points obtained: {self.points}/{max_points}")
        print(f"📈 Percentage: {percentage:.1f}%")
        
        errors = len([h for h in self.history if not h['correct']])
        print(f"❌ Errors made: {errors}")
        
        if self.history:
            total_time = len(self.history) * 30  # Estimated
            print(f"⏱️  Estimated play time: {total_time//60} min")
        
        print("\n" + "═" * 52)
        print("\n🏅 CLASSIFICATION:")
        
        if percentage == 100:
            print("🌟 PERFECT! Level: Total Genius")
            print("   You deserve no punishment, you're amazing!")
        elif percentage >= 90:
            print("⭐ EXCELLENT! Level: Master")
            print("   Almost perfect, well done.")
        elif percentage >= 70:
            print("👍 VERY GOOD! Level: Advanced")
            print("   Good work, keep it up.")
        elif percentage >= 50:
            print("💪 GOOD! Level: Intermediate")
            print("   You're on the right track, practice more.")
        elif percentage >= 30:
            print("📚 AVERAGE! Level: Beginner")
            print("   You need to study more.")
        else:
            print("🎯 NEED PRACTICE! Level: Novice")
            print("   Don't give up, practice makes perfect.")
        
        print("\n" + "═" * 52)
        
        # Ask to play again
        option = input("\nPlay again? (Y/N): ").upper()
        if option == 'Y':
            self.restart_game()
            self.execute_quiz()
        else:
            print(f"\n👋 Thanks for playing, {self.user}!")
            print("📱 To play again: python app_mobile.py")
    
    def restart_game(self):
        """Restart the game"""
        self.points = 0
        self.consecutive_errors = 0
        self.history = []
        # Don't reset username

# ========== HELPER FUNCTIONS ==========
def check_environment():
    """Check if running in Termux or PC"""
    is_termux = 'com.termux' in sys.executable if hasattr(sys, 'executable') else False
    
    print("\n" + "═" * 52)
    if is_termux:
        print("✅ Environment detected: Termux (Android)")
    else:
        print("💻 Environment detected: PC/Simulation")
        print("💡 For Android, install Termux from Play Store")
    print("═" * 52 + "\n")
    
    return is_termux

def main():
    """Main function"""
    try:
        app = QuizPunishmentApp()
        check_environment()
        app.execute_quiz()
        
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. See you soon!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("🔧 Please report this error.")
        input("\nPress Enter to exit...")

# ========== EXECUTION ==========
if __name__ == "__main__":
    main()