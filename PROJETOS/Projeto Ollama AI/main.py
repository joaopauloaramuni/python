import time
import ollama

start_time = time.time()

import ollama

stream = ollama.chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

end_time = time.time()

print(f"Time taken: {end_time - start_time:.2f} seconds")

# pip install ollama
# brew install ollama
# brew services start ollama
# ollama start
# ollama pull llama3.1

# https://ollama.com/
# https://github.com/ollama/ollama-python
