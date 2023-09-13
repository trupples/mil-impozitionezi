#!/usr/bin/env python

import sys
from pdfrw import PdfReader, PdfWriter, PageMerge 

def merge(pages):
	""" Lay out a list of pages horizontally, into a single signature """
	# TODO: handle bleed margins properly
	signature = PageMerge()

	x = 0
	for page in pages:
		signature.add(page)
		signature[-1].x = x
		x += signature[-1].w

	return signature.render()


if __name__ == '__main__':
	if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) != 3:
		print(f"usage: {sys.argv[0]} [-h|--help] source.pdf destination.pdf")
		sys.exit(1)

	pages = PdfReader(sys.argv[1]).pages

	if len(pages) % 4 != 0:
		pad = (-len(pages))%4
		pages += [None] * pad
		print(f"W: Number of pages not a multiple of 4 ({len(pages) % 4 =}). Adding {pad} blank pages.")

	signatures = []
	for i in range(0, len(pages) // 2, 2):
		signatures += [
			merge([ pages[-i - 1], pages[i]      ]),
			merge([ pages[i + 1],  pages[-i - 2] ])
		]

	PdfWriter(sys.argv[2]).addpages(signatures).write()
