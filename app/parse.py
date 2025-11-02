from dataclasses import dataclass


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str]


def main(output_csv_path: str) -> None:
    


if __name__ == "__main__":
    main("quotes.csv")
