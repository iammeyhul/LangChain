from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator='',
    chunk_size=5,
    chunk_overlap=0,
)

result = splitter.split_text("hello my name is john doe and i am a software engineer. i work at a tech company in silicon valley. i love coding and building new things. my hobbies include hiking, reading, and playing video games. i also enjoy spending time with my family and friends.")

print(result)
