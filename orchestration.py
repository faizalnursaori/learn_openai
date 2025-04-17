from pm import PromptManager
from prompt import GENERATE_TITLE_PROMPT, GENERATE_SECTION_PROMPT, GENERATE_CONTENT_PROMPT

class GenerateBlog:
    def __init__(self, topic):
        self.topic = topic
        self.section = {}

    def generate_title(self):
        pm = PromptManager()
        pm.add_message("system", GENERATE_TITLE_PROMPT.format(topic=self.topic))
        pm.add_message("user", "Generate a title for blog.")
        return pm.generate()
    
    def generate_section(self):
        pm = PromptManager()
        pm.add_message("system", GENERATE_SECTION_PROMPT.format(topic=self.topic))
        pm.add_message("user", "Generate the blog section")
        return pm.generate()
    
    def generate_content(self, section_title):
        pm = PromptManager()
        pm.add_message("system", GENERATE_CONTENT_PROMPT.format(section_title=section_title))
        pm.add_message("user", "Generate the content based on section title")
        return pm.generate()
    
def generate_blog():
    client = GenerateBlog("What is the best programming language for learn about AI?")

    title = client.generate_title()
    sections = client.generate_section()

    print(title)
    print(sections)

if __name__ == "__main__":
    generate_blog()