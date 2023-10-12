from .base import BaseViewer
import sublime
import re

class Sublime3Viewer(BaseViewer):
	def load(self):
		version_match = re.match(r"\d+", sublime.version())

		if not version_match:
			raise Exception("Not Sublime 3! (%s)" % sublime.version())

		numeric_version = int(version_match.group(0))

		if numeric_version < 3000:
			raise Exception("Not Sublime 3! (%s)" % sublime.version())

	def view(self,diagram_files):
		for diagram_file in diagram_files:
			if diagram_file:
				sublime.active_window().open_file(diagram_file.name)


class NoneViewer(BaseViewer):
	def load(self):
		pass

	def view(self, filenames):
		pass
