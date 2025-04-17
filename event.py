from pm import PromptManager
from pydantic import BaseModel, Field
from datetime import datetime
import json


class AnalyzeEvent(BaseModel):
    is_event: bool = Field(description="Information of the query if contain an event")
    description: str = Field(description="Description of event")
    confidence_score: float = Field(description="How confidence you are between 0 to 1")


class EventDetail(BaseModel):
    name: str = Field(description="Name of event")
    description: str = Field(description="Description of event")
    date_time: str = Field(description="Date time of event")
    duration: str = Field(description="Duration of event")


def analyze_event(query):
    pm = PromptManager()
    pm.add_message("user", query)

    result = pm.generate_structured(AnalyzeEvent)
    is_event = result.get("is_event")
    description = result.get("description")
    confidence_score = result.get("confidence_score")

    return description, is_event, confidence_score


def extract_event(query):
    today = datetime.today()
    format_date = today.strftime("%d-%m-%Y")

    pm = PromptManager()
    pm.add_message(
        "system",
        f"Extract the event detail based on user query, as additional information today's date is {format_date}",
    )
    pm.add_message("user", query)

    result = pm.generate_structured(EventDetail)
    return result

def get_current_event():
    return """
    Event List :
    
    - name : Meeting with Fabianka
      date : 12 April 2025, 13.00 PM
      duration : 2 Hour

    - name : Meeting with Investor
      date : 14 April 2025, 10.00 AM
      duration : 2 Hour
    """

def aggregate_event(current_event: str, new_event: str):
    pm = PromptManager()
    pm.add_message("system", f"You have list of user's current events, and check if it's already exist. Here is the event: {current_event} ")
    pm.add_message("user", new_event)

    result = pm.generate()

    return result
def generate_confirmation(query):
    pm = PromptManager()
    pm.add_message(
        "system",
        """
        Generate a confirmation message to the user, and ask if it's confirmed
        
        EXAMPLE RESPONSE OUTPUT:
        Hey, i will make an event for you, with this details: follow with the event details
        """,
    )
    pm.add_message("user", query)

    return pm.generate()


def run():
    input_query = input("Query: ")

    description, is_event, confidence_score = analyze_event(input_query)

    if is_event and confidence_score > 0.7:
        current_event= get_current_event()
        new_event = json.dumps(extract_event(description))

        agg_result = aggregate_event(current_event, new_event)
        print(agg_result)
        # result = generate_confirmation(json.dumps(event))
        # print(result)
    else:
        print("Event is not happening")


if __name__ == "__main__":
    run()
