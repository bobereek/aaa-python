def get_mean_by_attribute(data, attribute):
    assert any(attribute in laureate for laureate in data), f"Unknown attribute {attribute}"

    values = [laureate[attribute] for laureate in data if laureate[attribute] is not None]
    return round(sum(values) / len(values), 4)


def get_median_by_attribute(data, attribute):
    assert any(attribute in laureate for laureate in data), f"Unknown attribute {attribute}"

    values = [laureate[attribute] for laureate in data if laureate[attribute] is not None]
    values.sort()
    mid = len(values) // 2
    if len(values) % 2 == 0:
        return round((values[mid] + values[mid - 1]) / 2, 4)
    return round(values[mid], 4)


def get_max_by_attribute(data, attribute):
    assert any(attribute in laureate for laureate in data), f"Unknown attribute {attribute}"

    values = [laureate[attribute] for laureate in data if laureate[attribute] is not None]
    return round(max(values), 4)


def get_min_by_attribute(data, attribute):
    assert any(attribute in laureate for laureate in data), f"Unknown attribute {attribute}"

    values = [laureate[attribute] for laureate in data if laureate[attribute] is not None]
    return round(min(values), 4)


def get_top_k_values_by_attribute(data, attribute, k):
    assert any(attribute in laureate for laureate in data), f"Unknown attribute {attribute}"
    assert k > 0, "k must be greater than 0"

    values = [laureate[attribute] for laureate in data if laureate[attribute] is not None]
    values.sort(reverse=True)
    return values[:k]
