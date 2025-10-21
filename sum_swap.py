{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "229559f4-0c61-49a7-9032-660b85a9e489",
   "metadata": {},
   "outputs": [],
   "source": [
    "def swap_sum(A, B):\n",
    "    \n",
    "    SA = sum(A)\n",
    "    SB = sum(B)\n",
    "\n",
    "    D = SB - SA - 10\n",
    "    if D % 2 != 0:\n",
    "        return None  \n",
    "\n",
    "    t = D // 2  \n",
    "\n",
    "    i, j = 0, 0\n",
    "    n, m = len(A), len(B)\n",
    "\n",
    "    while i < n and j < m:\n",
    "        diff = B[j] - A[i]\n",
    "        if diff == t:\n",
    "            return (i, j)\n",
    "        elif diff < t:\n",
    "            j += 1  \n",
    "        else:\n",
    "            i += 1  \n",
    "\n",
    "    return None\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64b73bdf-3d56-48fd-8a0b-f1b454654ae5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
