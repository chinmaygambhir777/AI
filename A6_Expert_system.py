# -------------------------------
# Expert System: Hospital Diagnosis Assistant
# -------------------------------

# Global Knowledge Base
DISEASES = {
    "Common Cold": ["sneezing", "runny_nose", "mild_cough"],
    "Flu": ["fever", "body_pain", "weakness"],
    "COVID-19": ["fever", "dry_cough", "breathing_problem"],
    "Anemia": ["weakness", "paleness", "dizziness"],
    "Diabetes": ["frequent_urination", "increased_thirst", "fatigue"],
    "Migraine": ["headache", "nausea", "sensitivity_to_light"]
}

# Global Questions
QUESTIONS = {
    "sneezing": "Are you sneezing frequently?",
    "runny_nose": "Do you have a runny nose?",
    "mild_cough": "Do you have mild cough?",
    
    "fever": "Do you have fever?",
    "body_pain": "Are you experiencing body pain?",
    "weakness": "Do you feel weakness or low energy?",
    
    "dry_cough": "Do you have dry cough?",
    "breathing_problem": "Are you facing breathing problems?",
    
    "paleness": "Does your skin look pale?",
    "dizziness": "Do you feel dizziness often?",
    
    "frequent_urination": "Are you urinating frequently?",
    "increased_thirst": "Do you feel excessive thirst?",
    "fatigue": "Do you feel tired frequently?",
    
    "headache": "Do you have severe headaches?",
    "nausea": "Do you feel nausea?",
    "sensitivity_to_light": "Are your eyes sensitive to bright light?"
}


# Function to ask questions
def ask(question):
    while True:
        answer = input(question + " (Yes/No): ").lower()

        if answer in ["yes", "y"]:
            return True

        elif answer in ["no", "n"]:
            return False

        else:
            print("Please enter Yes or No.\n")


# Main Expert System
def hospital_expert_system():

    print("=" * 60)
    print("     WELCOME TO SMART HOSPITAL EXPERT SYSTEM")
    print("=" * 60)

    # Store user symptoms
    user_symptoms = {}

    # Ask all questions
    for symptom, question in QUESTIONS.items():
        user_symptoms[symptom] = ask(question)

    print("\nAnalyzing symptoms...")
    print("-" * 60)

    diagnosis = {}

    # Match symptoms with diseases
    for disease, symptoms in DISEASES.items():

        match_count = 0

        for symptom in symptoms:
            if user_symptoms[symptom]:
                match_count += 1

        # Calculate matching percentage
        percentage = (match_count / len(symptoms)) * 100

        if percentage > 0:
            diagnosis[disease] = percentage

    # Display results
    if diagnosis:

        print("\nPossible Diagnosis:\n")

        for disease, percentage in diagnosis.items():
            print(f"{disease} --> {percentage:.0f}% Match")

    else:
        print("No disease matched with given symptoms.")

    print("\nNOTE: This system provides only basic guidance.")
    print("Please consult a doctor for proper medical advice.")


# Run Program
hospital_expert_system()
