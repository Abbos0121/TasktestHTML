import unittest

from msg_split import split_message


class TestSplitMessage(unittest.TestCase):
    def assertFragmentInHTML(self, fragment, html):
        self.assertIn(fragment, html, f"\nFragment: {fragment}\nNot found in HTML:\n{html}")

    def test_split_message_with_max_len(self):
        html_text = """<!DOCTYPE html>
<html>
<body>
<p>This is a <b>sample</b> HTML <i>text</i> for testing.</p>
<p>It contains multiple <span>tags</span> that should be split correctly.</p>
</body>
</html>
"""

        max_len = 50
        fragments = list(split_message(html_text, max_len=max_len))
        expected_result = [
            '<!DOCTYPE html>\n<html>\n<body>\n<p>This is a <b>sample</b></p>\n</body>\n</html>',
            '<html>\n<body>\n<p>It contains multiple <span>tags</span></p>\n</body>\n</html>']

        for fragment, expected_fragment in zip(fragments, expected_result):
            with self.subTest(fragment=fragment):
                self.assertFragmentInHTML(fragment, html_text)
