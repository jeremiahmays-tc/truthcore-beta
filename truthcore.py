import numpy as np
from sklearn.preprocessing import normalize

def analyze_source_lineage(source):
    # Simulated: Score based on source credibility (e.g., known outlets vs. unknown)
    credibility_map = {
        'reputable': 0.9,  # e.g., NYT, BBC
        'neutral': 0.5,    # e.g., blogs
        'unreliable': 0.1  # e.g., known fake news sites
    }
    return credibility_map.get(source.lower(), 0.5)  # Default to neutral

def check_evidence_consistency(evidences):
    # Simulated: Consistency as agreement ratio among evidences
    if not evidences:
        return 0.5
    agreements = np.random.rand(len(evidences))  # Placeholder for real NLP comparison
    return np.mean(agreements)

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

def calculate_confidence(claim, source, evidences=None, source_history=None):
    if evidences is None:
        evidences = []
    if source_history is None:
        source_history = []
    
    # Get individual scores
    lineage_score = analyze_source_lineage(source)
    consistency_score = check_evidence_consistency(evidences)
    reliability_score = evaluate_historical_reliability(source_history)
    manipulation_score = detect_manipulation_signals(claim)
    
    # Weighted average (adjust weights as needed)
    weights = np.array([0.3, 0.3, 0.2, 0.2])
    scores = np.array([lineage_score, consistency_score, reliability_score, manipulation_score])
    normalized_weights = normalize([weights], norm='l1')[0]
    confidence = np.dot(scores, normalized_weights)
    
    return round(confidence * 100, 2)  # Percentage
# Example usage (for testing):
score = calculate_confidence("Claim text here", "reputable", ["evidence1", "evidence2"], [0.8, 0.9])
print(f"Confidence Score: {score}%")
