from langchain.schema import Document

# Create 5 Document objects with different content
documents = [
    Document(page_content="This is the first document.", metadata={"id": 1}),
    Document(page_content="Second document for testing.", metadata={"id": 2}),
    Document(page_content="Here is the third document.", metadata={"id": 3}),
    Document(page_content="Fourth document in the list.", metadata={"id": 4}),
    Document(page_content="Finally, the fifth document.", metadata={"id": 5}),
]

# Print the documents to verify
for doc in documents:
    print(doc)
