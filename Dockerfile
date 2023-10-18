FROM fedora:38

RUN dnf install -y python3-pip git nodejs; dnf clean all

RUN pip install --no-cache-dir "jupyterlab<4" ipywidgets plotly pandas scikit-learn scikit-image jupyterlab-git

ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--notebook-dir=/app"]

