import random

def generate(data):
    thing = random.randint(-100, 100)
    data['params']['variable'] = thing
    data["correct_answers"]["answer"] = thing
    
