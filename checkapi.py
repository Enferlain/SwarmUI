import requests
import json

# Example usage (replace with your actual Swarm URL and session ID):
swarm_url = "http://localhost:7801"  # Default SwarmUI URL
session_id = "YOUR_SESSION_ID"  # You'll need to get this from /API/GetNewSession

def get_new_session(swarm_url):
    """
    Gets a new session ID from the SwarmUI API.

    Args:
        swarm_url (str): The base URL of your SwarmUI instance.

    Returns:
        str: The new session ID, or None if an error occurred.
    """
    endpoint = f"{swarm_url}/API/GetNewSession"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(endpoint, headers=headers, json={})
        response.raise_for_status()

        session_data = response.json()
        return session_data.get("session_id")
    except requests.exceptions.RequestException as e:
        print(f"Error getting new session: {e}")
        return None

# Example usage:
session_id = get_new_session(swarm_url)
print(f"New session ID: {session_id}")


def get_t2i_params(swarm_url, session_id):
    """
    Fetches the available text-to-image parameters from the SwarmUI API.

    Args:
        swarm_url (str): The base URL of your SwarmUI instance.
        session_id (str): Your SwarmUI session ID.

    Returns:
        dict: A dictionary containing the available T2I parameters, or None if an error occurred.
    """
    endpoint = f"{swarm_url}/API/ListT2IParams"
    headers = {"Content-Type": "application/json"}
    data = {
        "session_id": session_id
    }

    try:
        response = requests.post(endpoint, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching T2I parameters: {e}")
        return None

t2i_params = get_t2i_params(swarm_url, session_id)

if t2i_params:
    output_file = "t2i_params.json"
    with open(output_file, "w") as f:
        json.dump(t2i_params, f, indent=4)
    print(f"T2I parameters written to {output_file}")