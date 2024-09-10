{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "008872c4-a9ee-485e-8f84-13e4f8711f03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python is easy\n",
      "ytho\n",
      "hon is ea\n",
      "p\n",
      "y\n",
      "python is easypython is easy\n"
     ]
    }
   ],
   "source": [
    "#string\n",
    "str=(\"python is easy\")\n",
    "print(str)\n",
    "print(str[1:5])\n",
    "print(str[3:12])\n",
    "print(str[0])\n",
    "print(str[-1])\n",
    "print(str*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "05831b44-8a88-4501-98c4-de9752152528",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "pcu\n",
      "('pcu', 10, 3.14)\n",
      "pcu\n",
      "98\n",
      "('a', 'pcu', 10, 3.14, 'a', 'pcu', 10, 3.14)\n",
      "('k', 98, 65.5, 'k', 98, 65.5)\n"
     ]
    }
   ],
   "source": [
    "#tuples\n",
    "tup1=('a','pcu',10,3.14)\n",
    "tup2=('k',98,65.5)\n",
    "print(tup1[0])\n",
    "print(tup1[1])\n",
    "print(tup1[1:4])\n",
    "print(tup1[-3])\n",
    "print(tup2[-2])\n",
    "print(tup1*2)\n",
    "print(tup2*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "2cedbcb8-a0b4-483b-ae82-53a310432912",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "['e', 64]\n",
      "o\n",
      "['a', 'e', 64, 92.4, 'a', 'e', 64, 92.4, 'a', 'e', 64, 92.4]\n",
      "['i', 'o', 78, 9.2, 'i', 'o', 78, 9.2, 'i', 'o', 78, 9.2, 'i', 'o', 78, 9.2, 'i', 'o', 78, 9.2]\n"
     ]
    }
   ],
   "source": [
    "#list\n",
    "list1=['a','e',64,92.4]\n",
    "list2=['i','o',78,9.2]\n",
    "print(list1[0])\n",
    "print(list1[1:3])\n",
    "print(list2[-3])\n",
    "print(list1*3)\n",
    "print(list2*5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "caef0eed-024c-465b-8203-cb822f7255e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "chocolate\n"
     ]
    }
   ],
   "source": [
    "#dictionary\n",
    "dict={\"item\":\"chocolate\",\"price\":100}\n",
    "print(dict['item'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5a1b8188-c598-4970-914c-77db165f4857",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the first side of triangle 2\n",
      "enter the second side of triangle 3\n",
      "enter the third side of triangle 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a= 2.0\n",
      "b= 3.0\n",
      "c= 4.0\n",
      "area of triangle is= 2.9047375096555625\n"
     ]
    }
   ],
   "source": [
    "#area_of_triangle\n",
    "a=float(input(\"enter the first side of triangle\"))\n",
    "b=float(input(\"enter the second side of triangle\"))\n",
    "c=float(input(\"enter the third side of triangle\"))\n",
    "sqrt=0\n",
    "print(\"a=\",a)\n",
    "print(\"b=\",b)\n",
    "print(\"c=\",c)\n",
    "s=(a+b+c)/2\n",
    "area=((s*(s-a)*(s-b)*(s-c))**0.5)\n",
    "print(\"area of triangle is=\",area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "fe26edf3-4035-41f6-a301-c9860e90b2a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter value of x1= 2\n",
      "enter value of x2= 3\n",
      "enter value of y1= 4\n",
      "enter value of y2= 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "distance= 1.4142135623730951\n"
     ]
    }
   ],
   "source": [
    "#distance betwwen two points\n",
    "x1=int(input(\"enter value of x1=\"))\n",
    "x2=int(input(\"enter value of x2=\"))\n",
    "y1=int(input(\"enter value of y1=\"))\n",
    "y2=int(input(\"enter value of y2=\"))\n",
    "distance=(((x2-x1)**2+(y2-y1)**2)**0.5)\n",
    "print(\"distance=\",distance)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "e6682df1-df16-46b4-bb95-cfe0ce00a029",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the radius of circle= 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "area= 12.56\n"
     ]
    }
   ],
   "source": [
    "#area of circle\n",
    "radius=float(input(\"enter the radius of circle=\"))\n",
    "area=3.14*radius*radius\n",
    "print(\"area=\",area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "4c6d5e52-9305-4d91-8f38-389dfb0b1bfa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the number= 12345\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "one's place= 5.0\n"
     ]
    }
   ],
   "source": [
    "#digit_at_one's_place\n",
    "num=float(input(\"enter the number=\"))\n",
    "one_place=num%10\n",
    "print(\"one's place=\",one_place)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "64b1ef03-92e6-4384-9647-ac3b5e96cdcf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter x= 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 <class 'int'>\n",
      "10 <class 'float'>\n"
     ]
    }
   ],
   "source": [
    "x=input(\"enter x=\")\n",
    "y=int(x)\n",
    "print(x,type(y))\n",
    "z=float(x)\n",
    "print(x,type(z))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "02bd31be-b7b6-498d-ac83-4b20a8c96d55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a character a\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ASCII VALUE= 97\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=input(\"enter a character\")\n",
    "print(\"ASCII VALUE=\",ord(a))\n",
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "69bec386-4bae-4f20-a7a2-8fbb8e5a1d06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "#length_of_list\n",
    "list1=['a','b','c',4,5]\n",
    "list2=['h',3,90]\n",
    "print(len(list1))\n",
    "print(len(list2))\n",
    "\n"
   ]
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
