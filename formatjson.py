import json

def filter_t2i_params(t2i_params_json):
    """
    Filters and transforms the T2I parameters JSON, keeping only "name", "id", and "description" 
    for most entries, but retaining the entire structure for entries containing specific keywords.

    Args:
        t2i_params_json (dict): The JSON response from SwarmUI's /API/ListT2IParams endpoint.

    Returns:
        dict: The filtered and transformed JSON data.
    """
    keywords = ["prompt", "negative_prompt", "batch size", "steps", "cfg_scale", "width", "height", "sampler_name", "scheduler"]
    filtered_params = []

    for param in t2i_params_json.get("list", []):
        param_name = param.get("name", "").lower()
        param_id = param.get("id", "").lower()
        param_description = param.get("description", "").lower()

        # Check if any of the keywords are present in name, id, or description
        if any(keyword in param_name or keyword in param_id or keyword in param_description for keyword in keywords):
            filtered_params.append(param)  # Keep the entire entry
        else:
            filtered_params.append({
                "name": param.get("name"),
                "id": param.get("id"),
                "description": param.get("description")
            })

    return {"list": filtered_params}

# Example Usage (assuming you have the t2i_params.json file from before):
input_file = "t2i_params.json"
output_file = "filtered_t2i_params.json"

with open(input_file, "r") as f:
    t2i_params = json.load(f)

filtered_t2i_params = filter_t2i_params(t2i_params)

with open(output_file, "w") as f:
    json.dump(filtered_t2i_params, f, indent=4)

print(f"Filtered T2I parameters written to {output_file}")