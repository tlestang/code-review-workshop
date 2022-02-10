""""""

from itertools import starmap
from operator import le, lt, and_
from pathlib import Path
from os import path
from sys import argv, stdout
from argparse import ArgumentParser

from data import load_graph


def neighbourhood(coord: tuple[int, int], borders) -> None:
    n, s, w, e, nw, ne, sw, se = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]
    return filter(
        lambda l: and_(*starmap(le, zip((0, 0), l)))
        and and_(*starmap(lt, zip(l, borders))),
        map(lambda n: tuple(map(sum, zip(coord, n))), (n, s, w, e, nw, ne, sw, se)),
    )


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Determine the list of arcs in the input Graph whose weight is greater or equal to their neighbour coordinates."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="Path of the input file containing the list of coordinates to check",
        dest="data_filepath",
    )
    parser.add_argument(
        "-o", "--output", type=Path, dest="logfile_output_path", default=None
    )

    cli_args = parser.parse_args()
    adj_matrix = load_graph(cli_args.data_filepath, sparse=False, fillna_with=0)
    N = len(adj_matrix)

    nn = list()
    for u, _ in enumerate(adj_matrix):
        for v, w in enumerate(adj_matrix[u]):
            for (i, j) in neighbourhood((u, v), borders=(N, N)):
                if w >= adj_matrix[i][j]:
                    nn.append((u, v))
    print(f"Found {len(nn)} edges in the input Graph satisfying the condition.")

    if (
        cli_args.logfile_output_path is not None
        and cli_args.logfile_output_path.exists()
    ):
        logfile = open(cli_args.logfile_output_path, "w")
    else:
        logfile = stdout

    for edge in nn:
        print(f"{edge}", file=logfile)
