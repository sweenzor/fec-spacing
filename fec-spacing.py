#!/usr/bin/env python

from itertools import izip

class wall_segments(object):
	def __init__(self):
		self.points = []
	
	def load_segments(self, corners):
		segments = []
		segments.append((corners[-1], corners[0]))
		for segx, segy in izip(corners[::2], corners[1::2]):
			segments.append((segx, segy))
		for segment in segments:
			self.points.append(self.build_segment(segment))

	def build_segment(self, segment):
		print segment[0]
		print segment[1]
		if segment[0][1] == segment[1][1]:
			length = abs(segment[0][0] - segment[1][0])
			print length
		else:
			length = abs(segment[0][1] - segment[1][1])
			print length			
		print '\n'

if __name__ == "__main__":
	corners = [(0, 0), (100, 0), (100, 80), (40, 80), (40, 120), (0, 120)]
	ws = wall_segments()
	ws.load_segments(corners)
