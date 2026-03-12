import anthropic
import os

# Connect to Claude
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Your work context — edit this to describe your actual projects!
MY_WORK_CONTEXT = """
I am Stacy Case, Senior Director of Partner-led Growth. 
My current projects include managing partner relationships, 
tracking partner pipeline, and growing revenue through partnerships.
"""

# Ask your agent a question
question = input("What would you like to know about your work? ")

# Send it to Claude with your context
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"Here is context about my work:\n{MY_WORK_CONTEXT}\n\nQuestion: {question}"
        }
    ]
)

# Print the answer
print("\nAgent says:")
print(message.content[0].text)