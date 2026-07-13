import datetime
import pywhatkit
import requests

def fetch_wikipedia_summary(keyword):
    """
    Direct REST API client for Wikipedia. 
    Handles network queries securely without crashing on raw responses.
    """
    # Professional user-agent taaki Wikipedia ka server request block na kare
    headers = {
        'User-Agent': 'ModularAIApp/1.0 (ayushnaman@example.com) Python-Requests/2.0'
    }
    
    # Official Wikipedia API Endpoint
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "exsentences": 2,  # Sirf 2 lines extract karega
        "titles": keyword,
        "redirects": 1     # Sahi context par automatic redirect karega
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            page_data = data.get("query", {}).get("pages", {})
            
            # Extract parsing from dynamic page key
            if page_data:
                page_id = list(page_data.keys())[0]
                if page_id != "-1":
                    summary = page_data[page_id].get("extract", "")
                    if summary:
                        return {"status": "success", "data": summary}
            
            return {"status": "error", "message": "Search Exception: Target context could not be matched dynamically."}
        else:
            return {"status": "error", "message": f"Server Refusal: HTTP {response.status_code}"}
            
    except Exception as e:
        return {"status": "error", "message": f"Network Exception: {str(e)}"}


def handle_automation(user_command):
    # Input formatting and clean-up
    normalized_query = user_command.lower().strip()
    
    if 'wikipedia' in normalized_query or 'search for' in normalized_query:
        keyword = normalized_query.replace("wikipedia", "").replace("search for", "").strip()
        
        # Smart context routing for engineering domains
        if keyword == 'python':
            keyword = 'python (programming language)'
        elif keyword == 'java':
            keyword = 'java (programming language)'
            
        # Capitalize first letter as required by standard web APIs
        keyword = keyword.title()
        
        # Executing API pipeline
        result = fetch_wikipedia_summary(keyword)
        if result["status"] == "success":
            return {"status": "success", "type": "wiki", "data": result["data"]}
        else:
            return {"status": "error", "message": result["message"]}
            
    elif 'play' in normalized_query:
        media_target = normalized_query.replace("play", "").strip()
        if not media_target:
            return {"status": "error", "message": "Validation Error: Intent target identifier missing."}
        
        pywhatkit.playonyt(media_target)
        return {"status": "success", "type": "play", "data": media_target}
        
    elif 'time' in normalized_query or 'clock' in normalized_query:
        timestamp = datetime.datetime.now().strftime('%I:%M %p')
        return {"status": "success", "type": "time", "data": timestamp}
        
    else:
        return {"status": "warning", "message": "Routing Failure: Input parameter does not match valid hooks ('wikipedia', 'play', 'time')."}