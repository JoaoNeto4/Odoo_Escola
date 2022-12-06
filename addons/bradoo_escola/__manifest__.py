{
    'name': 'Bradoo Escolas',
    'summary': 'Projeto de Treinamento',
    'version': '1.0.1',
    'sequence': 1,
    'author': 'João',
    'depends': [
        'base',
        'web',
        'sale_management',
        'hr',
        'l10n_br',
    ],
    'data': [
        'data/job_data.xml',
        'data/courses_data.xml',
        'data/department_data.xml',
        'data/employee_data.xml',

        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/security_data.xml',

        'views/product_template/form.xml',

        'views/bradoo_escola_class/tree.xml',
        'views/bradoo_escola_class/action.xml',
        'views/bradoo_escola_class/form.xml', 
        'views/bradoo_escola_class/search.xml',        
  
        'views/bradoo_escola_attendance/tree.xml',
        'views/bradoo_escola_attendance/form.xml',
        'views/bradoo_escola_attendance/action.xml',

        'views/bradoo_escola_course/tree.xml',
        'views/bradoo_escola_course/form.xml',
        'views/bradoo_escola_course/action.xml',

        'views/hr_employee/form.xml',

        'views/bradoo_escola_lesson/tree.xml',
        'views/bradoo_escola_lesson/form.xml',
        'views/bradoo_escola_lesson/action.xml',

        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}