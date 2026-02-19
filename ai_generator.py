
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()   # MUST be before Client()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



def generate_battle_card(competitor, update_text):

    prompt = f"""
You are FlytBase's product marketing expert.

Competitor: {competitor}

Competitor update:
{update_text[:3000]}

FlytBase strengths:
- Enterprise drone autonomy platform
- Hardware-agnostic
- Reliable at scale
- Automation-first workflows

Generate:

1. What changed
2. Weakness in competitor feature
3. FlytBase advantage
4. Sales battle card
5. LinkedIn post
6. Email pitch
7. Blog outline

Write in confident enterprise marketing tone.
Return clean markdown. Do NOT use LaTeX or dollar signs.
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text
