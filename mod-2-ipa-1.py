{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "43b689fe-b08f-4bcb-9bc9-c932f0aa51ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    '''\n",
    "    Savings.\n",
    "    5 points.\n",
    "    This function calculates the money remaining\n",
    "        for an employee after taxes and expenses.\n",
    "    \n",
    "    To get the take-home pay of an employee, we will\n",
    "        follow the following process:\n",
    "        1. Apply the tax rate to the gross pay of the employee; round down\n",
    "        2. Subtract the expenses from the after-tax pay of the employee\n",
    "        \n",
    "    Parameters\n",
    "    ----------\n",
    "    gross_pay: int\n",
    "        the gross pay of an employee for a certain time period, expressed in centavos\n",
    "    tax_rate: float\n",
    "        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)\n",
    "    expenses: int\n",
    "        the expenses of an employee for a certain time period, expressed in centavos\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the number of centavos remaining from an employee's pay after taxes and expenses\n",
    "    '''\n",
    "    return int((((gross_pay - (gross_pay * tax_rate)) - expenses))*100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0abafea5-4c65-4f78-a7c8-179db3f3f602",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6800"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "savings(100,0.07,25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b1de87e4-55e7-4068-badc-81451c1d37fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "52500"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "savings(1000,0.27,205)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8ba0b744-8a0c-4b0b-ab0b-05057284974f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9524"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "savings(123,0.12,13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6265e037-6167-484a-b8cb-93339db465f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def interest(principal, rate, periods):\n",
    "    '''\n",
    "    Interest.\n",
    "    5 points.\n",
    "    This function calculates the final value of an investment after\n",
    "        gaining simple interest over a number of periods.\n",
    "    To calculate simple interest, simply multiply the principal to the quantity (rate * time). \n",
    "        Add this amount to the principal to get the final value.\n",
    "    Round down the final amount.\n",
    "    Parameters\n",
    "    ----------\n",
    "    principal: int\n",
    "        the principal (i.e., starting) amount invested, expressed in centavos\n",
    "    rate: float\n",
    "        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)\n",
    "    periods: int\n",
    "        the number of periods invested\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the final value of the investment\n",
    "    '''\n",
    "    return int((principal + (principal * (rate * periods))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ac3b1941-4e6b-485e-8987-4e78525a1114",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8500"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "interest(100,21,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3e69b3ff-3f8c-4797-873f-871fe2846e57",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1216"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "interest(234,0.6,7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e1215f74-7a63-48f7-a8c9-e6f49b498a05",
   "metadata": {},
   "outputs": [],
   "source": [
    "def body_mass_index(weight, height):\n",
    "    '''\n",
    "    Body Mass Index.\n",
    "    5 points.\n",
    "    This function calculates the body mass index (BMI) of a person\n",
    "        given their weight and height.\n",
    "    The formula for BMI is: kg / (m ^ 2)\n",
    "        (i.e., kilograms over meters squared)\n",
    "    Unfortunately, the users of this function use the imperial system.\n",
    "        You will need to first convert their arguments to the metric system.\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    weight: float\n",
    "        the weight of the person, in pounds\n",
    "    height: list\n",
    "        the height of the person, expressed as a list of two integers.\n",
    "        the first integer is the foot component of their height.\n",
    "        the second integer is the inches component of their height.\n",
    "        for example, 5'10\" would be passed as [5, 10].\n",
    "    Returns\n",
    "    -------\n",
    "    float\n",
    "        the BMI of the person.\n",
    "    '''\n",
    "    \n",
    "    return float(((weight/2.2) / ((height[0]*(12*2.54)) * (height[1]*2.54))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "261818fb-4243-416f-9884-a6257688dffb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.06282209534116037"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "body_mass_index(107, [5, 2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "21ab0424-2b10-49ea-96cd-af3c956a8aa0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0733902982957481"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "body_mass_index(150, [6, 2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d7ac0e1d-0f52-40c5-942f-4edf5fd9ab14",
   "metadata": {},
   "outputs": [],
   "source": [
    "def material_waste(total_material, material_units, num_jobs, job_consumption):\n",
    "    '''\n",
    "    Material Waste.\n",
    "    5 points.\n",
    "    This function calculates how much material input will be wasted\n",
    "        after running a certain number of jobs that consume\n",
    "        a set amount of material.\n",
    "    To get the waste of a set of jobs:\n",
    "        1. Multiply the number of jobs by the material consumption per job.\n",
    "        2. Subtract the total material consumed from the total material available.\n",
    "    The users of this function also want you to format the output as a string, annotated with the\n",
    "        units in which the material is expressed. Do not add a space between the number and the unit.\n",
    "    Parameters\n",
    "    ----------\n",
    "    total_material: int\n",
    "        the total material available\n",
    "    material_units: str\n",
    "        the units used to express a quantity of the material (e.g., \"kg\", \"L\", etc.)\n",
    "    num_jobs: int\n",
    "        the number of jobs to run\n",
    "    job_consumption: int\n",
    "        the amount of material consumed per job\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the amount of remaining material expressed with its unit (e.g., \"10kg\").\n",
    "    '''\n",
    "    return str(total_material - (num_jobs * job_consumption))+ (material_units)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7990db4d-f1f0-4cf7-972d-261152ca0360",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'82kg'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "material_waste(100,\"kg\",6,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "df4b2236-9e8c-40d6-a4d2-18821766388a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'39ml'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "material_waste(234,\"ml\",39,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e724074b-9a36-4fc5-a878-5a3f39328581",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31afbea9-4952-4207-ae1b-278efe14e1b9",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
