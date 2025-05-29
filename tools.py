import arxiv

client = arxiv.Client()

def fetch_arxiv_papers(title: str, papers_count: int):
    search_query = f"all:{title}"
    search = arxiv.Search(
        query=search_query,
        max_results=papers_count,
        sort_by= arxiv.SortCriterion.SubmittedDate
    )
    papers = []
    results = client.results(search)
    for result in results:
        paper_info = {
            "title": result.title,
            "summary": result.summary,
            "published": result.published,
            "journal_ref": result.journal_ref,
            "doi": result.doi,
            "primary_category": result.primary_category,
            "categories": result.categories,
            "pdf_url": result.pdf_url,
            "arxiv_url": result.entry_id,
            "authors": [author.name for author in result.authors]
        }
        papers.append(paper_info)
    return papers