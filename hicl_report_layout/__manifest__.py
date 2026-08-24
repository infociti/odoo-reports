{
    'name': 'HICL Report Layout - Header on First Page Only',
    'version': '19.0.1.12.5',
    'summary': 'Quotation & Invoice: Bubble layout, header page 1 only, repeating table header, single-line footer, A4.',
    'author': 'HICL', 'category': 'Technical',
    'depends': ['web', 'sale', 'account'],
    'data': ['data/paperformat.xml', 'views/report_layout.xml'],
    'assets': {'web.report_assets_common': ['hicl_report_layout/static/src/scss/report.scss']},
    'license': 'LGPL-3', 'installable': True, 'application': False,
}
