{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1f30cdb6-b734-4776-822a-f50f13819b85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\u001b[31m:\u001b[39m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Asus\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3557: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import joblib\n",
    "import pandas as pd\n",
    "print(\"App started\")\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load model\n",
    "model = joblib.load(\"best_random_forest_model.pkl\")\n",
    "\n",
    "# List of input features\n",
    "features = [\n",
    "    \"age\", \"bp\", \"sg\", \"al\", \"su\", \"rbc\", \"pc\", \"pcc\", \"ba\",\n",
    "    \"bgr\", \"bu\", \"sc\", \"sod\", \"pot\", \"hemo\", \"pcv\", \"wc\", \"rc\",\n",
    "    \"htn\", \"dm\", \"cad\", \"appet\", \"pe\", \"ane\"\n",
    "]\n",
    "\n",
    "@app.route(\"/predict\", methods=[\"POST\"])\n",
    "def predict():\n",
    "    data = request.json\n",
    "\n",
    "    try:\n",
    "        input_df = pd.DataFrame([data], columns=features)\n",
    "        prediction = model.predict(input_df)[0]\n",
    "        result = \"Chronic Kidney Disease (CKD)\" if prediction == 1 else \"No CKD\"\n",
    "        return jsonify({\"prediction\": result})\n",
    "    except Exception as e:\n",
    "        return jsonify({\"error\": str(e)})\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad48d8cc-af6c-4453-83a9-55078f3cb104",
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
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
