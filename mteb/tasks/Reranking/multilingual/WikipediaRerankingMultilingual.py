from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskReranking import AbsTaskReranking

_EVAL_LANGS = {
    "bg": ["bul-Cyrl"],
    "bn": ["ben-Beng"],
    "cs": ["ces-Latn"],
    "da": ["dan-Latn"],
    "de": ["deu-Latn"],
    "en": ["eng-Latn"],
    "fa": ["fas-Arab"],
    "fi": ["fin-Latn"],
    "hi": ["hin-Deva"],
    "it": ["ita-Latn"],
    "nl": ["nld-Latn"],
    "pt": ["por-Latn"],
    "ro": ["ron-Latn"],
    "sr": ["srp-Cyrl"],
}
_CONFIG_LIST = list(_EVAL_LANGS.keys())

class WikipediaRerankingMultilingual(AbsTaskReranking):
    metadata = TaskMetadata(
        name="WikipediaRerankingMultilingual",
        description="The dataset is derived from Cohere's wikipedia-2023-11 dataset and contains synthetically generated queries.",
        reference="https://huggingface.co/datasets/ellamind/wikipedia-2023-11-reranking-multilingual",
        hf_hub_name="ellamind/wikipedia-2023-11-reranking-multilingual",
        dataset={
            "path": "ellamind/wikipedia-2023-11-reranking-multilingual",
            "revision": "b20adcd11a02dc0226edbe8b5951e99ee0bb091c",
            # "config": _CONFIG_LIST,
        },
        type="Reranking",
        category="s2p",
        eval_splits=["test"],
        eval_langs=_EVAL_LANGS,
        main_score="map",
        date=("2023-11-01", "2024-05-15"),
        form=["written"],
        domains=["Encyclopaedic"],
        task_subtypes=[],
        license="cc-by-sa-3.0",
        socioeconomic_status="mixed",
        annotations_creators="derived",
        dialect=[],
        text_creation="LM-generated and verified",
        bibtex_citation="",
        n_samples={
            "en": 1500,
            "de": 1500,
            "it": 1500,
            "pt": 1500,
            "nl": 1500,
            "cs": 1500,
            "ro": 1500,
            "bg": 1500,
            "sr": 1500,
            "fi": 1500,
            "da": 1500,
            "fa": 1500,
            "hi": 1500,
            "bn": 1500,
        },
        avg_character_length={"test": 452},
    )

    def load_data(self, config: str, **kwargs):
        """Load dataset from HuggingFace hub"""
        if self.data_loaded:
            return
        self.dataset = datasets.load_dataset(config=config, **self.metadata_dict["dataset"])  # type: ignore
        self.dataset_transform()
        self.data_loaded = True