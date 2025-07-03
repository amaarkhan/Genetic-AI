from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field



class EmailGeneratorInput(BaseModel):
    """Input schema for EmailGeneratorTool."""
    email_context: str = Field(..., description="The raw idea or purpose of the email provided by the user.")


class EmailGeneratorTool(BaseTool):
    name: str = "EmailGenerator"
    description: str = (
        "Generates a professional and well-formatted email from provided context, "
        "such as a reason or idea for the email. It includes greeting, body, and closing."
    )
    args_schema: Type[BaseModel] = EmailGeneratorInput

    def _run(self, email_context: str) -> str:
        return f"""\
Dear Sir/Madam,

{email_context.strip()}

Best regards,  
Your Name"""