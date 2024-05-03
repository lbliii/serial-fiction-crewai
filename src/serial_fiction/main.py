import os
from dotenv import load_dotenv
load_dotenv()

from crew import SerialFictionCrew

story_concept = "The series is called Seven Halos. It starts on Halloween night when a gay man, aged 27, finds a techy-looking halo hovering on the ground of the new york subway and decides to use it as part of his cliche angel costume for the party he's on his way to. Unknowingly, He's now thrown into a galactic war between 6 other angels fighting for control of the universe. The angel who collects all 7 halos will have the power to reshape the universe in their image. The premise is a mix of sci-fi, fantasy, and comedy. Think of it as a mix of Lord of The Rings and Scott Pilgrim vs The World. A bit absurd, a bit epic, and a bit funny. The Halo is sentient and has a personality, similar to Sauron's ring or the sorting hat."

def run():
    inputs = {
        "story_concept": story_concept
    }
    SerialFictionCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()   