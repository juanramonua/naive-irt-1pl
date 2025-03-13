import numpy as np

__all__ = ["naive_irt_1pl"]


def naive_irt_1pl(dataset):
    """Estimates naive difficulty and ability parameters using a simplified 1PL IRT model (Rasch).

    Args:
        dataset: [items x participants] matrix of True/False Values (0 or 1)
         - 1: correct response
         - 0: incorrect response
         - Any other value is treated as unanswered (NaN).

    Returns:
        dict: Dictionary with two keys:
            - 'Difficulty': (1d array) item difficulties, defined as 1 - Facility.
            - 'Ability': (1d array) participant abilities, defined as the sum of difficulties
              of correctly answered items divided by the sum of those difficulties plus the
              sum of facilities of incorrectly answered items. Assigns 0.5 in case of division by zero.
    """
    # Convert invalid responses (neither 0 nor 1) to np.nan
    X_valid = np.where((dataset == 0) | (dataset == 1), dataset, np.nan)

    # Count correct and incorrect responses per item (rows)
    # Note: (np.nan == 1) and (np.nan == 0) are False, so they are excluded from counts
    sum_1 = np.sum(X_valid == 1, axis=1)
    sum_0 = np.sum(X_valid == 0, axis=1)

    # Compute facility: proportion of correct responses per item
    total = sum_1 + sum_0
    # Avoid division by zero by assigning np.nan when total == 0
    facility = np.divide(sum_1, total, out=np.full_like(sum_1, np.nan, dtype=float), where=(total != 0))
    # Item difficulty: 1 - Facility
    difficulty = 1 - facility

    # For each participant (columns):
    # - Accumulate difficulty for correct responses
    # - Accumulate facility for incorrect responses
    # Use boolean masks and broadcasting for vectorized computation
    mask_correct = (X_valid == 1)
    mask_incorrect = (X_valid == 0)

    # Expand difficulty and facility vectors for matrix multiplication
    # Original shape (n_items,) becomes (n_items, 1)
    diff_matrix = difficulty[:, np.newaxis]
    fac_matrix = facility[:, np.newaxis]

    # Sum difficulties for correct responses per participant
    ability_sum1 = np.nansum(mask_correct * diff_matrix, axis=0)
    # Sum facilities for incorrect responses per participant
    ability_sum0 = np.nansum(mask_incorrect * fac_matrix, axis=0)

    # Compute ability, assigning 0.5 where denominator is zero
    total_part = ability_sum1 + ability_sum0
    ability = np.where(total_part == 0, 0.5, ability_sum1 / total_part)

    return {'Difficulty': difficulty, 'Ability': ability}


if __name__ == "__main__":
    # Example usage
    sample_data = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 0]])
    result = naive_irt_1p(sample_data)
    print("Item Difficulties:", result['Difficulty'])
    print("Participant Abilities:", result['Ability'])
