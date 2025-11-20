{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyMWVJe/7WhTRbVgEoxsn7Ks",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bahattinyaylagul-sketch/clevel-seo-forecast/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qdKcf9HuXhFd"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "96f59749"
      },
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "import numpy as np\n",
        "import statsmodels.api as sm\n",
        "\n",
        "st.set_page_config(page_title=\"C-Level SEO Forecast\", layout=\"wide\")\n",
        "\n",
        "st.markdown(\"\"\"\n",
        "<style>\n",
        "[data-testid=\"stSidebar\"] {display: none;}\n",
        ".block-container {padding: 2rem 4rem;}\n",
        "h1, h2, h3 {font-family: 'Inter', sans-serif !important; font-weight: 600 !important; color: #111 !important;}\n",
        ".card {background:#fff; padding:1.5rem; border-radius:12px; border:1px solid #e5e7eb; box-shadow:0px 1px 3px rgba(0,0,0,0.06); margin-bottom:1.2rem;}\n",
        ".kpi {background:#f9fafb; padding:1.2rem; border-radius:10px; border:1px solid #E5E7EB; text-align:center;}\n",
        "</style>\n",
        "\"\"\", unsafe_allow_html=True)\n",
        "\n",
        "st.markdown(\"\"\"\n",
        "<div class=\"card\">\n",
        "    <h1 style=\"margin-bottom:4px;\">C-Level SEO Forecast Tool</h1>\n",
        "    <p style=\"color:#666; margin-top:0px;\">Temiz ve profesyonel SEO tahmin aracı.</p>\n",
        "</div>\n",
        "\"\"\", unsafe_allow_html=True)\n",
        "\n",
        "st.markdown(\"<div class='card'>\", unsafe_allow_html=True)\n",
        "st.subheader(\"1) Google Search Console CSV Yükle\")\n",
        "uploaded = st.file_uploader(\"CSV dosyası seçin\", type=[\"csv\"])\n",
        "st.markdown(\"</div>\", unsafe_allow_html=True)\n",
        "\n",
        "if uploaded:\n",
        "    df = pd.read_csv(uploaded)\n",
        "    st.markdown(\"<div class='card'>\", unsafe_allow_html=True)\n",
        "    st.subheader(\"Veri Önizleme\")\n",
        "    st.dataframe(df.head(), use_container_width=True)\n",
        "    st.markdown(\"</div>\", unsafe_allow_html=True)\n",
        "\n",
        "    clicks = df[\"Clicks\"].sum() if \"Clicks\" in df else 0\n",
        "    imp = df[\"Impressions\"].sum() if \"Impressions\" in df else 0\n",
        "    ctr = (clicks / imp) * 100 if imp > 0 else 0\n",
        "\n",
        "    col1, col2, col3 = st.columns(3)\n",
        "    with col1: st.markdown(f\"<div class='kpi'><h3>{clicks}</h3><p>Toplam Clicks</p></div>\", unsafe_allow_html=True)\n",
        "    with col2: st.markdown(f\"<div class='kpi'><h3>{imp}</h3><p>Toplam Impressions</p></div>\", unsafe_allow_html=True)\n",
        "    # The user's provided code was cut off, so I'm completing it based on typical Streamlit patterns\n",
        "    with col3: st.markdown(f\"<div class='kpi'><h3>{ctr:.2f}%</h3><p>Ortalama CTR</p></div>\", unsafe_allow_html=True)\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c765beaa",
        "outputId": "ebaa582b-6286-48b7-f577-f492f5f69cb2"
      },
      "source": [
        "%%writefile requirements.txt\n",
        "streamlit\n",
        "pandas\n",
        "plotly\n",
        "numpy\n",
        "statsmodels"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing requirements.txt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "FKODCTbGZHj-"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}