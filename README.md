# BYU-Pathway Missionary Role-Play Training System

An AI-powered training application designed to help BYU-Pathway service missionaries practice conducting new student orientation visits through realistic conversations with AI personas representing prospective PathwayConnect students.

## Overview

This system enables missionaries to develop critical skills including empathy, cultural sensitivity, clear communication, and problem-solving by engaging in safe, repeatable practice scenarios with AI-driven student personas. Each persona represents authentic challenges that missionaries encounter in real orientation visits, including non-member concerns, language barriers, and confidence issues.

## Features

- **Interactive AI Personas**: Practice conversations with three diverse student personas
- **Real-time Chat Interface**: Natural conversation flow powered by OpenAI's GPT-5.1
- **Comprehensive Content Library**: 11+ detailed persona descriptions, system prompts, and training materials
- **Evaluation Framework**: 6-dimension grading rubric for assessing missionary performance
- **Session Memory**: Full conversation history maintained throughout each training session
- **Streamlit-based UI**: Clean, intuitive interface for easy navigation

## Project Structure

```
role-play/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── roleplay-content/              # Complete training content package
│   ├── personas/                  # Student persona descriptions (3 personas)
│   │   ├── jorge-vargas.md       # Non-member with honor code concerns
│   │   ├── katra.md              # Adult learner with low confidence
│   │   └── vitoria.md            # English language learner
│   ├── prompts/                   # LLM system prompts for embodying personas
│   │   ├── jorge-system-prompt.md
│   │   ├── katra-system-prompt.md
│   │   ├── vitoria-system-prompt.md
│   │   └── grading-system-prompt.md
│   ├── rubric/                    # Evaluation framework
│   │   └── grading-rubric.md     # 6-dimension scoring rubric
│   ├── docs/                      # Expansion guides and templates
│   │   ├── persona-creation-guide.md
│   │   ├── persona-template.md
│   │   └── quality-checklist.md
│   └── README.md                  # Content package documentation
├── venv/                          # Virtual environment (created during setup)
├── .env                           # API key configuration
├── .gitignore                     # Git ignore file
└── README.md                      # This file
```

## Student Personas

The system includes three carefully designed personas representing common challenges in PathwayConnect student orientation:

### 1. **Jorge Vargas** - Non-Member with Honor Code Concerns
- **Location**: Guayaquil, Ecuador
- **Age**: 24
- **Challenge**: Worried about honor code requirements and whether he needs to convert to the LDS Church
- **Skills Tested**: Cultural sensitivity to non-members, clarity about policies, respect for other faiths
- **Background**: Customer service professional seeking business management education, has LDS friends but identifies as Catholic

### 2. **Katra** - Adult Learner with Low Confidence
- **Location**: Port Moresby, Papua New Guinea
- **Age**: 41
- **Challenge**: Deep insecurity about returning to school after 25+ years; fears he's not smart enough
- **Skills Tested**: Empathy, validation, connecting support resources, reframing capabilities
- **Background**: Hotel shift supervisor who left school at age 16, carries belief that he lacks intelligence

### 3. **Vitoria da Silva** - English Language Learner
- **Location**: Manaus, Brazil
- **Age**: 28
- **Challenge**: Limited English proficiency (A2 level); doesn't understand English Language Assessment requirement
- **Skills Tested**: Recognizing language barriers, adapting communication, clarity with simple language
- **Background**: Retail store owner with limited formal education, speaks Portuguese and very limited English

## Evaluation Framework

Conversations are evaluated across 6 dimensions using a comprehensive rubric:

1. **Empathy & Active Listening** - Recognizing and responding to student emotions; validation; clarifying questions
2. **Clarity of Communication** - Simple language; avoiding jargon; adapting to comprehension level
3. **Cultural Sensitivity** - Respect for cultural/religious background; avoiding assumptions
4. **Scriptural/Spiritual Approach** - Appropriate testimony; connecting faith to education; spiritual discernment
5. **Accuracy of Information** - Correct policies; distinguishing PathwayConnect from degree programs
6. **Problem Resolution & Next Steps** - Clear action items; connecting to support; addressing concerns

Each dimension is scored 1-5 (Needs Improvement → Exemplary), with actionable feedback provided.

## Setup Instructions

### Prerequisites
- Python 3.12
- OpenAI API key with access to GPT-5.1

### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd role-play
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a `.env` file in the project root:

```bash
touch .env
```

Add your OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

Get your API key from: https://platform.openai.com/api-keys

### 6. Run the Application

```bash
python3 -m streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Subsequent Runs

After initial setup:

```bash
source venv/bin/activate  # Activate virtual environment
python3 -m streamlit run app.py
```

## Usage

### For Missionaries (Current Implementation)

1. **Start the Application**: Launch the Streamlit app as described in setup
2. **Begin Conversation**: The welcome screen greets you with a time-appropriate greeting
3. **Engage with Persona**: Type messages in the chat input to converse with the AI persona
4. **Practice Skills**: Work through the student's concerns using empathy, clarity, and cultural sensitivity
5. **Review Conversation**: Use the copy button to save messages or regenerate responses as needed
6. **Start Fresh**: Click "Clear Conversation" in the sidebar to begin a new practice session

### Current Workflow

The current prototype provides the conversation interface. The full training workflow will include:

```
Select Persona → Conversation Practice → End Session →
AI Evaluation → View Scores & Feedback → Reflect & Improve
```

### Future Enhancements

**Phase 2 - Evaluation Integration** (Planned):
- Automated conversation grading using the 6-dimension rubric
- Personalized feedback and improvement recommendations
- Progress tracking across multiple practice sessions

**Phase 3 - Persona Expansion** (Planned):
- 6-12 total personas covering diverse challenges
- Random persona selection for authentic training
- Difficulty levels (beginner, intermediate, advanced)

**Phase 4 - Production Deployment** (Planned):
- User authentication and missionary profiles
- Historical performance tracking and analytics
- Integration with New Missionary Orientation curriculum

## Technical Details

### Technology Stack
- **Frontend**: Streamlit (Python web framework)
- **AI Model**: OpenAI GPT-5.1 via Responses API
- **Configuration**: python-dotenv for environment management
- **State Management**: Streamlit session state

### API Configuration
- **Model**: GPT-5.1 (latest OpenAI flagship model)
- **API Endpoint**: `client.responses.create()`
- **Reasoning Mode**: `{"effort": "none"}` for fast, low-latency responses
- **Memory**: Session-based conversation history (resets on browser refresh)
- **Streaming**: Not currently implemented (planned for future)

### Content Architecture
The system uses a **prompt-based persona embodiment** approach:
- Each persona has a detailed system prompt (~3,800-4,500 words)
- System prompts instruct the LLM to authentically embody the student persona
- Conversation context maintains full message history for realistic dialogue
- Future: Grading prompt (~5,500 words) will evaluate completed conversations

### Estimated Token Usage & Costs

**Per Training Session:**
- System Prompt: ~3,000-5,000 tokens
- Conversation (10-20 exchanges): ~1,000-3,000 tokens
- **Total per conversation**: ~4,000-8,000 tokens

**Future Grading (not yet implemented):**
- Grading Prompt + Transcript: ~6,000-8,000 tokens
- Evaluation Output: ~1,500-2,500 tokens
- **Total per evaluation**: ~7,500-10,500 tokens

**Estimated Cost per Complete Session (with grading):**
- Using GPT-5.1: ~$0.50-0.75 per full training session
- At 100 sessions/month: ~$50-75/month in API costs

## Deployment Options

### Local Development
Follow the setup instructions above. Best for development and testing.

### Streamlit Cloud Deployment

1. **Prepare Repository**:
   - Ensure `.env` is in `.gitignore` (never commit API keys)
   - Push code to GitHub
   - Verify `requirements.txt` is up to date

2. **Deploy to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app" and select your repository
   - Select `app.py` as the main file

3. **Configure Secrets**:
   - In app settings, go to "Secrets"
   - Add your API key in TOML format:
   ```toml
   OPENAI_API_KEY = "sk-your-api-key-here"
   ```
   - Save secrets

4. **Deploy**: Click "Deploy" and wait for app to build

The app automatically handles both local `.env` files (for development) and Streamlit Cloud secrets (for production).

### Alternative Deployment (Future)
- **Render**: Python web service deployment
- **Docker**: Containerized deployment for enterprise environments
- **BYU-Pathway Infrastructure**: Integration with existing missionary training platforms

## Content Package

The `roleplay-content/` directory contains **45,000+ words** of comprehensive training materials:

- **3 Complete Personas**: Detailed backgrounds, personalities, and communication styles
- **4 System Prompts**: LLM instructions for persona embodiment and evaluation
- **6-Dimension Rubric**: Comprehensive evaluation framework with examples
- **Expansion Guides**: Step-by-step instructions for creating additional personas
- **Quality Assurance**: Checklists and templates for content validation

See [roleplay-content/README.md](roleplay-content/README.md) for complete content documentation.

## Project Purpose & Goals

### Educational Objectives
This training system aims to help BYU-Pathway missionaries:
- Develop **empathy** for diverse student backgrounds and challenges
- Practice **active listening** and validation techniques
- Build **cultural sensitivity** and religious respect (especially for non-members)
- Master **clear communication** adapted to language and comprehension levels
- Provide **accurate information** about PathwayConnect policies and resources
- Offer **appropriate spiritual guidance** without pressure or insensitivity
- Create **actionable next steps** that help students feel confident and supported

### Success Metrics
- **Missionary Skill Development**: Pre/post training assessment showing improvement across rubric dimensions
- **Student Outcomes**: Improved orientation visit quality leading to higher student confidence and retention
- **Scalability**: System that can train 100+ missionaries with minimal instructor oversight
- **Cost-Effectiveness**: AI-powered training more scalable than role-play with human actors

## Development Status

### Current Status: Prototype Phase
- ✅ Core conversation interface implemented
- ✅ Complete content package (3 personas, system prompts, rubric)
- ✅ Basic UI with session management
- ✅ OpenAI GPT-5.1 integration with Responses API
- ⏳ Evaluation system (not yet integrated)
- ⏳ Persona selection interface (not yet implemented)
- ⏳ Progress tracking (not yet implemented)

### Next Steps
1. Implement persona selection screen
2. Integrate grading system for post-conversation evaluation
3. Build feedback display interface
4. Add session history and progress tracking
5. User testing with actual missionaries
6. Iterate based on feedback

## Contributing

### Creating New Personas
To expand the training library:
1. Review [roleplay-content/docs/persona-creation-guide.md](roleplay-content/docs/persona-creation-guide.md)
2. Copy [roleplay-content/docs/persona-template.md](roleplay-content/docs/persona-template.md)
3. Research authentic student challenges
4. Develop persona and system prompt
5. Test with LLM and validate using quality checklist
6. Submit for review

### Code Contributions
- Follow existing code structure and conventions
- Test thoroughly with all three personas
- Update documentation as needed
- Consider API cost implications of changes

## License & Ethical Use

**Internal Use Only**: This system is designed for BYU-Pathway Worldwide's internal missionary training purposes.

### Ethical Guidelines
- Use only for training, not for production student interactions without oversight
- Maintain cultural sensitivity and respect in all implementations
- Protect student privacy if using real conversation data for improvements
- Follow BYU-Pathway policies and standards for missionary conduct
- Do not deploy publicly without proper authorization

## Support & Resources

### Documentation
- **Content Package**: See [roleplay-content/README.md](roleplay-content/README.md)
- **Persona Details**: Individual markdown files in `roleplay-content/personas/`
- **Grading Rubric**: [roleplay-content/rubric/grading-rubric.md](roleplay-content/rubric/grading-rubric.md)

### Technical Support
- OpenAI API Documentation: https://platform.openai.com/docs
- Streamlit Documentation: https://docs.streamlit.io
- Python-dotenv: https://github.com/theskumar/python-dotenv

### Project Context
This training system is based on:
- BYU-Pathway new student orientation scenarios
- New Missionary Orientation training materials at missionary.byupathway.org
- PathwayConnect student research and retention data
- Best practices in empathy-based education and cultural sensitivity

## Acknowledgments

**Purpose**: To equip BYU-Pathway service missionaries with the skills to conduct compassionate, effective, culturally sensitive orientation visits that help students feel prepared, supported, and confident about beginning their educational journey.

**Created**: November 2025
**Version**: 1.0 (Prototype)
**Status**: Active Development
