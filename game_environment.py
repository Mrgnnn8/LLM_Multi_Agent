from bot import Seeker, Oracle

class GameEnvironment:
    def __init__(self, seeker: Seeker, oracle: Oracle):
        self.seeker = seeker
        self.oracle = oracle
        self.score = 100
        self.question_budget = seeker.question_budget
        self.game_over = False
        self.guess = None
        self.correct = None

    def run(self):
        print(f"The chosen country: {self.oracle.hidden_country}")
        print(f"Game starting...\n")

        #print("=== SEEKER PROFILE ===")
        #print(self.seeker.profile())
        #print("=== ORACLE PROFILE ===")
        #print(self.oracle.profile())

        while self.seeker.questions_asked < self.question_budget:
            question = self.seeker.act()
            print(f"Seeker: {question}")

            self.score -= 10

            answer = self.oracle.action(question)
            print(f"Oracle: {answer}")
 
            print(f"Questions remaining: {self.question_budget - self.seeker.questions_asked}")

            self.seeker.update_history(question, answer)
            self.oracle.update_history(question, answer)

        self.guess = self.seeker.make_guess()
        self.correct = self.guess.lower() == self.oracle.hidden_country.lower()
        if not self.correct:
            self.score = 0
        self.game_over = True

        print(f"\nSeeker's final guess: {self.guess}")
        print(f"Correct answer: {self.oracle.hidden_country}")
        print(f"Correct: {self.correct}")
        print(f"Score: {self.score}")

    def result(self) -> dict:
        if not self.game_over:
            return None
        return {
            "guess": self.guess,
            "correct_answer": self.oracle.hidden_country,
            "correct": self.correct,
            "question_asked": self.seeker.questions_asked,
            "score": self.score
        }