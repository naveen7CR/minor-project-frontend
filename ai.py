def analyze_question(q):
    q = q.lower()

    if "python" in q:
        return "python"
    elif "math" in q:
        return "math"
    elif "ai" in q:
        return "ai"
    return "general"


def best_mentor(subject, mentors):
    best = None
    top = -1

    for m in mentors:
        if m.subject == subject and m.stars > top:
            best = m
            top = m.stars

    return best