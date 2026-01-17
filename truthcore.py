import numpy as np
from sklearn.preprocessing import normalize
import requests
import json

def analyze_source_lineage(source):
    # Simulated: Score based on source credibility (e.g., known outlets vs. unknown)
    credibility_map = {
        'reputable': 0.9,  # e.g., NYT, BBC
        'neutral': 0.5,    # e.g., blogs
        'unreliable': 0.1  # e.g., known fake news sites
    }
    return credibility_map.get(source.lower(), 0.5)  # Default to neutral

def check_evidence_consistency(evidences, claim, api_key):
    if not api_key:
        return 0.5  # Fallback if no key
    query = claim.replace(" ", "%20")  # URL-encode the claim
    url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?query={query}&key={api_key}"
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        if 'claims' in data and data['claims']:
            positive_ratings = ['true', 'mostly true', 'accurate', 'correct']
            positive_count = sum(1 for c in data['claims'] if any(r.get('textualRating', '').lower() in positive_ratings for r in c.get('claimReview', [])))
            total = len(data['claims'])
            return positive_count / total if total > 0 else 0.5
        return 0.5  # Neutral if no results
    except Exception as e:
        return 0.5  # Fallback on error

def evaluate_historical_reliability(source_history):
    # Simulated: Average past accuracy
    if not source_history:
        return 0.5
    return np.mean([float(h) for h in source_history])

def detect_manipulation_signals(claim):
    # Simulated: Detect sensational words or biases
    sensational_keywords = ['shocking', 'unbelievable', 'exposed']
    score_penalty = sum(word in claim.lower() for word in sensational_keywords) * 0.1
    return max(0.0, 1.0 - score_penalty)

def calculate_confidence(claim, source, evidences=None, source_history=None, api_key=None):
    if evidences is None:
        evidences = []
    if source_history is None:
        source_history = []
    
    # Get individual scores
    lineage_score = analyze_source_lineage(source)
    consistency_score = check_evidence_consistency(evidences, claim, api_key)
    reliability_score = evaluate_historical_reliability(source_history)
    manipulation_score = detect_manipulation_signals(claim)
    
    # Weighted average (adjust weights as needed)
    weights = np.array([0.3, 0.3, 0.2, 0.2])
    scores = np.array([lineage_score, consistency_score, reliability_score, manipulation_score])
    normalized_weights = normalize([weights], norm='l1')[0]
    confidence = np.dot(scores, normalized_weights)
    
    return round(confidence * 100, 2)  # Percentage

# Example usage (for testing):
score = calculate_confidence("Earth is flat", "unreliable", ["NASA says no", "Conspiracy site says yes"], [0.2, 0.3], api_key="AIzaSyA5NAuGX8iSgv6kX2uUru5Em4ISTqRiPQY")  # Replace with real key for test
print(f"Confidence Score: {score}%")
