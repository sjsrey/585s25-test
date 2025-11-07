# Spatial Data Science — Colab Course Template

This repository is a **starter template** for teaching Spatial Data Science using **Google Colab**.

## How to use

1. Create a new GitHub repo and upload these files.
2. Edit the Colab badge links below to point at your org/user and repo.
3. Share links in your LMS (Canvas) that open directly in Colab.

### Open directly in Colab

[![Open 01_intro in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sjsrey/585s25-test/blob/main/notebooks/01_intro.ipynb)

[![Open 02_spatial_weights in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sjsrey/585s25-test/blob/main/notebooks/02_spatial_weights.ipynb)

Replace `ORG_OR_USER/REPO_NAME` with your repo path.

## Contents

```
sds-course/
├─ notebooks/
│  ├─ 01_intro.ipynb
│  └─ 02_spatial_weights.ipynb
├─ data/
│  └─ neighborhoods.geojson
├─ requirements_colab.txt
├─ utils/
│  └─ plot.py
└─ README.md
```

## Notes

- Dependencies are installed **inside each notebook** (no conda).
- Use **Parquet/GeoJSON** for small demo datasets.
- For bigger datasets, fetch with `wget` or `gdown` in the notebook.
