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
        event = extract_event(description)
        result = generate_confirmation(json.dumps(event))
        print(result)
    else:
        print("Event is not happening")


if __name__ == "__main__":
    run()
