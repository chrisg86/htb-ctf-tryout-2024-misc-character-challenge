import socket
import re
import sys
import os

PROMPT = "Which character (index) of the flag do you want? Enter an index: "
GET_INDEX_REGEX = r"Character at Index \d+: (.)"

def extract_char(reply_text: str) -> str | None:
    match = re.search(GET_INDEX_REGEX, reply_text)
    if match:
        return match.group(1)
    return None

def collect_until_stop(host: str, port: str, stop_char='}'):
    collected_chars = []
    prompt_bytes = PROMPT.encode()
    index = 0
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, int(port)))

        # Step 1: Read initial prompt and discard
        buffer = b""
        while not buffer.endswith(prompt_bytes):
            chunk = s.recv(1)
            if not chunk:
                raise ConnectionError("Connection closed before initial prompt.")
            buffer += chunk

        while True:
            # Make sure to include newline here, otherwise input is not accepted as submitted
            s.sendall(f"{index}\n".encode())

            buffer = b""
            while not buffer.endswith(prompt_bytes):
                chunk = s.recv(1)
                if not chunk:
                    raise ConnectionError("Connection closed unexpectedly.")
                buffer += chunk

            message = buffer[:-len(prompt_bytes)].decode()

            char = extract_char(message)
            
            if char:
                collected_chars.append(char)
                # Pretty print in the console as data comes in
                sys.stdout.write(f"\r{"".join(collected_chars)}")
                sys.stdout.flush()
                if char == stop_char:
                    break

            index += 1
    
    return collected_chars

def main():
    host = os.environ.get('HOST')
    port = os.environ.get('PORT')

    if not host or not port:
        print("HOST and PORT are required")
        sys.exit(1)

    collect_until_stop(host, port, "}")

if __name__ == "__main__":
    main()
