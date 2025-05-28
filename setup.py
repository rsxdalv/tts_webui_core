import setuptools

setuptools.setup(
    name="tts_webui_core",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="rsxdalv",
    description="TTS WebUI Core",
    url="https://github.com/rsxdalv/tts_webui_core",
    project_urls={},
    scripts=[],
    install_requires=[
        "gradio",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
