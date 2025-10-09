"""
Utility methods for getting math word terms.
"""
import math

BINARY_OPERATORS = {
    '^', '*', '/', '+', '-', '.'
}

# Each key is an ISO 639-2 language code
# https://www.loc.gov/standards/iso639-2/php/code_list.php
MATH_WORDS = {
    'DUT': {
        'prefix_unary_operators': {
            'vierkantswortel van': 'sqrt',
            'wortel van': 'sqrt',
            'logaritme van': 'log'
        },
        'postfix_unary_operators': {
            'kwadraat': '^ 2'
        },
        'binary_operators': {
            'plus': '+',
            'gedeeld door': '/',
            'min': '-',
            'maal': '*',
            'tot de macht': '^',
            'tot de': '^'
        },
        'numbers': {
            'nul': 0,
            'een': 1,
            'één': 1,
            'twee': 2,
            'drie': 3,
            'vier': 4,
            'vijf': 5,
            'zes': 6,
            'zeven': 7,
            'acht': 8,
            'negen': 9,
            'tien': 10,
            'elf': 11,
            'twaalf': 12,
            'dertien': 13,
            'veertien': 14,
            'vijftien': 15,
            'zestien': 16,
            'zeventien': 17,
            'achttien': 18,
            'negentien': 19,
            'twintig': 20,
            'dertig': 30,
            'veertig': 40,
            'vijftig': 50,
            'zestig': 60,
            'zeventig': 70,
            'tachtig': 80,
            'negentig': 90
        },
        'scales': {
            'honderd': 100,
            'duizend': 1000,
            'miljoen': 1000000,
            'miljard': 1000000000,
            'biljard': 1000000000000
        }
    },
    'ENG': {
        'prefix_unary_operators': {
            'square root of': 'sqrt',
            'negative': 'neg',
            'logarithm of': 'log',
            'log of': 'log'
        },
        'postfix_unary_operators': {
            'squared': '^ 2',
            'cubed': '^ 3',
        },
        'binary_operators': {
            'plus': '+',
            'divided by': '/',
            'minus': '-',
            'times': '*',
            'to the power of': '^',
            'point': '.'
        },
        'numbers': {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90
        },
        'scales': {
            'hundred': 100,
            'thousand': 1000,
            'million': 1000000,
            'billion': 1000000000,
            'trillion': 1000000000000
        }
    },
    'FRE': {
        'prefix_unary_operators': {
            'racine carrée de': 'sqrt',
            'logarithme de': 'log'
        },
        'postfix_unary_operators': {
            'au carré': '^ 2',
            'au cube': '^ 3'
        },
        'binary_operators': {
            'plus': '+',
            'divisé par': '/',
            'moins': '-',
            'fois': '*',
            'équarri': '^ 2',
            'en cubes': '^ 3',
            'à la puissance': '^',
            'virgule': '.'
        },
        'numbers': {
            'zéro': 0,
            'un': 1,
            'deux': 2,
            'trois': 3,
            'quatre': 4,
            'cinq': 5,
            'six': 6,
            'sept': 7,
            'huit': 8,
            'neuf': 9,
            'dix': 10,
            'onze': 11,
            'douze': 12,
            'treize': 13,
            'quatorze': 14,
            'quinze': 15,
            'seize': 16,
            'dix-sept': 17,
            'dix-huit': 18,
            'dix-neuf': 19,
            'vingt': 20,
            'trente': 30,
            'quarante': 40,
            'cinquante': 50,
            'soixante': 60,
            'soixante-dix': 70,
            'septante': 70,
            'quatre-vingts': 80,
            'huitante': 80,
            'quatre-vingt-dix': 90,
            'nonante': 90
        },
        'scales': {
            'cent': 100,
            'mille': 1000,
            'un million': 1000000,
            'un milliard': 1000000000,
            'billions de': 1000000000000
        }
    },
    'GER': {
        'prefix_unary_operators': {
            'Quadratwurzel von': 'sqrt',
            'Wurzel von': 'sqrt',
            'Logarithmus von': 'log'
        },
        'postfix_unary_operators': {
            'quadriert': '^ 2',
            'hoch drei': '^ 3'
        },
        'binary_operators': {
            'plus': '+',
            'geteilt durch': '/',
            'geteilt': '/',
            'minus': '-',
            'mal': '*',
            'multipliziert mit': '*',
            'im Quadrat': '^ 2',
            'hoch zwei': '^ 2',
            'cubed': '^ 3',
            'hoch': '^'
        },
        'numbers': {
            'null': 0,
            'eins': 1,
            'zwei': 2,
            'drei': 3,
            'vier': 4,
            'fünf': 5,
            'sechs': 6,
            'sieben': 7,
            'acht': 8,
            'neun': 9,
            'zehn': 10,
            'elf': 11,
            'zwölf': 12,
            'dreizehn': 13,
            'vierzehn': 14,
            'fünfzehn': 15,
            'sechszehn': 16,
            'siebzehn': 17,
            'achtzehn': 18,
            'neunzehn': 19,
            'zwanzig': 20,
            'dreißig': 30,
            'vierzig': 40,
            'fünfzig': 50,
            'sechzig': 60,
            'siebzig': 70,
            'achtzig': 80,
            'neunzig': 90
        },
        'scales': {
            'hundert': 100,
            'tausend': 1000,
            'hunderttausend': 100000,
            'million': 1000000,
            'milliarde': 1000000000,
            'billion': 1000000000000
        }
    },
    'GRE': {
        'prefix_unary_operators': {
            'τετραγωνική ρίζα του': 'sqrt',
            'λογάριθμος του': 'log'
        },
        'postfix_unary_operators': {
            'στο τετράγωνο': '^ 2',
            'στον κύβο': '^ 3',
        },
        'binary_operators': {
            'συν': '+', 'και': '+',
            'διά': '/',
            'πλην': '-',
            'επί': '*',
            'στην δύναμη του': '^',
            'εις την': '^'
        },
        'numbers': {
            'μηδέν': 0,
            'ένα': 1,
            'δύο': 2,
            'τρία': 3,
            'τέσσερα': 4,
            'πέντε': 5,
            'έξι': 6,
            'εφτά': 7,
            'οκτώ': 8, 'οχτώ': 8,
            'εννιά': 9, 'εννέα': 9,
            'δέκα': 10,
            'έντεκα': 11,
            'δώδεκα': 12,
            'δεκατρία': 13,
            'δεκατέσσερα': 14,
            'δεκαπέντε': 15,
            'δεκαέξι': 16,
            'δεκαεφτά': 17,
            'δεκαοκτώ': 18, 'δεκαοχτώ': 18,
            'δεκαεννιά': 19, 'δεκαεννέα': 19,
            'είκοσι': 20,
            'τριάντα': 30,
            'σαράντα': 40,
            'πενήντα': 50,
            'εξήντα': 60,
            'εβδομήντα': 70,
            'ογδόντα': 80,
            'ενενήντα': 90
        },
        'scales': {
            'εκατό': 100,
            'χίλια': 1000,
            'εκατομμύρια': 1000000, 'εκ.': 1000000,
            'δισεκατομμύρια': 1000000000,
            'δισ.': 1000000000, 'δις': 1000000000,
            'τρισεκατομμύρια': 1000000000000,
            'τρισ.': 1000000000000, 'τρις': 1000000000000
        }
    },
    'ITA': {
        'prefix_unary_operators': {
            'radice quadrata di': 'sqrt',
            'logaritmo di': 'log'
        },
        'postfix_unary_operators': {
            'al quadrato': '^ 2',
            'al cubo': '^ 3'
        },
        'binary_operators': {
            'più': '+',
            'diviso': '/',
            'meno': '-',
            'per': '*',
            'al quadrato': '^ 2',
            'cubetti': '^ 3',
            'alla potenza di': '^'
        },
        'numbers': {
            'zero': 0,
            'uno': 1,
            'due': 2,
            'tre': 3,
            'quattro': 4,
            'cinque': 5,
            'sei': 6,
            'sette': 7,
            'otto': 8,
            'nove': 9,
            'dieci': 10,
            'undici': 11,
            'dodici': 12,
            'tredici': 13,
            'quattordici': 14,
            'quindici': 15,
            'sedici': 16,
            'diciassette': 17,
            'diciotto': 18,
            'diciannove': 19,
            'venti': 20,
            'trenta': 30,
            'quaranta': 40,
            'cinquanta': 50,
            'sessanta': 60,
            'settanta': 70,
            'ottanta': 80,
            'novanta': 90
        },
        'scales': {
            'centinaia': 100,
            'migliaia': 1000,
            'milioni': 1000000,
            'miliardi': 1000000000,
            'bilioni': 1000000000000
        }
    },
    'MAR': {
        'prefix_unary_operators': {
            'वर्गमूल': 'sqrt',
            'लॉगरिथम': 'log'
        },
        'postfix_unary_operators': {
            'वर्ग': '^ 2',
            'घन': '^ 3'
        },
        'binary_operators': {
            'बेरीज': '+',
            'भागाकार': '/',
            'वजाबाकी': '-',
            'गुणाकार': '*',
            '(संख्या)वर्ग': '^ 2',
            'छोटे': '^ 3',
            'गुण्या करण्यासाठी': '^'
        },
        'numbers': {
            'शून्य': 0,
            'एक': 1,
            'दोन': 2,
            'तीन': 3,
            'चार': 4,
            'पाच': 5,
            'सहा': 6,
            'सात': 7,
            'आठ': 8,
            'नऊ': 9,
            'दहा': 10,
            'अकरा': 11,
            'बारा': 12,
            'तेरा': 13,
            'चौदा': 14,
            'पंधरा': 15,
            'सोळा': 16,
            'सतरा': 17,
            'अठरा': 18,
            'एकोणीस': 19,
            'वीस': 20,
            'तीस': 30,
            'चाळीस': 40,
            'पन्नास': 50,
            'साठ': 60,
            'सत्तर': 70,
            'ऐंशी': 80,
            'नव्वद': 90,
            'शंभर': 100
        },
        'scales': {
            'शंभर': 100,
            'हजार': 1000,
            'दशलक्ष': 1000000,
            'अब्ज': 1000000000,
            'खर्व': 1000000000000
        }
    },
    'RUS': {
        'prefix_unary_operators': {
            'квадратный корень из': 'sqrt',
            'корень из': 'sqrt',
            'логарифм': 'log'
        },
        'postfix_unary_operators': {
            'в квадрате': '^ 2',
            'в кубе': '^ 3'
        },
        'binary_operators': {
            'плюс': '+',
            'разделить': '/',
            'деленное на': '/',
            'делить на': '/',
            'минус': '-',
            'вычесть': '-',
            'отнять': '-',
            'умножить': '*',
            'умноженное на': '*',
            'умножить на': '*',
            'квадрат': '^ 2',
            'в квадрате': '^ 2',
            'возведенный в куб': '^ 3',
            'степень': '^'
        },
        'numbers': {
            'ноль': 0,
            'один': 1,
            'два': 2,
            'три': 3,
            'четыре': 4,
            'пять': 5,
            'шесть': 6,
            'семь': 7,
            'восемь': 8,
            'девять': 9,
            'десять': 10,
            'одинадцать': 11,
            'двенадцать': 12,
            'тринадцать': 13,
            'четырнадцать': 14,
            'пятнадцать': 15,
            'шестнадцать': 16,
            'семнадцать': 17,
            'восемнадцать': 18,
            'девятнадцать': 19,
            'двадцать': 20,
            'тридцать': 30,
            'сорок': 40,
            'пятьдесят': 50,
            'шестьдесят': 60,
            'семьдесят': 70,
            'восемьдесят': 80,
            'девяносто': 90
        },
        'scales': {
            'сто': 100,
            'тысяч': 1000,
            'миллион': 1000000,
            'миллиард': 1000000000,
            'триллион': 1000000000000
        }
    },
    'POR': {
        'prefix_unary_operators': {
            'raiz quadrada de': 'sqrt',
            'logaritmo de': 'log'
        },
        'postfix_unary_operators': {
            'ao quadrado': '^ 2',
            'ao cubo': '^ 3',
        },
        'binary_operators': {
            'mais': '+',
            'dividido por': '/',
            'menos': '-',
            'vezes': '*',
            'elevado à potência de': '^'
        },
        'numbers': {
            'zero': 0,
            'um': 1,
            'dois': 2,
            'três': 3,
            'quatro': 4,
            'cinco': 5,
            'seis': 6,
            'sete': 7,
            'oito': 8,
            'nove': 9,
            'dez': 10,
            'onze': 11,
            'doze': 12,
            'treze': 13,
            'quatorze': 14,
            'catorze': 14,
            'quinze': 15,
            'dezesseis': 16,
            'dezessete': 17,
            'dezoito': 18,
            'dezenove': 19,
            'vinte': 20,
            'trinta': 30,
            'quarenta': 40,
            'cinquenta': 50,
            'sessenta': 60,
            'setenta': 70,
            'oitenta': 80,
            'noventa': 90
        },
        'scales': {
            'cem': 100,
            'mil': 1000,
            'milhão': 1000000,
            'bilhão': 1000000000,
            'trilhão': 1000000000000
        }
    },
    'UKR': {
        'prefix_unary_operators': {
            'квадратний корінь з': 'sqrt',
            'корінь з': 'sqrt',
            'логарифм': 'log'
        },
        'postfix_unary_operators': {
            'у квадраті': '^ 2',
            'у кубі': '^ 3'
        },
        'binary_operators': {
            'додати': '+',
            'розділити': '/',
            'поділити на': '/',
            'ділити на': '/',
            'мінус': '-',
            'відняти': '-',
            'відняти від': '-',
            'помножити': '*',
            'помножене на': '*',
            'помножити на': '*',
            'квадрат': '^ 2',
            'у квадраті': '^ 2',
            'зведений у куб': '^ 3',
            'ступінь': '^'
        },
        'numbers': {
            'нуль': 0,
            'один': 1,
            'два': 2,
            'три': 3,
            'чотири': 4,
            'п’ять': 5,
            'шість': 6,
            'сім': 7,
            'вісім': 8,
            'дев’ять': 9,
            'десять': 10,
            'одинадцять': 11,
            'дванадцять': 12,
            'тринадцять': 13,
            'чотирнадцять': 14,
            'п’ятнадцять': 15,
            'шістнадцять': 16,
            'сімнадцять': 17,
            'вісімнадцять': 18,
            'дев’ятнадцять': 19,
            'двадцять': 20,
            'тридцять': 30,
            'сорок': 40,
            'п’ятдесят': 50,
            'шістдесят': 60,
            'сімдесят': 70,
            'вісімдесят': 80,
            'дев’яносто': 90
        },
        'scales': {
            'сто': 100,
            'тисяча': 1000,
            'мільйон': 1000000,
            'мільярд': 1000000000,
            'трильйон': 1000000000000
        }
    },
    'ESP': {
        'prefix_unary_operators': {
            'raiz cuadrada de': 'sqrt',
            'logaritmo de': 'log'
        },
        'postfix_unary_operators': {
            'al cuadrado': '^ 2',
            'al cubo': '^ 3',
        },
        'binary_operators': {
            'más': '+',
            'entre': '/',
            'menos': '-',
            'por': '*',
            'veces': '*',
            'elevado al': '^',
            'punto': '.'
        },
        'numbers': {
            'cero': 0,
            'uno': 1,
            'dos': 2,
            'tres': 3,
            'cuatro': 4,
            'cinco': 5,
            'seis': 6,
            'siete': 7,
            'ocho': 8,
            'nueve': 9,
            'diez': 10,
            'once': 11,
            'doce': 12,
            'trece': 13,
            'catorce': 14,
            'quince': 15,
            'dieciséis': 16,
            'diecisiete': 17,
            'dieciocho': 18,
            'diecinueve': 19,
            'veinte': 20,
            'treinta': 30,
            'cuarenta': 40,
            'cincuenta': 50,
            'sesenta': 60,
            'setenta': 70,
            'ochenta': 80,
            'noventa': 90
        },
        'scales': {
            'cien': 100,
            'mil': 1000,
            'millon': 1000000,
            'billon': 1000000000,
            'trillon': 1000000000000
        }
    },
    'THA': {
        'prefix_unary_operators': {
            'สแควรูท': 'sqrt',
            'ลอการิทึม': 'log'
        },
        'postfix_unary_operators': {
            'ยกกำลังสอง': '^ 2',
            'ยกกำลังสาม': '^ 3'
        },
        'binary_operators': {
            'บวก': '+',
            'หาร': '/',
            'ลบ': '-',
            'คูณ': '*',
            'ยกกำลัง': '^'
        },
        'numbers': {
            'ศูนย์': 0,
            'หนึ่ง': 1,
            'สอง': 2,
            'สาม': 3,
            'สี่': 4,
            'ห้า': 5,
            'หก': 6,
            'เจ็ด': 7,
            'แปด': 8,
            'เก้า': 9,
            'สิบ': 10,
            'สิบเอ็ด': 11,
            'สิบสอง': 12,
            'สิบสาม': 13,
            'สิบสี่': 14,
            'สิบห้า': 15,
            'สิบหก': 16,
            'สิบเจ็ด': 17,
            'สิบแปด': 18,
            'สิบเก้า': 19,
            'ยี่สิบ': 20,
            'สามสิบ': 30,
            'สี่สิบ': 40,
            'ห้าสิบ': 50,
            'หกสิบ': 60,
            'เจ็ดสิบ': 70,
            'แปดสิบ': 80,
            'เก้าสิบ': 90
        },
        'scales': {
            'ร้อย': 100,
            'พัน': 1000,
            'หมื่น': 10000,
            'แสน': 100000,
            'ล้าน': 1000000,
            'พันล้าน': 1000000000,
            'ล้านล้าน': 1000000000000
        }
    },
    'CHI': {
        'prefix_unary_operators': {
            '平方根': 'sqrt',
            '开方': 'sqrt',
            '负': 'neg',
            '对数': 'log'
        },
        'postfix_unary_operators': {
            '平方': '^ 2',
            '立方': '^ 3',
            '的平方': '^ 2',
            '的立方': '^ 3'
        },
        'binary_operators': {
            '加': '+',
            '加上': '+',
            '加法': '+',
            '除以': '/',
            '除': '/',
            '除法': '/',
            '减': '-',
            '减去': '-',
            '减法': '-',
            '乘': '*',
            '乘以': '*',
            '乘法': '*',
            '乘上': '*',
            '倍': '*',
            '的': '^',
            '次方': '^',
            '次幂': '^'
        },
        'numbers': {
            '零': 0,
            '一': 1,
            '二': 2,
            '三': 3,
            '四': 4,
            '五': 5,
            '六': 6,
            '七': 7,
            '八': 8,
            '九': 9,
            '十': 10,
            '十一': 11,
            '十二': 12,
            '十三': 13,
            '十四': 14,
            '十五': 15,
            '十六': 16,
            '十七': 17,
            '十八': 18,
            '十九': 19,
            '二十': 20,
            '三十': 30,
            '四十': 40,
            '五十': 50,
            '六十': 60,
            '七十': 70,
            '八十': 80,
            '九十': 90,
            '壹': 1,
            '贰': 2,
            '两': 2,
            '叁': 3,
            '肆': 4,
            '伍': 5,
            '陆': 6,
            '柒': 7,
            '捌': 8,
            '玖': 9,
            '拾': 10
        },
        'scales': {
            '十': 10,
            '百': 100,
            '千': 1000,
            '万': 10000,
            '十万': 100000,
            '百万': 1000000,
            '千万': 10000000,
            '亿': 100000000,
            '十亿': 1000000000,
            '百亿': 10000000000,
            '千亿': 100000000000,
            '万亿': 1000000000000
        }
    },
    'JPN': {
        'prefix_unary_operators': {
            '平方根': 'sqrt',
            'ルート': 'sqrt',
            '負の': 'neg'
        },
        'postfix_unary_operators': {
            '二乗': '^ 2',
            '三乗': '^ 3',
            'の二乗': '^ 2',
            'の三乗': '^ 3'
        },
        'binary_operators': {
            'たす': '+',
            'プラス': '+',
            'わる': '/',
            '割る': '/',
            'ひく': '-',
            'マイナス': '-',
            'かける': '*',
            '掛ける': '*',
            '乗': '^',
            'の': '^'
        },
        'numbers': {
            'ゼロ': 0, '零': 0,
            '一': 1, 'いち': 1,
            '二': 2, 'に': 2,
            '三': 3, 'さん': 3,
            '四': 4, 'し': 4, 'よん': 4,
            '五': 5, 'ご': 5,
            '六': 6, 'ろく': 6,
            '七': 7, 'しち': 7, 'なな': 7,
            '八': 8, 'はち': 8,
            '九': 9, 'きゅう': 9, 'く': 9,
            '十': 10, 'じゅう': 10,
            '十一': 11, 'じゅういち': 11,
            '十二': 12, 'じゅうに': 12,
            '十三': 13, 'じゅうさん': 13,
            '十四': 14, 'じゅうし': 14,
            '十五': 15, 'じゅうご': 15,
            '十六': 16, 'じゅうろく': 16,
            '十七': 17, 'じゅうしち': 17,
            '十八': 18, 'じゅうはち': 18,
            '十九': 19, 'じゅうきゅう': 19,
            '二十': 20, 'にじゅう': 20,
            '三十': 30, 'さんじゅう': 30,
            '四十': 40, 'よんじゅう': 40,
            '五十': 50, 'ごじゅう': 50,
            '六十': 60, 'ろくじゅう': 60,
            '七十': 70, 'ななじゅう': 70,
            '八十': 80, 'はちじゅう': 80,
            '九十': 90, 'きゅうじゅう': 90
        },
        'scales': {
            '百': 100, 'ひゃく': 100,
            '千': 1000, 'せん': 1000,
            '万': 10000, 'まん': 10000,
            '十万': 100000,
            '百万': 1000000,
            '千万': 10000000,
            '億': 100000000, 'おく': 100000000,
            '兆': 1000000000000, 'ちょう': 1000000000000
        }
    },
    'KOR': {
        'prefix_unary_operators': {
            '제곱근': 'sqrt',
            '루트': 'sqrt'
        },
        'postfix_unary_operators': {
            '제곱': '^ 2',
            '세제곱': '^ 3'
        },
        'binary_operators': {
            '더하기': '+',
            '플러스': '+',
            '나누기': '/',
            '빼기': '-',
            '마이너스': '-',
            '곱하기': '*',
            '곱': '*',
            '의': '^',
            '승': '^'
        },
        'numbers': {
            '영': 0, '공': 0,
            '일': 1, '하나': 1,
            '이': 2, '둘': 2,
            '삼': 3, '셋': 3,
            '사': 4, '넷': 4,
            '오': 5, '다섯': 5,
            '육': 6, '여섯': 6,
            '칠': 7, '일곱': 7,
            '팔': 8, '여덟': 8,
            '구': 9, '아홉': 9,
            '십': 10, '열': 10,
            '십일': 11,
            '십이': 12,
            '십삼': 13,
            '십사': 14,
            '십오': 15,
            '십육': 16,
            '십칠': 17,
            '십팔': 18,
            '십구': 19,
            '이십': 20, '스물': 20,
            '삼십': 30, '서른': 30,
            '사십': 40, '마흔': 40,
            '오십': 50, '쉰': 50,
            '육십': 60, '예순': 60,
            '칠십': 70, '일흔': 70,
            '팔십': 80, '여든': 80,
            '구십': 90, '아흔': 90
        },
        'scales': {
            '백': 100,
            '천': 1000,
            '만': 10000,
            '십만': 100000,
            '백만': 1000000,
            '천만': 10000000,
            '억': 100000000,
            '조': 1000000000000
        }
    },
    'VIE': {
        'prefix_unary_operators': {
            'căn bậc hai': 'sqrt',
            'căn': 'sqrt'
        },
        'postfix_unary_operators': {
            'bình phương': '^ 2',
            'lập phương': '^ 3'
        },
        'binary_operators': {
            'cộng': '+',
            'thêm': '+',
            'chia': '/',
            'chia cho': '/',
            'trừ': '-',
            'bớt': '-',
            'nhân': '*',
            'lũy thừa': '^'
        },
        'numbers': {
            'không': 0,
            'một': 1, 'mốt': 1,
            'hai': 2,
            'ba': 3,
            'bốn': 4, 'tư': 4,
            'năm': 5, 'lăm': 5,
            'sáu': 6,
            'bảy': 7, 'bẩy': 7,
            'tám': 8,
            'chín': 9,
            'mười': 10,
            'mười một': 11,
            'mười hai': 12,
            'mười ba': 13,
            'mười bốn': 14,
            'mười lăm': 15,
            'mười sáu': 16,
            'mười bảy': 17,
            'mười tám': 18,
            'mười chín': 19,
            'hai mươi': 20,
            'ba mươi': 30,
            'bốn mươi': 40,
            'năm mươi': 50,
            'sáu mươi': 60,
            'bảy mươi': 70,
            'tám mươi': 80,
            'chín mươi': 90
        },
        'scales': {
            'trăm': 100,
            'nghìn': 1000, 'ngàn': 1000,
            'triệu': 1000000,
            'tỷ': 1000000000,
            'nghìn tỷ': 1000000000000
        }
    },
    'HIN': {
        'prefix_unary_operators': {
            'वर्गमूल': 'sqrt',
            'ऋणात्मक': 'neg'
        },
        'postfix_unary_operators': {
            'वर्ग': '^ 2',
            'घन': '^ 3'
        },
        'binary_operators': {
            'जोड़': '+',
            'प्लस': '+',
            'भाग': '/',
            'विभाजित': '/',
            'घटा': '-',
            'माइनस': '-',
            'गुणा': '*',
            'घात': '^'
        },
        'numbers': {
            'शून्य': 0,
            'एक': 1,
            'दो': 2,
            'तीन': 3,
            'चार': 4,
            'पाँच': 5, 'पांच': 5,
            'छह': 6, 'छः': 6,
            'सात': 7,
            'आठ': 8,
            'नौ': 9,
            'दस': 10,
            'ग्यारह': 11,
            'बारह': 12,
            'तेरह': 13,
            'चौदह': 14,
            'पंद्रह': 15,
            'सोलह': 16,
            'सत्रह': 17,
            'अठारह': 18,
            'उन्नीस': 19,
            'बीस': 20,
            'तीस': 30,
            'चालीस': 40,
            'पचास': 50,
            'साठ': 60,
            'सत्तर': 70,
            'अस्सी': 80,
            'नब्बे': 90
        },
        'scales': {
            'सौ': 100,
            'हजार': 1000,
            'लाख': 100000,
            'दस लाख': 1000000,
            'करोड़': 10000000,
            'अरब': 1000000000,
            'खरब': 100000000000
        }
    },
    'ARA': {
        'prefix_unary_operators': {
            'الجذر التربيعي': 'sqrt',
            'جذر': 'sqrt',
            'سالب': 'neg'
        },
        'postfix_unary_operators': {
            'تربيع': '^ 2',
            'مكعب': '^ 3',
            'مربع': '^ 2'
        },
        'binary_operators': {
            'زائد': '+',
            'جمع': '+',
            'مقسوم على': '/',
            'قسمة': '/',
            'ناقص': '-',
            'طرح': '-',
            'ضرب': '*',
            'في': '*',
            'أس': '^',
            'قوة': '^'
        },
        'numbers': {
            'صفر': 0,
            'واحد': 1,
            'اثنان': 2, 'اثنين': 2,
            'ثلاثة': 3,
            'أربعة': 4,
            'خمسة': 5,
            'ستة': 6,
            'سبعة': 7,
            'ثمانية': 8,
            'تسعة': 9,
            'عشرة': 10,
            'أحد عشر': 11,
            'اثنا عشر': 12,
            'ثلاثة عشر': 13,
            'أربعة عشر': 14,
            'خمسة عشر': 15,
            'ستة عشر': 16,
            'سبعة عشر': 17,
            'ثمانية عشر': 18,
            'تسعة عشر': 19,
            'عشرون': 20,
            'ثلاثون': 30,
            'أربعون': 40,
            'خمسون': 50,
            'ستون': 60,
            'سبعون': 70,
            'ثمانون': 80,
            'تسعون': 90
        },
        'scales': {
            'مئة': 100, 'مائة': 100,
            'ألف': 1000,
            'مليون': 1000000,
            'مليار': 1000000000,
            'تريليون': 1000000000000
        }
    },
    'HEB': {
        'prefix_unary_operators': {
            'שורש ריבועי': 'sqrt',
            'שורש': 'sqrt',
            'שלילי': 'neg'
        },
        'postfix_unary_operators': {
            'בריבוע': '^ 2',
            'בחזקת שלוש': '^ 3',
            'בשלישית': '^ 3'
        },
        'binary_operators': {
            'פלוס': '+',
            'ועוד': '+',
            'חלקי': '/',
            'חילוק': '/',
            'מינוס': '-',
            'פחות': '-',
            'כפול': '*',
            'פעמים': '*',
            'בחזקת': '^',
            'חזקה': '^'
        },
        'numbers': {
            'אפס': 0,
            'אחד': 1, 'אחת': 1,
            'שניים': 2, 'שתיים': 2,
            'שלושה': 3, 'שלוש': 3,
            'אַרבעה': 4, 'ארבע': 4,
            'חמישה': 5, 'חמש': 5,
            'שישה': 6, 'שש': 6,
            'שבעה': 7, 'שבע': 7,
            'שמונה': 8, 'שמונה': 8,
            'תשעה': 9, 'תשע': 9,
            'עשרה': 10, 'עשר': 10,
            'אחד עשר': 11,
            'שנים עשר': 12,
            'שלושה עשר': 13,
            'ארבעה עשר': 14,
            'חמישה עשר': 15,
            'שישה עשר': 16,
            'שבעה עשר': 17,
            'שמונה עשר': 18,
            'תשעה עשר': 19,
            'עשרים': 20,
            'שלושים': 30,
            'ארבעים': 40,
            'חמישים': 50,
            'שישים': 60,
            'שבעים': 70,
            'שמונים': 80,
            'תשעים': 90
        },
        'scales': {
            'מאה': 100,
            'אלף': 1000,
            'מיליון': 1000000,
            'מיליארד': 1000000000,
            'טריליון': 1000000000000
        }
    },
    'TUR': {
        'prefix_unary_operators': {
            'karekök': 'sqrt',
            'negatif': 'neg'
        },
        'postfix_unary_operators': {
            'kare': '^ 2',
            'küp': '^ 3'
        },
        'binary_operators': {
            'artı': '+',
            'toplama': '+',
            'bölü': '/',
            'bölme': '/',
            'eksi': '-',
            'çıkarma': '-',
            'çarpı': '*',
            'çarpma': '*',
            'üzeri': '^',
            'kuvvet': '^'
        },
        'numbers': {
            'sıfır': 0,
            'bir': 1,
            'iki': 2,
            'üç': 3,
            'dört': 4,
            'beş': 5,
            'altı': 6,
            'yedi': 7,
            'sekiz': 8,
            'dokuz': 9,
            'on': 10,
            'on bir': 11,
            'on iki': 12,
            'on üç': 13,
            'on dört': 14,
            'on beş': 15,
            'on altı': 16,
            'on yedi': 17,
            'on sekiz': 18,
            'on dokuz': 19,
            'yirmi': 20,
            'otuz': 30,
            'kırk': 40,
            'elli': 50,
            'altmış': 60,
            'yetmiş': 70,
            'seksen': 80,
            'doksan': 90
        },
        'scales': {
            'yüz': 100,
            'bin': 1000,
            'milyon': 1000000,
            'milyar': 1000000000,
            'trilyon': 1000000000000
        }
    },
    'SWE': {
        'prefix_unary_operators': {
            'kvadratroten av': 'sqrt',
            'roten ur': 'sqrt'
        },
        'postfix_unary_operators': {
            'i kvadrat': '^ 2',
            'i kubik': '^ 3'
        },
        'binary_operators': {
            'plus': '+',
            'delat med': '/',
            'minus': '-',
            'gånger': '*',
            'multiplicerat med': '*',
            'upphöjt till': '^'
        },
        'numbers': {
            'noll': 0,
            'ett': 1, 'en': 1,
            'två': 2,
            'tre': 3,
            'fyra': 4,
            'fem': 5,
            'sex': 6,
            'sju': 7,
            'åtta': 8,
            'nio': 9,
            'tio': 10,
            'elva': 11,
            'tolv': 12,
            'tretton': 13,
            'fjorton': 14,
            'femton': 15,
            'sexton': 16,
            'sjutton': 17,
            'arton': 18,
            'nitton': 19,
            'tjugo': 20,
            'trettio': 30,
            'fyrtio': 40,
            'femtio': 50,
            'sextio': 60,
            'sjuttio': 70,
            'åttio': 80,
            'nittio': 90
        },
        'scales': {
            'hundra': 100,
            'tusen': 1000,
            'miljon': 1000000,
            'miljard': 1000000000,
            'biljon': 1000000000000
        }
    },
    'NOR': {
        'prefix_unary_operators': {
            'kvadratrot av': 'sqrt',
            'rot av': 'sqrt'
        },
        'postfix_unary_operators': {
            'i andre': '^ 2',
            'i tredje': '^ 3'
        },
        'binary_operators': {
            'pluss': '+',
            'delt på': '/',
            'minus': '-',
            'ganger': '*',
            'multiplisert med': '*',
            'opphøyd i': '^'
        },
        'numbers': {
            'null': 0,
            'en': 1, 'ett': 1,
            'to': 2,
            'tre': 3,
            'fire': 4,
            'fem': 5,
            'seks': 6,
            'sju': 7, 'syv': 7,
            'åtte': 8,
            'ni': 9,
            'ti': 10,
            'elleve': 11,
            'tolv': 12,
            'tretten': 13,
            'fjorten': 14,
            'femten': 15,
            'seksten': 16,
            'sytten': 17,
            'atten': 18,
            'nitten': 19,
            'tjue': 20,
            'tretti': 30,
            'førti': 40,
            'femti': 50,
            'seksti': 60,
            'sytti': 70,
            'åtti': 80,
            'nitti': 90
        },
        'scales': {
            'hundre': 100,
            'tusen': 1000,
            'million': 1000000,
            'milliard': 1000000000,
            'billion': 1000000000000
        }
    },
    'DAN': {
        'prefix_unary_operators': {
            'kvadratrod af': 'sqrt',
            'rod af': 'sqrt'
        },
        'postfix_unary_operators': {
            'i anden': '^ 2',
            'i tredje': '^ 3'
        },
        'binary_operators': {
            'plus': '+',
            'divideret med': '/',
            'minus': '-',
            'gange': '*',
            'multipliceret med': '*',
            'opløftet i': '^'
        },
        'numbers': {
            'nul': 0,
            'en': 1, 'et': 1,
            'to': 2,
            'tre': 3,
            'fire': 4,
            'fem': 5,
            'seks': 6,
            'syv': 7,
            'otte': 8,
            'ni': 9,
            'ti': 10,
            'elleve': 11,
            'tolv': 12,
            'tretten': 13,
            'fjorten': 14,
            'femten': 15,
            'seksten': 16,
            'sytten': 17,
            'atten': 18,
            'nitten': 19,
            'tyve': 20,
            'tredive': 30,
            'fyrre': 40, 'fyrretyve': 40,
            'halvtreds': 50,
            'tres': 60,
            'halvfjerds': 70,
            'firs': 80,
            'halvfems': 90
        },
        'scales': {
            'hundrede': 100,
            'tusind': 1000,
            'million': 1000000,
            'milliard': 1000000000,
            'billion': 1000000000000
        }
    },
    'FIN': {
        'prefix_unary_operators': {
            'neliöjuuri': 'sqrt',
            'juuri': 'sqrt'
        },
        'postfix_unary_operators': {
            'toiseen': '^ 2',
            'kolmanteen': '^ 3'
        },
        'binary_operators': {
            'plus': '+',
            'jaettuna': '/',
            'miinus': '-',
            'kertaa': '*',
            'kerrottuna': '*',
            'potenssiin': '^'
        },
        'numbers': {
            'nolla': 0,
            'yksi': 1,
            'kaksi': 2,
            'kolme': 3,
            'neljä': 4,
            'viisi': 5,
            'kuusi': 6,
            'seitsemän': 7,
            'kahdeksan': 8,
            'yhdeksän': 9,
            'kymmenen': 10,
            'yksitoista': 11,
            'kaksitoista': 12,
            'kolmetoista': 13,
            'neljätoista': 14,
            'viisitoista': 15,
            'kuusitoista': 16,
            'seitsemäntoista': 17,
            'kahdeksantoista': 18,
            'yhdeksäntoista': 19,
            'kaksikymmentä': 20,
            'kolmekymmentä': 30,
            'neljäkymmentä': 40,
            'viisikymmentä': 50,
            'kuusikymmentä': 60,
            'seitsemänkymmentä': 70,
            'kahdeksankymmentä': 80,
            'yhdeksänkymmentä': 90
        },
        'scales': {
            'sata': 100,
            'tuhat': 1000,
            'miljoona': 1000000,
            'miljardi': 1000000000,
            'biljoona': 1000000000000
        }
    },
    'POL': {
        'prefix_unary_operators': {
            'pierwiastek kwadratowy z': 'sqrt',
            'pierwiastek z': 'sqrt'
        },
        'postfix_unary_operators': {
            'do kwadratu': '^ 2',
            'do sześcianu': '^ 3'
        },
        'binary_operators': {
            'plus': '+',
            'podzielone przez': '/',
            'dzielone przez': '/',
            'minus': '-',
            'razy': '*',
            'pomnożone przez': '*',
            'do potęgi': '^'
        },
        'numbers': {
            'zero': 0,
            'jeden': 1, 'jedna': 1,
            'dwa': 2, 'dwie': 2,
            'trzy': 3,
            'cztery': 4,
            'pięć': 5,
            'sześć': 6,
            'siedem': 7,
            'osiem': 8,
            'dziewięć': 9,
            'dziesięć': 10,
            'jedenaście': 11,
            'dwanaście': 12,
            'trzynaście': 13,
            'czternaście': 14,
            'piętnaście': 15,
            'szesnaście': 16,
            'siedemnaście': 17,
            'osiemnaście': 18,
            'dziewiętnaście': 19,
            'dwadzieścia': 20,
            'trzydzieści': 30,
            'czterdzieści': 40,
            'pięćdziesiąt': 50,
            'sześćdziesiąt': 60,
            'siedemdziesiąt': 70,
            'osiemdziesiąt': 80,
            'dziewięćdziesiąt': 90
        },
        'scales': {
            'sto': 100,
            'tysiąc': 1000,
            'milion': 1000000,
            'miliard': 1000000000,
            'bilion': 1000000000000
        }
    },
    'CZE': {
        'prefix_unary_operators': {
            'druhá odmocnina': 'sqrt',
            'odmocnina': 'sqrt'
        },
        'postfix_unary_operators': {
            'na druhou': '^ 2',
            'na třetí': '^ 3'
        },
        'binary_operators': {
            'plus': '+',
            'děleno': '/',
            'minus': '-',
            'krát': '*',
            'násobeno': '*',
            'na': '^'
        },
        'numbers': {
            'nula': 0,
            'jeden': 1, 'jedna': 1, 'jedno': 1,
            'dva': 2, 'dvě': 2,
            'tři': 3,
            'čtyři': 4,
            'pět': 5,
            'šest': 6,
            'sedm': 7,
            'osm': 8,
            'devět': 9,
            'deset': 10,
            'jedenáct': 11,
            'dvanáct': 12,
            'třináct': 13,
            'čtrnáct': 14,
            'patnáct': 15,
            'šestnáct': 16,
            'sedmnáct': 17,
            'osmnáct': 18,
            'devatenáct': 19,
            'dvacet': 20,
            'třicet': 30,
            'čtyřicet': 40,
            'padesát': 50,
            'šedesát': 60,
            'sedmdesát': 70,
            'osmdesát': 80,
            'devadesát': 90
        },
        'scales': {
            'sto': 100,
            'tisíc': 1000,
            'milion': 1000000,
            'miliarda': 1000000000,
            'bilion': 1000000000000
        }
    },
    'HUN': {
        'prefix_unary_operators': {
            'négyzetgyök': 'sqrt',
            'gyök': 'sqrt'
        },
        'postfix_unary_operators': {
            'négyzet': '^ 2',
            'köb': '^ 3'
        },
        'binary_operators': {
            'plusz': '+',
            'osztva': '/',
            'mínusz': '-',
            'szorozva': '*',
            'szor': '*',
            'hatványon': '^'
        },
        'numbers': {
            'nulla': 0,
            'egy': 1,
            'kettő': 2, 'két': 2,
            'három': 3,
            'négy': 4,
            'öt': 5,
            'hat': 6,
            'hét': 7,
            'nyolc': 8,
            'kilenc': 9,
            'tíz': 10,
            'tizenegy': 11,
            'tizenkettő': 12,
            'tizenhárom': 13,
            'tizennégy': 14,
            'tizenöt': 15,
            'tizenhat': 16,
            'tizenhét': 17,
            'tizennyolc': 18,
            'tizenkilenc': 19,
            'húsz': 20,
            'harminc': 30,
            'negyven': 40,
            'ötven': 50,
            'hatvan': 60,
            'hetven': 70,
            'nyolcvan': 80,
            'kilencven': 90
        },
        'scales': {
            'száz': 100,
            'ezer': 1000,
            'millió': 1000000,
            'milliárd': 1000000000,
            'billió': 1000000000000
        }
    },
    'RON': {
        'prefix_unary_operators': {
            'radical din': 'sqrt',
            'rădăcină pătrată din': 'sqrt'
        },
        'postfix_unary_operators': {
            'la pătrat': '^ 2',
            'la cub': '^ 3'
        },
        'binary_operators': {
            'plus': '+',
            'împărțit la': '/',
            'minus': '-',
            'înmulțit cu': '*',
            'ori': '*',
            'la puterea': '^'
        },
        'numbers': {
            'zero': 0,
            'unu': 1, 'una': 1,
            'doi': 2, 'două': 2,
            'trei': 3,
            'patru': 4,
            'cinci': 5,
            'șase': 6,
            'șapte': 7,
            'opt': 8,
            'nouă': 9,
            'zece': 10,
            'unsprezece': 11,
            'doisprezece': 12,
            'treisprezece': 13,
            'paisprezece': 14,
            'cincisprezece': 15,
            'șaisprezece': 16,
            'șaptesprezece': 17,
            'optsprezece': 18,
            'nouăsprezece': 19,
            'douăzeci': 20,
            'treizeci': 30,
            'patruzeci': 40,
            'cincizeci': 50,
            'șaizeci': 60,
            'șaptezeci': 70,
            'optzeci': 80,
            'nouăzeci': 90
        },
        'scales': {
            'sută': 100,
            'mie': 1000,
            'milion': 1000000,
            'miliard': 1000000000,
            'trilion': 1000000000000
        }
    }
}


LANGUAGE_CODES = list(MATH_WORDS.keys())


CONSTANTS = {
    'pi': 3.141693,
    'π': 3.141693,
    'e': 2.718281
}


UNARY_FUNCTIONS = {
    'sqrt': math.sqrt,

    # Most people assume a log of base 10 when a base is not specified
    'log': math.log10,

    # Unary minus function for negative numbers
    'neg': lambda x: -x
}


class InvalidLanguageCodeException(Exception):
    """
    Exception to be raised when a language code is specified that is not a part
    of the ISO 639-2 standard, or if the specified language is not yet
    supported by mathparse.
    """
    pass


def word_groups_for_language(language_code: str) -> dict[str, dict[str, str]]:
    """
    Return the math word groups for a language code.
    The language_code should be an ISO 639-2 language code.
    https://www.loc.gov/standards/iso639-2/php/code_list.php
    """

    if language_code not in LANGUAGE_CODES:
        message = '{} is not an available language code'.format(language_code)
        raise InvalidLanguageCodeException(message)

    return MATH_WORDS[language_code]


def words_for_language(language_code: str) -> set[str]:
    """
    Return the math words for a language code.
    The language_code should be an ISO 639-2 language code.
    https://www.loc.gov/standards/iso639-2/php/code_list.php
    """
    word_groups = word_groups_for_language(language_code)
    words = set()

    for group in word_groups:
        words.update(word_groups[group].keys())

    return words
