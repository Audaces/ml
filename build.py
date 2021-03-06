from cx_Freeze import setup, Executable

win32_executables = [Executable('src/ml2po/__main__.py',
                                base=None,
                                targetName="ml2po.exe"),
                     Executable('src/po2ml/__main__.py',
                                base=None,
                                targetName="po2ml.exe"),
                     Executable('src/mlcppgen/__main__.py',
                                base=None,
                                targetName="mlcppgen.exe"),
                     Executable('src/mlpp/__main__.py',
                                base=None,
                                targetName="mlpp.exe"),
                     Executable('src/validate_tra/__main__.py',
                                base=None,
                                targetName="validate_tra.exe"),
                     ]

setup(
    name='ml',
    version='1.0',
    license='MIT',
    package_dir={'': 'src'},
    packages=[
        'ml',
        'mlpp',
        'mlcppgen',
        'ml2po',
        'po2ml',
        'validate_tra'
    ],
    executables=win32_executables,
)
