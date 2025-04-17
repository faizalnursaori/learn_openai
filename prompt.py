GENERATE_TITLE_PROMPT = """
Generate a proper title from topic: {topic}

IMPORTANT :
- Title must be in clear english
- Title must e engaging not just click bait
"""

GENERATE_SECTION_PROMPT = """
Generate section based on a topic: {topic}

IMPORTANT :
- At least five section
- Output must be on a bullet list
- Do not add any additional information or explanation
"""

GENERATE_CONTENT_PROMPT = """
Generate content based on a section title: {section_title}
"""