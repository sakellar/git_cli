export PYTHONPATH=.
PYTHONPATH=$PYTHONPATH:../src
python -m unittest test_executor
python ../src/run_cli.py
