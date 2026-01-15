def get_relevant_chunks(vectorstore, query, k=3):
    """
    Retrieve top-k relevant chunks from the vector store.
    Returns a list of plain text strings.
    """

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )

    docs = retriever.invoke(query)

    return [doc.page_content for doc in docs]
