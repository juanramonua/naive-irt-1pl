import numpy as np

__all__ = ["naive_irt_1pl"]


def naive_irt_1pl(dataset):
    """Estimates naive difficulty and ability parameters using a simplified 1PL IRT model (Rasch).

    Args:
        dataset (np.ndarray): [items x participants] matrix of binary responses:
            - 1: Correct response
            - 0: Incorrect response
            - Any other value is treated as unanswered (ignored)

    Returns:
        dict: Dictionary with two keys:
            - 'Difficulty': (1d array) Item difficulty parameters (1 - Facility)
            - 'Ability': (1d array) Participant ability estimates calculated as:
                (sum of item difficulties for correct answers) / 
                (sum of difficulties + facilities for incorrect answers)
                0.5 is used when denominator is zero.

    Notes:
        - Excludes invalid responses (non-0/1 values) from all calculations
        - Ability estimates are constrained between 0 and 1
    """
    
    # === Response Filtering ===
    # Create boolean mask to identify valid responses (0 or 1)
    mask = (dataset == 0) | (dataset == 1)
    
    # Get matrix dimensions
    n_items, n_participants = dataset.shape

    # === Item Parameter Estimation ===
    # Calculate correct responses per item (ignoring invalid entries)
    sum_1 = np.sum((dataset == 1) & mask, axis=1)
    
    # Total valid responses per item (0/1 responses)
    total_responses = np.sum(mask, axis=1, dtype=float)
    
    # Compute item facility (proportion of correct responses)
    # Handles division by zero using out parameter
    facility = np.divide(
        sum_1, 
        total_responses,
        out=np.zeros_like(sum_1, dtype=float), 
        where=total_responses != 0
    )
    
    # Difficulty is inverse of facility
    difficulty = 1 - facility

    # === Participant Ability Estimation ===
    # Calculate weighted sums for ability estimation
    # Use element-wise multiplication with mask to exclude invalid responses
    
    # Sum of item difficulties for correct answers per participant
    sum1_part = np.sum(
        (dataset == 1) * mask * difficulty[:, np.newaxis],
        axis=0
    )
    
    # Sum of item facilities for incorrect answers per participant
    sum0_part = np.sum(
        (dataset == 0) * mask * facility[:, np.newaxis],
        axis=0
    )
    
    # Compute denominator for ability calculation
    denominator = sum1_part + sum0_part
    
    # Ability calculation with default 0.5 for undefined cases
    ability = np.divide(
        sum1_part,
        denominator,
        out=np.full_like(denominator, 0.5, dtype=float),
        where=denominator != 0
    )

    return {'Difficulty': difficulty,'Ability': ability}  
  


if __name__ == "__main__":
    # Example usage
    sample_data = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 0]])
    result = naive_irt_1pl(sample_data)
    print("Item Difficulties:", result['Difficulty'])
    print("Participant Abilities:", result['Ability'])
    
