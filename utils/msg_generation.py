import base64
def generate_messages_list(roles_info):
    messages = []

    for info in roles_info:
        role = info['role']
        message_contents = []

        # Add text content if provided
        if 'text' in info:
            message_contents.append({"type": "text", "text": info['text']})

        # Add image contents if provided. It supports multiple images now.
        image_inputs = info.get('image_inputs', [])
        for image_input in image_inputs:
            if isinstance(image_input, str) and image_input.startswith(('http://', 'https://')):
                # Image input is a URL, use it directly
                message_contents.append({"type": "image_url", "image_url": {"url": image_input}})
            elif isinstance(image_input, str):
                # Image input is a file path, encode to base64
                try:
                    with open(image_input, "rb") as image_file:
                        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
                        message_contents.append({
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                        })
                except FileNotFoundError:
                    # If file not found, add an error message
                    message_contents.append({
                        "type": "error",
                        "text": f"Image file not found: {image_input}"
                    })

        messages.append({"role": role, "content": message_contents})

    return messages

# # Example usage with multiple images for a single role
# roles_info = [
#     {'role': 'user', 'text': "User's text message", 'image_inputs': ["/Users/zhilinwang/PycharmProjects/Anton_TalnF/data/CV/text.jpg", "https://example.com/user_image2.jpg"]},
#     {'role': 'admin', 'image_inputs': ["/path/to/admin_image.png", "/path/to/another_admin_image.png"]},
#     {'role': 'moderator', 'text': "Moderator's announcement", 'image_inputs': ["/path/to/moderator_image.png"]}
# ]
#
# # Generate the list of message dictionaries from the user input
# messages_list_from_input = generate_messages_list(roles_info)
# print(messages_list_from_input)
#
