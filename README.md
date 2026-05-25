# Medical Expert System - Knowledge Representation Lab

## Project Title

**Simple Medical Expert System Using Knowledge Representation**

## Project Description

A rule-based expert system designed to identify possible illnesses based on symptoms reported by users. This system uses knowledge representation and logical inference to diagnose diseases using predefined symptoms and IF-THEN rules.

## Objectives

- Represent medical knowledge using facts and rules
- Design and implement a rule-based expert system
- Apply logical inference to suggest diagnoses
- Organize and document a project using GitHub
- Demonstrate understanding of knowledge representation concepts

## Symptoms Used

The system recognizes the following 10 symptoms:

1. **Fever** - Elevated body temperature
2. **Headache** - Pain in the head region
3. **Cough** - Involuntary expulsion of air
4. **Chest Pain** - Discomfort in the chest area
5. **Sneezing** - Sudden forceful expulsion of air
6. **Runny Nose** - Nasal discharge
7. **Fatigue** - Extreme tiredness
8. **Sore Throat** - Pain in the throat
9. **Vomiting** - Expulsion of stomach contents
10. **Diarrhea** - Abnormal bowel movements

## Diseases Detected

The system can diagnose the following 4 diseases:

1. **Malaria** - A parasitic disease transmitted by mosquitoes
   - Confidence: 85%
2. **Pneumonia** - A lung infection that inflames air sacs
   - Confidence: 80%
3. **Flu** - A viral infection of the respiratory system
   - Confidence: 75%
4. **Food Poisoning** - An illness caused by contaminated food or water
   - Confidence: 70%

## Rules Applied

### Rule 1: Malaria

```
IF Fever AND Headache AND Fatigue → Malaria (85% confidence)
```

### Rule 2: Pneumonia

```
IF Cough AND Chest Pain AND Fatigue → Pneumonia (80% confidence)
```

### Rule 3: Flu

```
IF Sneezing AND Runny Nose AND Sore Throat → Flu (75% confidence)
```

### Rule 4: Food Poisoning

```
IF Vomiting AND Diarrhea AND Fatigue → Food Poisoning (70% confidence)
```

## Technologies Used

- **Python 3.x** - Core programming language
- **JSON** - Knowledge base storage format
- **Standard Library**: `json`, `os` modules

## How to Run the Program

### Prerequisites

- Python 3.6 or higher installed
- `knowledge_base.json` file in the same directory as `main.py`

### Running Steps

1. **Navigate to the project directory:**

   ```bash
   cd medical_expert_system
   ```

2. **Run the main program:**

   ```bash
   python main.py
   ```

3. **Follow the interactive prompts:**
   - View the list of available symptoms
   - Enter the numbers corresponding to your symptoms (comma-separated)
   - Example: `1,2,7` for Fever, Headache, and Fatigue
   - The system will display possible diagnoses with confidence levels
   - Enter 'q' to quit at any time

### Example Session

```
MEDICAL EXPERT SYSTEM - DIAGNOSIS
============================================================

AVAILABLE SYMPTOMS
==================================================
1. Fever
2. Headache
3. Cough
4. Chest Pain
5. Sneezing
6. Runny Nose
7. Fatigue
8. Sore Throat
9. Vomiting
10. Diarrhea
==================================================

Your symptoms (or 'q' to quit): 1,2,7

============================================================
DIAGNOSIS RESULTS
============================================================

Based on symptoms: Fever, Headache, Fatigue

1. Malaria
   Confidence Level: 85%
   Matching Symptoms: Fever, Headache, Fatigue
   Description: A parasitic disease transmitted by mosquitoes

============================================================
DISCLAIMER: This system is for educational purposes only.
Please consult a qualified healthcare professional for accurate diagnosis.
============================================================
```

## Project Structure

```
medical_expert_system/
│
├── README.md                    # This file - Project documentation
├── main.py                      # Main expert system implementation
├── knowledge_base.json          # Knowledge base with facts and rules
├── semantic_network.png         # Semantic network diagram
└── docs/
    └── sample_outputs.txt       # Sample output screenshots/logs
```

## File Descriptions

### main.py

- **MedicalExpertSystem class**: Core system implementation
- **Key Methods**:
  - `load_knowledge_base()`: Loads rules and facts from JSON
  - `get_user_symptoms()`: Interactive symptom input
  - `infer_disease()`: Applies rules to symptoms
  - `display_diagnosis()`: Formats and displays results
  - `run()`: Main interactive loop

### knowledge_base.json

Stores:

- **symptoms**: List of recognized symptoms
- **diseases**: Disease descriptions
- **rules**: IF-THEN rules with confidence levels

## Key Features

✅ Interactive user interface  
✅ Rule-based inference engine  
✅ Confidence scoring  
✅ Multiple disease support  
✅ User input validation  
✅ Clear diagnostic feedback  
✅ Educational disclaimer

## Knowledge Representation Concepts Demonstrated

1. **Facts** - Symptoms and diseases are represented as facts
2. **Rules** - IF-THEN rules define relationships between symptoms and diseases
3. **Inference** - Forward chaining used to match symptoms against rules
4. **Confidence Factors** - Each rule has a confidence score
5. **Knowledge Base** - Centralized storage of medical knowledge in JSON format

## Semantic Network Diagram

The semantic network shows relationships between:

- **Patients** → report → **Symptoms**
- **Symptoms** → indicate → **Diseases**
- **Diseases** → characterized by → **Symptoms**

[Diagram: semantic_network.png]

## Sample Output Screenshots

See `docs/sample_outputs.txt` for example program runs

## Limitations & Future Enhancements

- Current system uses simple rule matching
- Could be extended with Bayesian networks
- Could add more sophisticated reasoning
- GUI/Web interface could improve usability
- Integration with actual medical databases possible

## Bonus Features Implemented

- User input validation
- Confidence scoring system
- Detailed symptom matching explanations
- User-friendly interactive interface

## Potential Bonus Activities

- [ ] Web interface using Flask/Django
- [ ] GUI using Tkinter or PyQt
- [ ] Voice-based interaction using speech recognition
- [ ] Expanded disease database
- [ ] Integration with medical APIs
- [ ] Mobile application

## Important Disclaimer

⚠️ **EDUCATIONAL PURPOSES ONLY**

This system is designed for educational purposes to demonstrate knowledge representation concepts. It is NOT a substitute for professional medical diagnosis. Users should:

- **Always consult qualified healthcare professionals** for accurate diagnosis
- Not rely solely on this system for medical decisions
- Seek immediate professional help for serious symptoms

## Author(s)

- [Your Name/Group Members]

## Date Completed

- May 2026

## References

- APT 3020B - Knowledge Representation Practical Lab
- Knowledge Representation in Artificial Intelligence
- Expert Systems and Rule-Based Systems

## License

Educational use only

---

**Last Updated:** May 2026
