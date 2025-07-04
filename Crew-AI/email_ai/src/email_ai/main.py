#!/usr/bin/env python
import sys
import warnings
import os
import csv
from datetime import datetime
from email_ai.crew import EmailAi

# Import document loaders - try newer langchain versions first
try:
    from langchain_community.document_loaders import PyPDFLoader, TextLoader
except ImportError:
    # Fallback for older versions
    from langchain.document_loaders import PyPDFLoader, TextLoader

# Try to import optional dependencies
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

try:
    import docx
except ImportError:
    docx = None

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def load_documents(folder_path="./knowledge"):
    documents = []
    if not os.path.exists(folder_path):
        print(f"[!] Folder '{folder_path}' does not exist. No documents loaded.")
        return ""
    
    supported_files = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if filename.endswith(".pdf"):
                try:
                    loader = PyPDFLoader(file_path)
                    docs = loader.load()
                    supported_files.append(filename)
                except Exception as e:
                    print(f"[!] Error loading PDF {filename}: {e}")
                    # Fallback: try to read as text if PyPDF fails
                    try:
                        if PyPDF2:
                            with open(file_path, 'rb') as file:
                                reader = PyPDF2.PdfReader(file)
                                text = ""
                                for page in reader.pages:
                                    text += page.extract_text() + "\n"
                                docs = [type('Document', (), {'page_content': text})]
                                supported_files.append(filename + " (fallback)")
                        else:
                            print(f"[!] PyPDF2 not available for fallback - skipping {filename}")
                            continue
                    except:
                        print(f"[!] Could not read PDF {filename} - skipping")
                        continue
                        
            elif filename.endswith((".txt", ".md")):
                try:
                    loader = TextLoader(file_path)
                    docs = loader.load()
                    supported_files.append(filename)
                except Exception as e:
                    print(f"[!] Error loading text file {filename}: {e}")
                    # Fallback: direct file reading
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                            docs = [type('Document', (), {'page_content': content})]
                            supported_files.append(filename + " (fallback)")
                    except:
                        print(f"[!] Could not read text file {filename} - skipping")
                        continue
                        
            elif filename.endswith(".docx"):
                try:
                    if docx:
                        doc = docx.Document(file_path)
                        text = ""
                        for paragraph in doc.paragraphs:
                            text += paragraph.text + "\n"
                        docs = [type('Document', (), {'page_content': text})]
                        supported_files.append(filename)
                    else:
                        print(f"[!] python-docx not available - skipping {filename}")
                        continue
                except Exception as e:
                    print(f"[!] Error loading DOCX {filename}: {e} - install python-docx")
                    continue
                    
            elif filename.endswith(".csv"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        reader = csv.reader(file)
                        content = "CSV Content:\n"
                        for row_num, row in enumerate(reader):
                            content += f"Row {row_num + 1}: {', '.join(row)}\n"
                    docs = [type('Document', (), {'page_content': content})]
                    supported_files.append(filename)
                except Exception as e:
                    print(f"[!] Error loading CSV {filename}: {e}")
                    continue
                    
            else:
                print(f"[!] Skipping unsupported file type: {filename}")
                continue

            documents.extend(docs)
        except Exception as e:
            print(f"[!] Error loading {filename}: {e}")

    if not documents:
        print("[!] No valid documents found.")
        return ""
    
    print(f"[✓] Loaded {len(supported_files)} documents: {', '.join(supported_files)}")
    return "\n\n".join([doc.page_content for doc in documents])


def run():
    """
    Run the crew.
    """
    email_intent = input("\nWhat do you want the email to be about? (e.g., 'Send today's update to my manager'): ").strip()
    if not email_intent:
        print("❌ Email intent is required.")
        return

    print(f"\n📁 Loading documents from './knowledge' folder...")
    document_text = load_documents()
    if not document_text:
        print("❌ No document content available. Please add documents to the './knowledge' folder.")
        return

    print(f"\n🤖 Generating ready-to-send email for: {email_intent}")
    print("📝 AI agents are analyzing documents and creating your email...")
    print("⚡ The email will be ready to send without any placeholders or editing required...")

    inputs = {
        'topic': email_intent,
        'document_text': document_text,
        'current_year': str(datetime.now().year)
    }

    try:
        result = EmailAi().crew().kickoff(inputs=inputs)
        print(f"\n✅ Ready-to-Send Email Generated Successfully!")
        print(f"📄 Your email has been saved to 'generated_email.md'")
        print(f"🚀 The email is ready to send immediately - no editing required!")
        print(f"💡 Review the email and send it directly to your recipient.")
        
        return result
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("💡 Make sure you have:")
        print("   1. Set up your API key in the .env file")
        print("   2. Installed all required dependencies")
        print("   3. Added documents to the './knowledge' folder")
        print("   4. Included your contact information in the documents")
        return None


def train():
    """
    Train the crew for a given number of iterations.
    """
    if len(sys.argv) < 3:
        print("Usage: python -m email_ai.main train <iterations> <filename>")
        return
        
    inputs = {
        "topic": "Document-based email generation",
        "document_text": load_documents(),
        'current_year': str(datetime.now().year)
    }
    try:
        EmailAi().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        print(f"An error occurred while training the crew: {e}")
        return None


def replay():
    """
    Replay the crew execution from a specific task.
    """
    if len(sys.argv) < 2:
        print("Usage: python -m email_ai.main replay <task_id>")
        return
        
    try:
        EmailAi().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        print(f"An error occurred while replaying the crew: {e}")
        return None


def test():
    """
    Test the crew execution and returns the results.
    """
    if len(sys.argv) < 3:
        print("Usage: python -m email_ai.main test <iterations> <eval_llm>")
        return
        
    inputs = {
        "topic": "Document-based email generation",
        "document_text": load_documents(),
        "current_year": str(datetime.now().year)
    }
    
    try:
        EmailAi().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        print(f"An error occurred while testing the crew: {e}")
        return None


if __name__ == "__main__":
    run()
