class Workout:
    def __init__ (self, name: str, weight: float, reps: int, sets: int):
        self.name: str = name
        self.weight: float = weight
        self.reps: int = reps
        self.sets: int = sets
    
    def __str__(self):
<<<<<<< HEAD
        return f"{self.name}, {self.weight}, {self.reps}, {self.sets}"
=======
        return f"{self.name}, {self.weight}, {self.reps}, {self.sets}"
    
    
>>>>>>> refs/remotes/origin/main
