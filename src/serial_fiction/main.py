import os
import fs
from dotenv import load_dotenv
load_dotenv()

from concept import STORY_CONCEPT 
from crew import SerialFictionCrew

story_concept = STORY_CONCEPT

def run():
    inputs = {
        "story_concept": story_concept
    }
    result = SerialFictionCrew().crew().kickoff(inputs=inputs)
    
    # write the result to a at output/result.txt

    print("~~~~~~~~~~~~")
    print(result)
    print(":-:-:-:-:-:-:")

    file = fs.open_fs("output")
    with file.open("result.txt", "w") as f:
        f.write(result)
    

if __name__ == "__main__":
    run()   