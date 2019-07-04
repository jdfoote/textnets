# -*- coding: utf-8 -*-

"""Console script for textnets."""

import os
import click
from textnets import TextCorpus, Textnets


@click.command()
@click.argument('corpus', nargs=-1, type=click.Path(exists=True),
                required=True)
@click.option('--lex', '-l', help='How to lex the corpus.',
              type=click.Choice(['noun_phrases', 'tokenized']),
              required=True)
@click.option('--node-type', '-n', help='Project network of this node type.',
              type=click.Choice(['doc', 'term']),
              required=False)
@click.option('--format', '-f', help='Output format (defaults to graphml).',
              type=click.Choice(['graphml', 'gml', 'pajek', 'graphviz']),
              default='graphml')
@click.option('-o', '--output', default='-',
              help='Output file (defaults to stdout).',
              type=click.File('w'))
def main(corpus, lex, node_type, format, output):
    """textnets - Automated text analysis using network techniques.

    This command takes a corpus of texts as its argument and outputs
    a network graph of either document or term nodes.

    CORPUS: Path containing corpus files.
    """
    if len(corpus) == 1 and os.path.isdir(corpus[0]):
        c = TextCorpus(os.path.join(corpus[0], '*'))
    else:
        c = TextCorpus(corpus)
    tt = getattr(c, lex)()
    tn = Textnets(tt)
    if node_type:
        g = tn.project(node_type=node_type)
    else:
        g = tn.graph
        g['cluster'] = tn.cluster().membership
    with output as f:
        g.write(f, format=format)


if __name__ == "__main__":
    main()
