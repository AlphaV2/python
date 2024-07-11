{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOt60Yt+CmpXd+KIN206yw2",
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
        "<a href=\"https://colab.research.google.com/github/AlphaV2/python/blob/main/session9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**sets**\n",
        "\n",
        "\n",
        "\n",
        "1.   It is an unordered collection of DataTypes\n",
        "2.   It doesnt allows duplicates\n",
        "3.   its mutable datatype\n",
        "4.   sets cannot be  access using indexing\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "bpKNRexeAWpc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Different types of sets in Python\n",
        "set1 = {1, 2, 3}\n",
        "set2 = set([3, 4, 5])\n",
        "set3 = set(\"Hello\")  # Creates a set of unique characters\n",
        "\n",
        "# Set operations\n",
        "union_set = set1 | set2  # Union of sets\n",
        "intersection_set = set1 & set2  # Intersection of sets\n",
        "difference_set = set1 - set2  # Difference of sets\n",
        "\n",
        "# Set methods\n",
        "set1.add(4)  # Add an element\n",
        "set1.remove(2)  # Remove an element (raises KeyError if not found)\n",
        "set1.discard(5)  # Remove an element if present (no error if not found)\n",
        "set1.pop()  # Remove and return an arbitrary element\n",
        "\n",
        "# Set functions\n",
        "len(set1)  # Returns the number of elements in the set\n",
        "max(set1)  # Returns the largest element in the set\n",
        "min(set1)  # Returns the smallest element in the set\n",
        "sum(set1)  # Returns the sum of all elements in the set\n",
        "sorted(set1)  # Returns a sorted list of the elements in the set\n",
        "\n",
        "# Checking for membership\n",
        "if 3 in set1:\n",
        "  print(\"3 is in the set\")\n",
        "\n",
        "# Iterating over a set\n",
        "for element in set1:\n",
        "  print(element)\n"
      ],
      "metadata": {
        "id": "fMoEdRSdDOWx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#initialization\n",
        "#use set () constructor for declaring empty set\n",
        "set2={}\n",
        "print(type(set2))\n",
        "set1={1,2,3,4}\n",
        "print(type(set1))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "17hXSKqXDT5a",
        "outputId": "1a516e19-a5d8-47c7-df0c-2db8e83b1ce0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'dict'>\n",
            "<class 'set'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#unordered  and cannot access sets using index and doesnt take duplicates\n",
        "set2={'a',2 ,\"hello\",\"sets\",\"tuples\",5}\n",
        "print(set2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ka5Wkm-nEniA",
        "outputId": "ebf630e1-38fa-4bac-e658-e91c9a9424f5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'a', 2, 'tuples', 'sets', 5, 'hello'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#true or 1\n",
        "set4={1,True,False,\"same\",\"any\"}\n",
        "print(set4)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-1ad8SGdFo6n",
        "outputId": "7bb67078-d3cf-446e-a8c1-38a5bfd4c50f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{False, 1, 'same', 'any'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#program to remove duplicate values from a list\n",
        "list1=[1,1,8,5,5,8,1,2,2,2,34,4,6,456,76]\n",
        "print(list1)\n",
        "list_rem=set(list1)\n",
        "print(list_rem)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vwbsYcS8GAER",
        "outputId": "6b569823-338b-4278-90a4-cd17bb1fd4cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 1, 8, 5, 5, 8, 1, 2, 2, 2, 34, 4, 6, 456, 76]\n",
            "{1, 2, 34, 4, 5, 6, 8, 456, 76}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#adding the elements of the  set\n",
        "print(\"Before adding to a set:\",set2)\n",
        "set2.add('ohayo')\n",
        "print(set2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lRK3G8OkHB8c",
        "outputId": "d5eba5c6-9d32-424e-a30a-ce08187eeb98"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Before adding to a set: {3, 4, 5, 6, 'ohayo', 90, 45}\n",
            "{3, 4, 5, 6, 'ohayo', 90, 45}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#intersect and union nad difference operations\n",
        "set1={1,2,3,5,4,4,90,45}\n",
        "set2={3,4,5,6,45,90}\n",
        "print(set1.intersection(set2))\n",
        "print(set1.union(set2))\n",
        "print(set1.difference(set2))\n",
        "#use operators for union and intersection and difference\n",
        "print(set1 | set2 )\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GPC6ghxAHlxf",
        "outputId": "75ab2940-9217-4433-9f34-b7fb63616e36"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{3, 4, 5, 45, 90}\n",
            "{1, 2, 3, 4, 5, 6, 45, 90}\n",
            "{1, 2}\n",
            "{1, 2, 3, 4, 5, 6, 45, 90}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#updating the set values\n",
        "set2.update(set4)\n",
        "print(\"updated set :\",set2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XjwdDZayKytY",
        "outputId": "105e863a-af2e-43ab-ba99-f03483004be5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "updated set : {False, 1, 2, 'tuples', 5, 'hello', 'ohayo', 'any', 'same', 'H', 'a', 'o', 'e', 'l', 'sets'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#intersection\n",
        "setc=set2.intersection(set4)\n",
        "print(setc)\n",
        "print(set2 & set4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vhLE8XdeLu16",
        "outputId": "2c82c512-a95b-49af-df46-41364f535016"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{False, 1, 'same', 'any'}\n",
            "{False, 1, 'same', 'any'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#difference  of a\n",
        "sets={1,3,555,8745,656,434}\n",
        "sets2={'gun','spam','eggs',33,43,34343,78787}\n",
        "print(sets,sets2)\n",
        "setz=sets2.pop()\n",
        "print(setz)\n",
        "print(sets.clear())\n",
        "\n",
        "# setd=set2.difference(set4)\n",
        "# print(setc)\n",
        "# print(setd)\n",
        "# print(set2-set4)\n",
        "# print(setd.remove(\"hello\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o8ndE65oM6yu",
        "outputId": "6c017133-7a27-4016-b4b4-60d00626bfa5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{656, 1, 434, 3, 8745, 555} {33, 78787, 'spam', 34343, 'eggs', 43, 'gun'}\n",
            "33\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "elements={2,3,5,6,66,77,88,99,-798}\n",
        "print(max(elements))\n",
        "print(min(elements))\n",
        "for a in elements:\n",
        "  print(\"iterated using for loop\",a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7kszQ1WrPnBB",
        "outputId": "775e2e0d-5938-4e50-c9a1-6441ad3d0c34"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "99\n",
            "-798\n",
            "iterated using for loop 66\n",
            "iterated using for loop 3\n",
            "iterated using for loop 2\n",
            "iterated using for loop 5\n",
            "iterated using for loop 6\n",
            "iterated using for loop 99\n",
            "iterated using for loop -798\n",
            "iterated using for loop 77\n",
            "iterated using for loop 88\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "elements_copy=elements.copy()\n",
        "print(\"original list:\",elements)\n",
        "print(\"copied elements:\",elements_copy)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jc8P1NdFQe4v",
        "outputId": "1d4c113b-f11d-4100-bf7c-338136b3a880"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "original list: {66, 3, 2, 5, 6, 99, -798, 77, 88}\n",
            "copied elements: {66, 3, 2, 5, 6, 99, -798, 77, 88}\n"
          ]
        }
      ]
    }
  ]
}