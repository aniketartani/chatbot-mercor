<h1>Industry Growth Analysis with BERT Fine-Tune Model by Aniket Artani</h1>
Welcome to the Industry Growth Analysis code documentation! This code aims to help users analyze the growth percentages of various industries. Using a fine-tuned BERT model, the code allows users to find the industry with the highest or lowest growth on a given day or retrieve the growth percentage of a specific industry.

<h3>Problem Statement</h3>
The problem addressed by this code is to enable users to access and analyze industry growth data easily. Users should be able to perform the following tasks:

Find the industry with the highest growth percentage on a given time.<br>
Find the industry with the lowest growth percentage on a given day.<br>
Retrieve the growth percentage of a particular industry on a given day.<br>

<h3>Solution Overview</h3>
To solve the problem, we employed a BERT fine-tuned model, which is a state-of-the-art natural language processing model. We use this model to extract relevant information about industry growth from various sources. The key libraries used in this solution are:<br>

Transformers: A powerful library by Hugging Face that provides pre-trained NLP models, including BERT.<br>
Pandas: A versatile library for data manipulation and analysis.<br>
Beautiful Soup: A library for extracting data from HTML and XML files.<br>

<h3>Dependencies</h3>
Before running the code, please ensure you have the following dependencies installed:<br>
Python 3.x<br>
transformers (Hugging Face)<br>
pandas<br>
beautifulsoup4<br>

<h3>How to run</h3>
<div>
  <pre><code>
conda create --name textbase
conda activate textbase
conda install pip
pip install poetry
poetry install
poetry run python textbase/textbase_cli.py test main.py
  </code></pre>
</div>

<h3>Conclusion</h3>
This code enables users to analyze industry growth data using a fine-tuned BERT model. By providing options to find the industry with the highest or lowest growth percentage on a given day and retrieve the growth percentage of a specific industry, users can gain valuable insights into the current state of various industries.

<h3>References</h3>
Here are some references that might be helpful in understanding the components used in this code:

Hugging Face Transformers: https://huggingface.co/transformers/<br>
Pandas Documentation: https://pandas.pydata.org/docs/<br>
Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/<br>
<b>Remember to cite and credit the respective sources if you use any external information or libraries in your implementation.<b><br>

