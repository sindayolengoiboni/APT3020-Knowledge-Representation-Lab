"""
Medical Expert System - Knowledge Representation Lab
APT 3020B Practical Assignment 3

A simple rule-based expert system to diagnose possible illnesses based on symptoms.
"""

import json
import os


class MedicalExpertSystem:
    """
    A knowledge-based expert system for medical diagnosis.
    Uses rule-based inference to suggest possible illnesses based on symptoms.
    """
    
    def __init__(self, knowledge_base_file='knowledge_base.json'):
        """
        Initialize the expert system with knowledge base.
        
        Args:
            knowledge_base_file: Path to the JSON knowledge base file
        """
        self.knowledge_base = self.load_knowledge_base(knowledge_base_file)
        self.symptoms = self.knowledge_base['symptoms']
        self.diseases = self.knowledge_base['diseases']
        self.rules = self.knowledge_base['rules']
        
    def load_knowledge_base(self, filename):
        """
        Load the knowledge base from a JSON file.
        
        Args:
            filename: Path to the JSON file
            
        Returns:
            Dictionary containing the knowledge base
        """
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
            return None
    
    def display_symptoms(self):
        """Display all available symptoms for user selection."""
        print("\n" + "-"*50)
        print("AVAILABLE SYMPTOMS")
        print("-"*50)
        for i, symptom in enumerate(self.symptoms, 1):
            print(f"{i}. {symptom.replace('_', ' ').title()}")
        print("-"*50 + "\n")
    
    def get_user_symptoms(self):
        """
        Get symptoms from the user.
        
        Returns:
            List of symptoms selected by the user
        """
        self.display_symptoms()
        user_symptoms = []
        
        print("Enter the numbers of symptoms you have (comma-separated).")
        print("Example: 1,2,7")
        
        try:
            input_str = input("Your symptoms (or 'q' to quit): ").strip()
            
            if input_str.lower() == 'q':
                return None
            
            indices = [int(x.strip()) - 1 for x in input_str.split(',')]
            
            for idx in indices:
                if 0 <= idx < len(self.symptoms):
                    user_symptoms.append(self.symptoms[idx])
                else:
                    print(f"Invalid symptom number: {idx + 1}")
            
            return user_symptoms
        
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            return self.get_user_symptoms()
    
    def infer_disease(self, user_symptoms):
        """
        Apply inference rules to determine possible diseases.
        
        Args:
            user_symptoms: List of symptoms reported by user
            
        Returns:
            List of tuples (disease, confidence, matching_symptoms)
        """
        if not user_symptoms:
            return []
        
        diagnosed_diseases = []
        user_symptoms_lower = [s.lower() for s in user_symptoms]
        
        # Check each rule
        for rule in self.rules:
            disease = rule['disease']
            required_symptoms = rule['symptoms_required']
            confidence = rule['confidence']
            
            # Count how many required symptoms match
            matching_symptoms = [
                symptom for symptom in required_symptoms 
                if symptom in user_symptoms_lower
            ]
            
            # If all required symptoms are present
            if len(matching_symptoms) == len(required_symptoms):
                diagnosed_diseases.append({
                    'disease': disease,
                    'confidence': confidence,
                    'matching_symptoms': matching_symptoms,
                    'required_symptoms': required_symptoms
                })
        
        # Sort by confidence score (highest first)
        diagnosed_diseases.sort(key=lambda x: x['confidence'], reverse=True)
        
        return diagnosed_diseases
    
    def display_diagnosis(self, diagnosis_results, user_symptoms):
        """
        Display the diagnosis results in a formatted way.
        
        Args:
            diagnosis_results: List of diagnosed diseases with confidence
            user_symptoms: List of symptoms provided by user
        """
        print("\n" + "-"*60)
        print("DIAGNOSIS RESULTS")
        print("-"*60)
        
        if not diagnosis_results:
            print("\n⚠️  No matching diseases found for the given symptoms.")
            print("Please consult a healthcare professional for accurate diagnosis.")
        else:
            print(f"\nBased on symptoms: {', '.join([s.replace('_', ' ').title() for s in user_symptoms])}\n")
            
            for i, result in enumerate(diagnosis_results, 1):
                disease = result['disease']
                confidence = result['confidence'] * 100
                matching = result['matching_symptoms']
                
                print(f"{i}. {disease}")
                print(f"   Confidence Level: {confidence:.0f}%")
                print(f"   Matching Symptoms: {', '.join([s.replace('_', ' ').title() for s in matching])}")
                
                # Get disease description
                for d in self.diseases:
                    if d['name'] == disease:
                        print(f"   Description: {d['description']}")
                        break
                print()
        
        print("-"*60)
        print("⚠️  DISCLAIMER: This system is for educational purposes only.")
        print("Please consult a qualified healthcare professional for accurate diagnosis.")
        print("-"*60 + "\n")
    
    def run(self):
        """Run the expert system in interactive mode."""
        print("\n" + "-"*60)
        print("MEDICAL EXPERT SYSTEM - DIAGNOSIS")
        print("Knowledge Representation - Assignment 3")
        print("-"*60)
        
        while True:
            # Get user symptoms
            user_symptoms = self.get_user_symptoms()
            
            if user_symptoms is None:
                print("\nThank you for using the Medical Expert System. Goodbye!")
                break
            
            if not user_symptoms:
                print("Please select at least one symptom.")
                continue
            
            # Perform inference
            diagnosis = self.infer_disease(user_symptoms)
            
            # Display results
            self.display_diagnosis(diagnosis, user_symptoms)
            
            # Ask if user wants to continue
            continue_choice = input("Do you want to check another set of symptoms? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("\nThank you for using the Medical Expert System. Goodbye!")
                break


def main():
    """Main entry point for the application."""
    # Initialize the expert system
    system = MedicalExpertSystem('knowledge_base.json')
    
    if system.knowledge_base is None:
        print("Failed to initialize the system.")
        return
    
    # Run the system
    system.run()


if __name__ == "__main__":
    main()
