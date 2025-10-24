from redlite.metric.math._parser import parse, Number, Negation, Tuple, Triple, Interval, Binary
from redlite.metric.math._score import norma, score


def test_number():
    assert parse("2") == Number(value=2)
    assert parse("2.55") == Number(value=2.55)
    assert parse(".33") == Number(value=0.33)
    assert parse("-1") == Negation(op=Number(value=1))


def test_tuple():
    p = parse("(1, 22)")
    assert p == Tuple(values=(Number(value=1), Number(value=22)))


def test_triple():
    p = parse("(1, 22, -3)")
    assert p == Triple(values=(Number(value=1), Number(value=22), Negation(op=Number(value=3))))


def test_triple_2():
    p = parse("1, 22, -3")
    assert p == Triple(values=(Number(value=1), Number(value=22), Negation(op=Number(value=3))))


def test_interval():
    p = parse("[1, 55)")
    assert p == Interval(values=(Number(value=1), Number(value=55)), brackets="[)")


def test_matrix():
    p = parse(
        """
\\begin{pmatrix}
    1 & -3.14 \\\\
    2.2 & 0 & 0 \\\\
\\end{pmatrix}
"""
    )
    assert p is not None
    assert p.type == "matrix"
    assert len(p.rows) == 2
    assert len(p.rows[0]) == 2
    assert len(p.rows[1]) == 3
    assert p.rows[1][0] == Number(value=2.2)


def test_expr():
    p = parse("1 + 2^6 - 18*4")
    assert p == Binary(
        name="+",
        op1=Number(value=1.0),
        op2=Binary(
            name="-",
            op1=Binary(
                name="^",
                op1=Number(value=2.0),
                op2=Number(value=6),
            ),
            op2=Binary(name="*", op1=Number(value=18.0), op2=Number(value=4.0)),
        ),
    )


def test_union():
    p = parse("(0,9) \\cup (9,36)")
    assert p is not None
    assert p.type == "union"


def test_actual_1():
    p = parse("\\left( 3, \\frac{\\pi}{2} \\right) ")
    assert p is not None


def test_actual_2():
    p = parse("(0,9) \\cup (9,36)")
    assert p is not None


def test_actual_3():
    p = parse("\\text{Navin}")
    assert p is not None


def test_actual_4():
    p = parse("(2,12) \\cup (12,102)")
    assert p is not None


def test_actual_5():
    p = parse(norma("10,\\!080"))
    assert p == Number(value=10080.0)


def test_should_parse():
    for x in _SHOULD_PARSE:
        p = parse(norma(x))
        assert p is not None, x


def test_score_1():
    s = score("x=5", "5")
    assert s == 1.0


def test_score_2():
    s = score("4210_5", "4210")
    assert s == 1.0

    s = score("4210_{8}", "4210")
    assert s == 1.0


def test_score_3():
    s = score("\\text{(E)}", "\\text{E}")
    assert s == 1.0


def test_score_4():
    s = score("864 \\mbox{ inches}^2", "864")
    assert s == 1.0

    s = score("5.4 \\text{ cents}", "5.4")
    assert s == 1.0


def test_score_5():
    s = score("3 \\pm 2 \\sqrt{2}", "3 + 2\\sqrt{2}, 3 - 2\\sqrt{2}")
    assert s == 1.0


def test_score_6():
    s = score("\\text{Navin}", "Navin")
    assert s == 1.0
    s = score("\\mbox{Navin}", "Navin")
    assert s == 1.0


def test_score_7():
    s = score("15\\mbox{ cm}^2", "15")
    assert s == 1.0


def test_score_8():
    s = score("\\dfrac{33}{100}", "\\frac{33}{100}")
    assert s == 1.0


def test_score_9():
    s = score("\\frac{9}{100}", "0.09")
    assert s == 1
    s = score("\\frac{11}{2}", "5.5")
    assert s == 1


def test_score_10():
    s = score(
        "\\begin{pmatrix} -1/3 \\\\ 2/3 \\\\ 5/3 \\end{pmatrix}",
        "\\begin{pmatrix} -\\frac{1}{3} \\\\ \\frac{2}{3} \\\\ \\frac{5}{3} \\end{pmatrix}",
    )
    assert s == 1.0


def test_score_11():
    s = score("1/3", "\\frac{1}{3}")
    assert s == 1.0


def test_score_11a():
    s = score("1/2, \\sqrt{3}", "(0.5, \\sqrt{3})")
    assert s == 1.0


def test_score_12():
    s = score("\\sqrt{9}", "3")
    assert s == 1.0


def test_score_13():
    s = score("10080", "10,080")
    assert s == 1.0


def test_score_14():
    s = score("(0,9) \\cup (9,36)", "(0, 9)")
    assert s == 0.0


def test_evaluations():
    for expected, actual, sc in _EVALUATIONS:
        s = score(expected, actual)
        assert s == sc, (expected, actual, sc)


# unique strings collected from (1) ground truth for Math-500 dataset, and (2) ChatGPT answers for the same dataset
_SHOULD_PARSE = [
    " 52 ",
    "(-1, 6)",
    "(-1,6)",
    "(-2, 1)",
    "(-2,1)",
    "(-3, 12, -1)",
    "(-\\infty, 0]",
    "(-\\infty, 2) \\cup (3, \\infty)",
    "(-\\sqrt{3}, \\sqrt{3})",
    "(0, 9)",
    "(0,9) \\cup (9,36)",
    "(1, -16, -4, 43)",
    "(1,-16,-4,43)",
    "(15, -29)",
    "(15,-29)",
    "(2, 12) \\cup (12, 102)",
    "(2, 4)",
    "(2,12) \\cup (12,102)",
    "(2,4)",
    "(2,\\infty)",
    "(3, \\frac{\\pi}{2})",
    "(3,4]",
    "(5, \\infty)",
    "(5,\\infty)",
    "(6,31,-1)",
    "(8, -2)",
    "(8,-2)",
    "(a + 5)(b + 2)",
    "(a+5)(b+2)",
    "-1",
    "-120",
    "-125",
    "-128",
    "-13x + 3",
    "-13x+3",
    "-19",
    "-2",
    "-2 + 7i",
    "-2,1",
    "-256",
    "-3",
    "-4",
    "-41",
    "-5",
    "-50",
    "-9",
    "-\\frac{1}{1005}",
    "-\\frac{23}{9}",
    "-\\frac{24}{25}",
    "-\\frac{35}{9}",
    "-\\frac{3}{16}",
    "-\\frac{3}{8}",
    "-\\frac{7}{4}",
    "-\\frac{\\pi}{6}",
    "-\\sqrt{3}",
    ".0000672",
    ".35625",
    "0",
    "0, 1",
    "0.0000672",
    "0.09",
    "0.15",
    "0.35625",
    "1",
    "1 - 12i",
    "1 \\pm \\sqrt{19}",
    "1 \\text{ and } -5",
    "1+274i",
    "1+2\\sqrt{3}",
    "1+2i",
    "1, -2",
    "1,-2",
    "1.25",
    "10",
    "10,080",
    "10,\\!080",
    "100",
    "10080",
    "100^\\circ",
    "103",
    "1030",
    "106^\\circ",
    "108",
    "10\\%",
    "11",
    "11 \\sqrt{5} + 11",
    "11,\\! 111,\\! 111,\\! 100",
    "110",
    "110^\\circ",
    "1111111110",
    "113",
    "114.031",
    "116",
    "11\\sqrt2",
    "11\\sqrt{2}",
    "12",
    "120",
    "120^\\circ",
    "121",
    "12470",
    "1250",
    "1251",
    "1260",
    "129",
    "12\\pi",
    "13",
    "13535",
    "137 \\frac{1}{2}",
    "137\\frac{1}{2}",
    "14",
    "143",
    "144",
    "1440",
    "145^\\circ",
    "14625",
    "15",
    "15\\mbox{ cm}^2",
    "15x - 80",
    "16",
    "16 \\sqrt{3}",
    "160",
    "1600",
    "162",
    "166.5",
    "17",
    "1736",
    "17\\pi",
    "18",
    "18 + 7\\pi",
    "18+2\\pi",
    "18.90",
    "180",
    "180^\\circ",
    "19",
    "1940",
    "1\\frac{4}{5}",
    "2",
    "2 \\sqrt{5}",
    "20",
    "200",
    "2000",
    "202",
    "203",
    "204_5",
    "21",
    "210",
    "2107",
    "216",
    "22",
    "2220",
    "224",
    "225",
    "23",
    "24",
    "240",
    "25",
    "2516_8",
    "255",
    "256",
    "26000",
    "27",
    "27648",
    "28",
    "284",
    "288 \\pi",
    "28800",
    "288\\pi",
    "28^\\circ",
    "29",
    "2\\sqrt{113}",
    "2\\sqrt{5}",
    "2k",
    "2k + 2",
    "2k+2",
    "3",
    "3 + 2\\sqrt{2}, 3 - 2\\sqrt{2}",
    "3 \\pm 2 \\sqrt{2}",
    "3 \\sqrt{5}",
    "3, 5, 7",
    "3.2",
    "3.21",
    "30",
    "30^\\circ",
    "31",
    "3125",
    "32",
    "32348",
    "326.5",
    "33",
    "331",
    "333",
    "34",
    "349",
    "35",
    "350",
    "36",
    "36^\\circ",
    "3R^2",
    "3\\sqrt{13}",
    "3\\sqrt{3}",
    "3\\sqrt{5}",
    "4",
    "4.5",
    "40",
    "4005",
    "406",
    "40^\\circ",
    "40_9",
    "41",
    "42",
    "4210",
    "4210_{5}",
    "4343",
    "4343_6",
    "44",
    "440",
    "4495",
    "45",
    "46",
    "47",
    "480",
    "49",
    "4\\sqrt{13}",
    "5",
    "5 + \\sqrt{7}",
    "5.4",
    "5.4 \\text{ cents}",
    "5.5",
    "50",
    "501",
    "504",
    "52",
    "52_8",
    "54",
    "540",
    "550",
    "55^\\circ",
    "56",
    "58",
    "58,500",
    "59",
    "5r^5",
    "5x - 7y + 11z + 4 = 0",
    "6",
    "6 + 9i",
    "6 - 5i",
    "6+9i",
    "60",
    "600",
    "63",
    "64",
    "65",
    "66",
    "6\\sqrt{2}",
    "6r^2 - 4r - 24",
    "6r^2-4r-24",
    "7",
    "70",
    "70 \\sqrt{2}",
    "72",
    "720",
    "7200",
    "75^\\circ",
    "76^\\circ",
    "78",
    "7\\pi",
    "8",
    "8 \\pi",
    "80",
    "8000",
    "80^\\circ",
    "81",
    "83",
    "84",
    "85",
    "850",
    "864",
    "864 \\mbox{ inches}^2",
    "898",
    "8n^2 + 4n + 1",
    "9",
    "90",
    "900",
    "90^\\circ",
    "9901",
    "Navin",
    "[-2, 7]",
    "[2, \\infty)",
    "\\$18.90",
    "\\$32,\\!348",
    "\\$36",
    "\\begin{pmatrix} -1 & 0 \\\\ 0 & -1 \\end{pmatrix}",
    "\\begin{pmatrix} -1/3 \\\\ 2/3 \\\\ 5/3 \\end{pmatrix}",
    "\\begin{pmatrix} -18 \\\\ -49 \\\\ 96 \\end{pmatrix}",
    "\\begin{pmatrix} -2 \\\\ -14 \\\\ -7 \\end{pmatrix}",
    "\\begin{pmatrix} -7 \\\\ 16 \\\\ 5 \\end{pmatrix}",
    "\\begin{pmatrix} -\\frac{1}{3} \\\\ \\frac{2}{3} \\\\ \\frac{5}{3} \\end{pmatrix}",
    "\\begin{pmatrix} 1/5 \\\\ -18/5 \\end{pmatrix}",
    "\\begin{pmatrix} 16/49 \\\\ 48/49 \\\\ 24/49 \\end{pmatrix}",
    "\\begin{pmatrix} 4 \\\\ 0 \\end{pmatrix}",
    "\\begin{pmatrix} 9 \\\\ -12 \\\\ 75 \\end{pmatrix}",
    "\\begin{pmatrix} \\frac{16}{49} \\\\ \\frac{48}{49} \\\\ \\frac{24}{49} \\end{pmatrix}",
    "\\cot x",
    "\\dfrac{13}{6}",
    "\\dfrac{17}{50}",
    "\\dfrac{33}{100}",
    "\\frac 34",
    "\\frac 59",
    "\\frac14",
    "\\frac43",
    "\\frac65",
    "\\frac9{19}",
    "\\frac{1+\\sqrt{5}}{2}",
    "\\frac{100}{3}",
    "\\frac{10}{11}",
    "\\frac{11 + 9a}{20}",
    "\\frac{11+9a}{20}",
    "\\frac{11}{2}",
    "\\frac{11}{36}",
    "\\frac{13}{15}",
    "\\frac{13}{18}",
    "\\frac{13}{4}",
    "\\frac{13}{6}",
    "\\frac{14}{3}",
    "\\frac{16}{27}",
    "\\frac{16}{3}",
    "\\frac{16}{5}",
    "\\frac{17}{21}",
    "\\frac{17}{50}",
    "\\frac{1997}{2}",
    "\\frac{1}{16}",
    "\\frac{1}{2}",
    "\\frac{1}{3}",
    "\\frac{1}{3}(a^2 + b^2 + c^2) + 3R^2",
    "\\frac{1}{4}",
    "\\frac{1}{8}",
    "\\frac{20000}{\\pi}",
    "\\frac{243}{625}",
    "\\frac{270}7\\text{ degrees}",
    "\\frac{2}{1005}",
    "\\frac{2}{21}",
    "\\frac{2}{3}",
    "\\frac{33}{100}",
    "\\frac{35}{128}",
    "\\frac{35}{64}",
    "\\frac{3840}{289}",
    "\\frac{3\\sqrt{2}}{2} + \\left(-3 + \\frac{3\\sqrt{2}}{2}\\right)i",
    "\\frac{3\\sqrt{3}}{4}",
    "\\frac{3}{2}",
    "\\frac{3}{4}",
    "\\frac{3}{56}",
    "\\frac{448}{15625}",
    "\\frac{480}{17}",
    "\\frac{4}{3}",
    "\\frac{4}{9}",
    "\\frac{5}{13}",
    "\\frac{5}{9}",
    "\\frac{639}{40}",
    "\\frac{6}{5}",
    "\\frac{7}{2}",
    "\\frac{7}{4}",
    "\\frac{8}{15}",
    "\\frac{8}{21}",
    "\\frac{8}{63}",
    "\\frac{990}{7}",
    "\\frac{9}{100}",
    "\\frac{9}{19}",
    "\\frac{9}{256}",
    "\\frac{\\pi^2 \\lambda}{6} ",
    "\\frac{\\pi^2}{4}",
    "\\frac{\\pi}{2}",
    "\\frac{\\pi}{4(1+k)}",
    "\\frac{\\sqrt{21}}{5}",
    "\\frac{\\sqrt{3}}{3}",
    "\\left( 3, \\frac{\\pi}{2} \\right)",
    "\\left( \\frac{3}{2}, -13 \\right)",
    "\\left( \\frac{3}{5}, \\frac{8}{3} \\right]",
    "\\left(\\frac{3}{2}, -13\\right)",
    "\\left(\\frac{3}{5},\\frac{8}{3}\\right]",
    "\\left[ \\frac{\\pi^2}{8}, \\frac{5 \\pi^2}{4} \\right]",
    "\\mathbf{0}",
    "\\pi",
    "\\sqrt{51}",
    "\\sqrt{53}",
    "\\sqrt{5}",
    "\\sqrt{66}",
    "\\text{(B)}",
    "\\text{(C)}",
    "\\text{(E)}",
    "\\text{B}",
    "\\text{C}",
    "\\text{Evelyn}",
    "\\text{E}",
    "\\text{Navin}",
    "\\text{east}",
    "\\text{ellipse}",
    "\\text{even}",
    "\\text{odd}",
    "\\{-1, 1, 1\\}",
    "\\{1\\pm\\sqrt{5},-2\\}",
    "i",
    "p - q",
    "x \\in [-2,7]",
    "x=5",
    "x^3 + 3x - 6",
    "x^3+3x-6",
    "x^5 - x^4 + x^3 - x^2 + x - 1",
    "x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1",
    "y = -2x",
    "y = 2x + 3",
    "y = x + 2",
]

_EVALUATIONS = [
    ("\\left( 3, \\frac{\\pi}{2} \\right)", "(3, \\frac{\\pi}{2})", 1.0),
    ("p - q", "\\frac{\\pi^2 \\lambda}{6} ", 0.0),
    ("90^\\circ", "90", 1.0),
    ("4", "2", 0.0),
    ("\\frac{3}{56}", "\\frac{8}{63}", 0.0),
    ("\\sqrt{51}", "10", 0.0),
    ("6 - 5i", "\\frac{3\\sqrt{2}}{2} + \\left(-3 + \\frac{3\\sqrt{2}}{2}\\right)i", 0.0),
    ("\\pi", "\\frac{\\pi}{2}", 0.0),
    ("28", "28^\\circ", 1.0),
    ("6+9i", "6 + 9i", 1.0),
    ("13535", "47", 0.0),
    ("x=5", "5", 1.0),
    ("1,-2", "0, 1", 0.0),
    ("144", "720", 0.0),
    ("11\\sqrt2", "11\\sqrt{2}", 1.0),
    ("70 \\sqrt{2}", "114.031", 0.0),
    ("(6,31,-1)", "(-3, 12, -1)", 0.0),
    ("\\frac{35}{64}", "\\frac{35}{128}", 0.0),
    ("x^3+3x-6", "x^3 + 3x - 6", 1.0),
    ("10", "10\\%", 1.0),
    ("2516_8", "12470", 0.0),
    ("(-2,1)", "(-2, 1)", 1.0),
    ("501", "2", 0.0),
    ("1", "3", 0.0),
    ("80", "110^\\circ", 0.0),
    ("1 \\pm \\sqrt{19}", "0", 0.0),
    ("2k+2", "2k + 2", 1.0),
    (
        "\\begin{pmatrix} -1/3 \\\\ 2/3 \\\\ 5/3 \\end{pmatrix}",
        "\\begin{pmatrix} -\\frac{1}{3} \\\\ \\frac{2}{3} \\\\ \\frac{5}{3} \\end{pmatrix}",
        1.0,
    ),
    ("145^\\circ", "75^\\circ", 0.0),
    ("(a+5)(b+2)", "(a + 5)(b + 2)", 1.0),
    ("(3,4]", "2", 0.0),
    ("40", "36", 0.0),
    ("\\frac43", "\\frac{4}{3}", 1.0),
    ("120^\\circ", "80^\\circ", 0.0),
    ("504", "63", 0.0),
    ("\\text{even}", "\\text{odd}", 0.0),
    ("1+274i", "i", 0.0),
    ("4210_{5}", "4210", 1.0),
    ("\\frac{3840}{289}", "\\frac{480}{17}", 0.0),
    ("3 \\sqrt{5}", "3\\sqrt{5}", 1.0),
    ("(15,-29)", "(15, -29)", 1.0),
    ("-2", "\\frac{1+\\sqrt{5}}{2}", 0.0),
    ("16", "32", 0.0),
    ("1", "0", 0.0),
    ("8", "\\frac{16}{3}", 0.0),
    ("2\\sqrt{113}", "4\\sqrt{13}", 0.0),
    ("30^\\circ", "90", 0.0),
    ("\\frac65", "\\frac{6}{5}", 1.0),
    ("\\dfrac{17}{50}", "\\frac{17}{50}", 1.0),
    ("-\\frac{35}{9}", "-\\frac{23}{9}", 0.0),
    ("-\\sqrt{3}", "-3", 0.0),
    ("\\frac{270}7\\text{ degrees}", "\\frac{990}{7}", 0.0),
    ("19", "12", 0.0),
    ("1736", "224", 0.0),
    (".0000672", "0.0000672", 1.0),
    ("30^\\circ", "60", 0.0),
    ("3", "50", 0.0),
    ("(2,\\infty)", "[2, \\infty)", 0.0),  # TODO
    ("160", "180", 0.0),
    ("10,\\!080", "10080", 1.0),
    ("0", "64", 0.0),
    ("\\left( \\frac{3}{2}, -13 \\right)", "\\left(\\frac{3}{2}, -13\\right)", 1.0),
    ("2", "1", 0.0),
    ("110", "85", 0.0),
    ("11,\\! 111,\\! 111,\\! 100", "1111111110", 0.0),
    ("11,\\! 111,\\! 111,\\! 100", "11111111100", 1.0),
    ("(-1,6)", "(-1, 6)", 1.0),
    ("\\frac{1}{2}", "\\frac{1}{4}", 0.0),
    ("54", "2", 0.0),
    ("\\frac{9}{256}", "\\frac{1}{16}", 0.0),
    ("\\text{(C)}", "\\text{C}", 1.0),
    ("288 \\pi", "288\\pi", 1.0),
    ("\\frac{16}{5}", "3.2", 1.0),
    ("30^\\circ", "30", 1.0),
    ("\\frac 59", "\\frac{5}{9}", 1.0),
    ("12", "9", 0.0),
    ("-4", "1 \\text{ and } -5", 0.0),
    ("16", "10", 0.0),
    ("116", "52", 0.0),
    ("\\$32,\\!348", "32348", 1.0),
    ("-13x+3", "-13x + 3", 1.0),
    ("\\begin{pmatrix} -1 & 0 \\\\ 0 & -1 \\end{pmatrix}", "\\mathbf{0}", 0.0),
    ("17", "21", 0.0),
    ("540", "7200", 0.0),
    ("81", "-19", 0.0),
    ("\\text{(E)}", "\\text{E}", 1.0),
    ("864 \\mbox{ inches}^2", "864", 1.0),
    ("120^\\circ", "120", 1.0),
    ("1\\frac{4}{5}", "8", 0.0),
    ("\\dfrac{33}{100}", "\\frac{33}{100}", 1.0),
    ("180^\\circ", "180", 1.0),
    ("18+2\\pi", "18 + 7\\pi", 0.0),
    ("11", "10", 0.0),
    ("3 \\pm 2 \\sqrt{2}", "3 + 2\\sqrt{2}, 3 - 2\\sqrt{2}", 1.0),
    ("440", "162", 0.0),
    ("\\frac{17}{21}", "6", 0.0),
    ("36", "108", 0.0),
    ("898", "256", 0.0),
    ("\\left(\\frac{3}{5},\\frac{8}{3}\\right]", "\\left( \\frac{3}{5}, \\frac{8}{3} \\right]", 1.0),
    ("\\text{(B)}", "\\text{B}", 1.0),
    ("5.4 \\text{ cents}", "5.4", 1.0),
    ("28", "21", 0.0),
    ("\\frac9{19}", "\\frac{9}{19}", 1.0),
    ("6", "2", 0.0),
    ("1+2\\sqrt{3}", "3\\sqrt{3}", 0.0),
    ("(5,\\infty)", "(5, \\infty)", 1.0),
    ("(2,4)", "(2, 4)", 1.0),
    ("\\frac{11+9a}{20}", "\\frac{11 + 9a}{20}", 1.0),
    ("120", "\\frac{100}{3}", 0.0),
    ("\\frac{9}{100}", "0.09", 1.0),
    ("15", "35", 0.0),
    ("\\frac{13}{6}", "\\dfrac{13}{6}", 1.0),
    ("4343_6", "4343", 1.0),
    ("55^\\circ", "113", 0.0),
    ("58,500", "14625", 0.0),
    ("6r^2-4r-24", "6r^2 - 4r - 24", 1.0),
    ("10080", "10,080", 1.0),
    ("11 \\sqrt{5} + 11", " 52 ", 0.0),
    ("100", "120", 0.0),
    ("\\frac{7}{4}", "-\\frac{7}{4}", 0.0),
    ("16 \\sqrt{3}", "4", 0.0),
    ("\\frac14", "\\frac{1}{4}", 1.0),
    ("(1,-16,-4,43)", "(1, -16, -4, 43)", 1.0),
    ("21", "166.5", 0.0),
    ("17", "5", 0.0),
    ("90^\\circ", "100^\\circ", 0.0),
    ("(8,-2)", "(8, -2)", 1.0),
    ("(0,9) \\cup (9,36)", "(0, 9)", 0.0),
    ("\\frac{1}{2}", "\\frac{5}{9}", 0.0),
    ("x \\in [-2,7]", "[-2, 7]", 1.0),
    ("\\frac{11}{2}", "5.5", 1.0),
    ("0", "5 + \\sqrt{7}", 0.0),
    ("\\sqrt{66}", "10", 0.0),
    ("\\frac 34", "\\frac{3}{4}", 1.0),
    ("-\\frac{3}{8}", "-\\frac{3}{16}", 0.0),
    ("\\text{Navin}", "Navin", 1.0),
    ("\\frac{13}{4}", "3", 0.0),
    ("\\begin{pmatrix} 1/5 \\\\ -18/5 \\end{pmatrix}", "\\begin{pmatrix} 4 \\\\ 0 \\end{pmatrix}", 0.0),
    ("2 \\sqrt{5}", "2\\sqrt{5}", 1.0),
    ("406", "349", 0.0),
    ("-2", "4", 0.0),
    ("\\begin{pmatrix} -7 \\\\ 16 \\\\ 5 \\end{pmatrix}", "\\begin{pmatrix} 9 \\\\ -12 \\\\ 75 \\end{pmatrix}", 0.0),
    (
        "\\begin{pmatrix} 16/49 \\\\ 48/49 \\\\ 24/49 \\end{pmatrix}",
        "\\begin{pmatrix} \\frac{16}{49} \\\\ \\frac{48}{49} \\\\ \\frac{24}{49} \\end{pmatrix}",
        1.0,
    ),
    ("27", "10", 0.0),
    ("\\{1\\pm\\sqrt{5},-2\\}", "\\{-1, 1, 1\\}", 0.0),
    ("3R^2", "\\frac{1}{3}(a^2 + b^2 + c^2) + 3R^2", 0.0),
    ("\\left[ \\frac{\\pi^2}{8}, \\frac{5 \\pi^2}{4} \\right]", "\\frac{\\pi^2}{4}", 0.0),
    ("331", "0", 0.0),
    (".35625", "0.35625", 1.0),
    ("\\frac{1}{2}", "\\frac{\\pi}{4(1+k)}", 0.0),
    ("15", "16", 0.0),
    ("y = 2x + 3", "y = x + 2", 0.0),
    ("-2,1", "1, -2", 1.0),
    ("\\$18.90", "18.90", 1.0),
    ("75^\\circ", "40^\\circ", 0.0),
    ("8 \\pi", "17\\pi", 0.0),
    ("15\\mbox{ cm}^2", "15", 1.0),
    ("27648", "3125", 0.0),
    ("137 \\frac{1}{2}", "137\\frac{1}{2}", 1.0),
    ("29", "70", 0.0),
    ("\\frac{2}{1005}", "-\\frac{1}{1005}", 0.0),
    ("8n^2 + 4n + 1", "2", 0.0),
    ("\\frac{8}{15}", "\\frac{4}{3}", 0.0),
    ("\\$36", "36", 1.0),
    ("14", "30", 0.0),
    ("(2,12) \\cup (12,102)", "(2, 12) \\cup (12, 102)", 1.0),
    ("\\frac{7}{2}", "4", 0.0),
    ("-1", "1", 0.0),
]
