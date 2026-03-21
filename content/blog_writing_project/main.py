from blog_writing_project.crew import BlogWritingWithCrewAI

def run(topic_name): # We now pass the topic here
    inputs = {
        "topic": topic_name
    }
    try:
        # Re-initialize the crew with the fresh inputs
        result = BlogWritingWithCrewAI().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
