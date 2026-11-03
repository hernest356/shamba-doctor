from openai import OpenAI

print("Starting AI test...")

client = OpenAI()

print("Sending request...")

response = client.responses.create(
    model="gpt-5.6-luna",
    input="You are Shamba Doctor. Give a short farming tip for a farmer growing maize."
)

print("AI response:")
print(response.output_text)