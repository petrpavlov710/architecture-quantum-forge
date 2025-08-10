from app.engine import get_engine


def make_query(query):
    db = get_engine()
    results = db.similarity_search(query, k=5)
    return results


def print_query_results(results):
    for number, doc in enumerate(results, 1):
        print(f"Результат {number}:")
        print(
            f"Источник: {doc.metadata['source']}, "
            f"чанк: {doc.metadata.get('chunk', 'N/A')}."
        )
        print("Текст результата:")
        print(doc.page_content)
        print("-" * 50)
    print(f"Общее количество результатов: {len(results)}")


if __name__ == "__main__":
    query = "черт неудачник"
    results = make_query(query)
    print_query_results(results)
