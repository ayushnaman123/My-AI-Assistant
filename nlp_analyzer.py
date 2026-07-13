def analyze_text_sentiment(raw_text_input):
    positive_tokens = {'good', 'great', 'awesome', 'best', 'happy', 'love', 'nice', 'badhiya', 'acha', 'mast', 'excellent'}
    negative_tokens = {'bad', 'worst', 'hate', 'angry', 'sad', 'poor', 'slow', 'waste', 'kharab', 'bekar', 'fail'}
    
    parsed_tokens = raw_text_input.lower().split()
    pos_matches = sum(1 for token in parsed_tokens if token in positive_tokens)
    neg_matches = sum(1 for token in parsed_tokens if token in negative_tokens)
    
    if pos_matches > neg_matches:
        return {"result": "positive", "score": pos_matches}
    elif neg_matches > pos_matches:
        return {"result": "negative", "score": neg_matches}
    else:
        return {"result": "neutral", "score": 0}