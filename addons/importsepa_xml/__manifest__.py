

{
    'name': 'Import SEPA XMLs',
    'author': 'cm,',
    'data': [
        'wizard/payment_sepa_import_view.xml',
        'data/sequence.xml',
    ],
    'depends': [
        'account_sepa_direct_debit',
        'account_payment',
        'mail'

    ],
    'installable': True,
}
