"""Regression coverage for the Bekasi vocabulary and contextual operators.

Run with: python -m unittest discover -s tests -p 'test_bekasi_syntax.py'
"""
import contextlib
import io
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

from pykasi import Interpreter, Parser, RuntimeErrorWithMessage, run_text


ROOT = Path(__file__).resolve().parents[1]


class HomepageExamples(HTMLParser):
    """Read the actual code/output pairs visitors see on the homepage."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.examples = []
        self.current = None
        self.capture = None
        self.parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'data-example' in attrs:
            self.current = {'name': attrs['data-example']}
            self.examples.append(self.current)
        if 'data-source' in attrs or 'data-output' in attrs:
            self.capture = 'source' if 'data-source' in attrs else 'output'
            self.parts = []

    def handle_endtag(self, tag):
        if self.capture and tag == ('code' if self.capture == 'source' else 'pre'):
            self.current[self.capture] = ''.join(self.parts).strip()
            self.capture = None

    def handle_data(self, data):
        if self.capture:
            self.parts.append(data)


class BekasiSyntaxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with contextlib.redirect_stderr(io.StringIO()):
            cls.parser = Parser()

    def output(self, source):
        result = io.StringIO()
        with contextlib.redirect_stdout(result):
            Interpreter().run(self.parser.parse(source))
        return result.getvalue()

    def test_arithmetic_precedence_and_associativity(self):
        self.assertEqual(self.output('''
            bacot 2 tambah 3 kali 4;
            bacot (2 tambah 3) kali 4;
            bacot 20 kurang 4 kurang 3;
            bacot 20 bagi 2 kali 3;
            bacot 17 sisa 5;
            bacot 2 pangkat 3 pangkat 2;
            bacot 2 + 3 kali 4 ** 2;
        '''), '14\n20\n13\n30.0\n2\n512\n50\n')

    def test_words_keep_string_and_list_semantics(self):
        self.assertEqual(self.output('''
            bacot "Woy, " tambah "Bekasi!";
            bacot [1, 2] tambah [3];
            bacot "gas " kali 2;
            bacot [1] kali 3;
        '''), "Woy, Bekasi!\n[1, 2, 3]\ngas gas \n[1, 1, 1]\n")

    def test_boolean_spelling_and_kaga(self):
        for spelling in ('danta', 'Danta', 'DANTA'):
            with self.subTest(spelling=spelling):
                self.assertEqual(self.output(
                    'kalo ' + spelling + ' { bacot "iya"; } kaga { bacot "kaga"; }'
                ), 'iya\n')
        for spelling in ('kagadanta', 'Kagadanta', 'KAGADANTA'):
            with self.subTest(spelling=spelling):
                self.assertEqual(self.output(
                    'kalo ' + spelling + ' { bacot "iya"; } kaga { bacot "kaga"; }'
                ), 'kaga\n')

    def test_typed_boolean_assignment(self):
        self.assertEqual(self.output(
            'danta siap gas danta; siap gas kagadanta; bacot siap;'
        ), 'False\n')
        with self.assertRaises(TypeError):
            self.output('danta siap gas danta; siap gas 42;')

    def test_operator_words_still_work_as_identifiers(self):
        self.assertEqual(self.output('''
            fungsi tambah(a, b) { balikin a tambah b; }
            fungsi kali(tambah, kurang) { balikin tambah kali kurang; }
            duit sisa gas 17 sisa 5;
            duit bagi gas 8;
            bacot tambah(2, 3);
            bacot kali(4, 6);
            bacot sisa;
            bacot bagi bagi 2;
            impor math sebagai pangkat;
            bacot pangkat.sqrt(9);
        '''), '5\n24\n2\n4.0\n3.0\n')

    def test_word_boundaries_comments_and_strings(self):
        self.assertEqual(self.output('''
            # tambah kagadanta bacot should not be interpreted here
            tambahan gas 7;
            kagadanta_bre gas 8;
            bacot tambahan tambah kagadanta_bre;
            bacot "danta kagadanta tambah bacot kaga";
        '''), '15\ndanta kagadanta tambah bacot kaga\n')

    def test_legacy_and_new_aliases_can_mix(self):
        self.assertEqual(self.output('''
            valid lama gas hoax;
            kalo lama { spill "iya"; } kalo_kaga { bacot "belum"; }
            lama gas danta;
            kalo lama { spill 3 + 2; } kaga { bacot 0; }
            spill valid;
            bacot kagadanta;
        '''), 'belum\n5\nTrue\nFalse\n')

    def test_loops_functions_and_comparisons(self):
        self.assertEqual(self.output('''
            fungsi hitung_total(n) {
                hasil gas 0;
                putaran gas 1;
                puterin putaran <= n {
                    hasil gas hasil tambah putaran;
                    putaran gas putaran tambah 1;
                }
                balikin hasil;
            }
            kalo hitung_total(3) == 6 {
                bacot "Danta, bre.";
            } kaga { bacot "Kagadanta."; }
        '''), 'Danta, bre.\n')

    def test_invalid_operands_and_zero_division(self):
        for source, error in (
            ('bacot "duit" tambah 1;', TypeError),
            ('bacot 1 bagi 0;', ZeroDivisionError),
            ('bacot 1 sisa 0;', ZeroDivisionError),
            ('bacot 1 tambah ;', SyntaxError),
        ):
            with self.subTest(source=source), self.assertRaises(error):
                self.output(source)

    def test_public_api_wraps_errors(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(RuntimeErrorWithMessage):
                run_text('bacot 1 bagi 0;')

    def test_homepage_output_matches_interpreter(self):
        page = HomepageExamples()
        page.feed((ROOT / 'docs/index.html').read_text(encoding='utf-8'))
        self.assertEqual(len(page.examples), 4)
        for example in page.examples:
            with self.subTest(example=example['name']):
                self.assertEqual(self.output(example['source']).strip(), example['output'])

    def test_documented_syntax_examples_parse_and_execute(self):
        text = (ROOT / 'SINTAKS.md').read_text(encoding='utf-8')
        examples = re.findall(r'```pykasi\n(.*?)```', text, re.DOTALL)
        self.assertGreaterEqual(len(examples), 4)
        for index, source in enumerate(examples):
            with self.subTest(example=index):
                self.output(source)

    def test_vscode_snippet_defaults_execute_in_their_context(self):
        snippets = json.loads((ROOT / 'vscode-extension/snippets/pykasi-snippets.json').read_text(encoding='utf-8'))
        for name, snippet in snippets.items():
            source = snippet['body']
            if isinstance(source, list):
                source = '\n'.join(source)
            source = re.sub(r'\$\{\d+:([^}]*)\}', lambda match: match.group(1), source)
            source = re.sub(r'\$\d+', '', source)
            if source.startswith('balikin '):
                source = 'fungsi demo() { hasil gas 5; ' + source + ' } bacot demo();'
            if source in ('terus;', 'berhenti;'):
                source = 'i gas 0; puterin i < 1 { i gas i tambah 1; ' + source + ' }'
            with self.subTest(snippet=name):
                self.output(source)


if __name__ == '__main__':
    unittest.main()
