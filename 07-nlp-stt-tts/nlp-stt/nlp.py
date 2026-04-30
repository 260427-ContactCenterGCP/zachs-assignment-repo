# Imports the Google Cloud client library.
from google.cloud import language_v1
from pyasn1_modules.rfc7633 import Features

# Instantiates a client.
client = language_v1.LanguageServiceClient()

# CHANGE ME
text = """While Kingdom Come: Deliverance 2 still stumbles in some aspects of its portrayal of 15th-century Bohemia, the shadow that lingered over the first game has mostly dissipated. This is a massively improved sequel in every other area, with better combat, quest design, and none of the technical issues that plagued the original. Not everyone will vibe with its slow-paced and oftentimes tedious approach, but those willing to meet it on its own terms will find a compelling open-world RPG that relishes in player agency and the consequences of your actions."""

document = language_v1.types.Document(
    content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text.
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

response = client.analyze_entities(
    request={"document": document}
)

classify = client.classify_text(
    request={"document": document}
)


# Add in details for checking the entities, classification, and moderation results

print(f"Text: {text}")
print(f"Sentiment: {sentiment.score}, Magnitude: {sentiment.magnitude}")

for entity in response.entities:
    print(f"{entity.name} is a {language_v1.Entity.Type(entity.type_).name}")

for category in classify.categories:
    print(f"Categorized as {category.name} with confidence level of {category.confidence}")