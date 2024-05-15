from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class WikipediaRetrievalHI(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="WikipediaRetrievalHI",
        description="The dataset is derived from Cohere's wikipedia-2023-11 dataset and contains synthetically generated queries.",
        reference="https://huggingface.co/datasets/ellamind/wikipedia-2023-11-retrieval-hi",
        dataset={
            "path": "ellamind/wikipedia-2023-11-retrieval-hi",
            "revision": "b0642ba7aa43bd243240de58af4e16ad9f7f5aad",
        },
        type="Retrieval",
        category="s2p",
        eval_splits=["test"],
        eval_langs=["hin-Deva"],
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
