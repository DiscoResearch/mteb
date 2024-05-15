from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class WikipediaRetrievalCS(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="WikipediaRetrievalCS",
        description="The dataset is derived from Cohere's wikipedia-2023-11 dataset and contains synthetically generated queries.",
        reference="https://huggingface.co/datasets/ellamind/wikipedia-2023-11-retrieval-cs",
        dataset={
            "path": "ellamind/wikipedia-2023-11-retrieval-cs",
            "revision": "89fa96cb55c3578cfc63b25b8696443f857b1cab",
        },
        type="Retrieval",
        category="s2p",
        eval_splits=["test"],
        eval_langs=["ces-Latn"],
        main_score="ndcg_at_10",
        date=("2023-11-01", "2024-05-15"),
        form=["written"],
        domains=["Encyclopaedic"],
        task_subtypes=["Question answering", "Article retrieval"],
        license="cc-by-sa-3.0",
        socioeconomic_status="mixed",
        annotations_creators="derived",
        dialect=[],
        text_creation="LM-generated and verified",
        bibtex_citation="",
        n_samples={"test": 1500},
        avg_character_length={"test": 452},
    )
