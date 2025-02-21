from setuptools import find_packages, setup

setup(
    name="autosave-sublime",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
    scripts=["scripts/autosave_sublime_setup.py"],
    entry_points={
        "console_scripts": [
            "autosave-sublime-setup=scripts.autosave_sublime_setup:main",
        ],
    },
    package_data={
        "autosave_sublime": ["auto_save_new_files.py", "AutoSaveNewFiles.sublime-settings"],
    },
)
