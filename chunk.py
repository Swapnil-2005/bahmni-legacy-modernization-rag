from langchain_core.documents import Document

def chunk_by_file(java_files):
    docs = []
    for jf in java_files:
        docs.append(
            Document(
                page_content=jf["content"],
                metadata={"source": jf["path"]}
            )
        )
    return docs
