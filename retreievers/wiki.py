from langchain_community.retrievers import WikipediaRetriever


ret = WikipediaRetriever(lang='en', top_k_results=2)

query = "what is the capital of France?"

result = ret.invoke(query)
print(result[0].page_content)