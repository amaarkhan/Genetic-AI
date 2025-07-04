# Email AI - Document-Based Email Generator

Welcome to the Email AI project, powered by [crewAI](https://crewai.com). This system uses AI agents to analyze documents and generate professional emails based on their content.

## 🚀 Features

- **Multi-format Document Support**: PDF, TXT, MD, DOCX, CSV files
- **Intelligent Document Analysis**: AI agents extract key information and insights
- **Professional Email Generation**: Creates well-structured, business-ready emails
- **Easy Setup**: Simple configuration and usage
- **Fallback Support**: Robust error handling and multiple parsing methods

## 📋 Installation

Ensure you have Python >=3.10 <3.14 installed on your system.

1. **Install UV** (if not already installed):
```bash
pip install uv
```

2. **Install Dependencies**:
```bash
crewai install
```

3. **Set up Environment Variables**:
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
# OR
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🗂️ Project Structure

```
email_ai/
├── knowledge/                   # Place your documents here
│   ├── sample_daily_report.txt  # Example document
│   └── (your documents...)
├── src/email_ai/
│   ├── config/
│   │   ├── agents.yaml          # AI agent configurations
│   │   └── tasks.yaml           # Task definitions
│   ├── crew.py                  # AI crew orchestration
│   └── main.py                  # Main execution script
├── .env                         # Environment variables
├── pyproject.toml               # Project dependencies
└── generated_email.md           # Output email file
```

## 💻 Usage

### Quick Start
```bash
python -m email_ai.main
```

### Step-by-Step Process:

1. **Add Documents**: Place your documents in the `./knowledge` folder
   - Supported formats: PDF, TXT, MD, DOCX, CSV
   - Multiple documents will be analyzed together

2. **Run the Generator**:
   ```bash
   python -m email_ai.main
   ```

3. **Provide Context**: When prompted, describe what you want the email to be about:
   ```
   What do you want the email to be about? Send today's update to my manager
   ```

4. **Get Results**: The system will:
   - Load and analyze your documents
   - Extract key information
   - Generate a professional email
   - Save it as `generated_email.md`

### Example Workflow:
```
=== Document-Aware Email Generator ===

What do you want the email to be about? Send daily project update to my manager

📁 Loading documents from './knowledge' folder...
[✓] Loaded 1 documents: sample_daily_report.txt

🤖 Generating email for: Send daily project update to my manager
📝 AI agents are analyzing documents and creating your email...

✅ Email Generated Successfully!
📄 Your email has been saved to 'generated_email.md'
💡 You can review and edit it before sending.
```

## 🎯 Use Cases

### Daily Reports
- Upload daily work logs or progress reports
- Generate summary emails for managers

### Project Updates
- Share milestone achievements and status updates
- Communicate project progress to stakeholders

### Data Analysis
- Upload CSV files with analysis results
- Create executive summaries of findings

### Meeting Follow-ups
- Convert meeting minutes to action item emails
- Share decisions and next steps with team

## 🔧 Configuration

### Agents (agents.yaml):
- **Document Reader**: Analyzes and summarizes document content
- **Email Writer**: Creates professional emails from analyzed content

### Tasks (tasks.yaml):
- **Document Analysis**: Extracts key information from documents
- **Email Generation**: Creates structured, professional emails

## 🛠️ Dependencies

- `crewai[tools]>=0.140.0` - AI agent framework
- `langchain-community>=0.0.20` - Document loading
- `pypdf2>=3.0.1` - PDF processing
- `python-docx>=1.1.0` - Word document processing
- `pandas>=2.0.0` - Data processing

## 🔍 Troubleshooting

### Common Issues:

1. **No documents found**:
   - Ensure documents are in the `./knowledge` folder
   - Check file formats are supported

2. **Import errors**:
   - Run `crewai install` to install dependencies
   - Ensure Python version is 3.10-3.13

3. **API errors**:
   - Check your API key in the `.env` file
   - Verify internet connection

4. **Document reading errors**:
   - System includes fallback methods for most formats
   - Check file isn't corrupted or password-protected

## 📝 Advanced Usage

### Training the Model
```bash
python -m email_ai.main train <iterations> <filename>
```

### Replay Previous Execution
```bash
python -m email_ai.main replay <task_id>
```

### Testing
```bash
python -m email_ai.main test <iterations> <eval_llm>
```

## 🤝 Contributing

This project is built on the crewAI framework. For more information:
- [crewAI Documentation](https://docs.crewai.com)
- [GitHub Repository](https://github.com/joaomdmoura/crewai)

## 📄 License

This project is built using crewAI and follows their licensing terms.
