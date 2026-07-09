"""
Analytics service.

Stores usage metrics for NovaCore Knowledge AI.
"""

import json
from collections import Counter
from datetime import datetime
from pathlib import Path

import pandas as pd


class AnalyticsService:
    """
    Handles application analytics.
    """

    def __init__(self):

        self.logs_path = Path("data/logs")

        self.logs_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.analytics_file = (
            self.logs_path / "queries.json"
        )

        if not self.analytics_file.exists():

            self.analytics_file.write_text(
                "[]",
                encoding="utf-8",
            )

    # -------------------------------------------------
    # PRIVATE
    # -------------------------------------------------

    def _load(self):

        try:

            with open(
                self.analytics_file,
                "r",
                encoding="utf-8",
            ) as file:

                return json.load(file)

        except Exception:

            return []

    def _save(self, data):

        with open(
            self.analytics_file,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    # -------------------------------------------------
    # PUBLIC
    # -------------------------------------------------

    def register_query(
        self,
        question: str,
        response_time: float,
        sources: list,
    ):

        data = self._load()

        documents = []

        for source in sources:

            if isinstance(source, dict):

                documents.append(
                    source["document"]
                )

            else:

                documents.append(
                    str(source)
                )

        data.append(
            {
                "timestamp": datetime.now().isoformat(),
                "question": question,
                "response_time": round(
                    response_time,
                    2,
                ),
                "documents": documents,
            }
        )

        self._save(data)

    # -------------------------------------------------

    def dataframe(self):

        data = self._load()

        if not data:

            return pd.DataFrame()

        df = pd.DataFrame(data)

        df["timestamp"] = pd.to_datetime(
            df["timestamp"]
        )

        df["date"] = (
            df["timestamp"]
            .dt.date
        )

        return df

    # -------------------------------------------------

    def total_queries(self):

        return len(
            self._load()
        )

    # -------------------------------------------------

    def average_response_time(self):

        df = self.dataframe()

        if df.empty:

            return 0

        return round(
            df["response_time"].mean(),
            2,
        )

    # -------------------------------------------------

    def latest_queries(
        self,
        limit: int = 5,
    ):

        df = self.dataframe()

        if df.empty:

            return []

        return (
            df.sort_values(
                "timestamp",
                ascending=False,
            )
            .head(limit)
            .to_dict("records")
        )

    # -------------------------------------------------

    def most_consulted_documents(
        self,
        limit: int = 5,
    ):

        counter = Counter()

        for query in self._load():

            counter.update(
                query["documents"]
            )

        return counter.most_common(
            limit
        )

    # -------------------------------------------------

    def queries_per_day(self):

        df = self.dataframe()

        if df.empty:

            return pd.DataFrame(
                columns=[
                    "date",
                    "queries",
                ]
            )

        result = (
            df.groupby("date")
            .size()
            .reset_index(
                name="queries"
            )
        )

        return result

    # -------------------------------------------------

    def response_time_history(self):

        df = self.dataframe()

        if df.empty:

            return pd.DataFrame(
                columns=[
                    "date",
                    "response_time",
                ]
            )

        result = (
            df.groupby("date")[
                "response_time"
            ]
            .mean()
            .reset_index()
        )

        return result