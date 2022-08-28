# Basket_Test
This test was developed to check availability of the "Add to basket" button on  http://selenium1py.pythonanywhere.com.

## Installation

MacOS only.

Setup an environment:

```bash
git clone https://github.com/AAI1992/Basket_Test
cd Basket_Test
python3 -m venv env
source env/bin/activate
pip install -r requirments.txt
```

Check the task:
```bash
pytest --browser_name=<your_browser> --language=<your_language> test_items.py
```
