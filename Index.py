{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyMQmicKHeQ9GRw+NBAJUEiv",
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
        "<a href=\"https://colab.research.google.com/github/RT-86/Ensemble-Techniques/blob/main/Index.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task\n",
        "Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).\n",
        "Note:  is considered to be an even index.\n",
        "Example\n",
        "\n",
        "Print abc def"
      ],
      "metadata": {
        "id": "7k3R3DVRgwCL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n=int(input())\n",
        "for i in range(n):\n",
        "    s=input()\n",
        "    a = ''\n",
        "    b = ''\n",
        "    for i in range(len(s)):\n",
        "        if i%2==0:\n",
        "            a+=s[i]\n",
        "        elif i%2!=0:\n",
        "            b+=s[i]\n",
        "    print(a,' ',b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hoc8W6tvxs04",
        "outputId": "a89db07c-72a7-4c78-f08c-ad68704aac03"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "hacker\n",
            "hce   akr\n",
            "rank\n",
            "rn   ak\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "wK_R73aPZIXs"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}