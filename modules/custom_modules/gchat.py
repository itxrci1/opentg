def generate_gemini_response(...):
    try:
        # existing code...
    except Exception as e:
        if "429" in str(e) or "invalid" in str(e).lower() or "403" in str(e) or "suspended" in str(e).lower():
            # handle key switching logic
        else:
            raise e


def gchat(...):
    def process_combined_messages(...):
        try:
            # existing code...
        except Exception as e:
            if "429" in str(e) or "invalid" in str(e).lower() or "403" in str(e) or "suspended" in str(e).lower():
                # handle key switching logic
            else:
                raise e
        # remaining code...